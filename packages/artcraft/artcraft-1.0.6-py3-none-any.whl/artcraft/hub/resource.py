import re
import os
import cgi
import json
import shutil
import hashlib
import zipfile
import requests
import subprocess
import dataclasses
from PIL import Image
from tqdm import tqdm
from io import BytesIO
from urllib.parse import unquote
from urllib.request import urlopen

from .model import ModelType, NetworkType, ModelHub, ModelMeta, get_or_create_dir, exists_path


@dataclasses.dataclass
class Resource:
    hub: ModelHub

    def convert(self, tmp_dir: str, base_name: str):
        if self.hub.model_type == ModelType.Checkpoint:
            print("convert checkpoint:", tmp_dir, base_name)
            convert_checkpoint(tmp_dir, base_name)
            print("convert done:", tmp_dir, base_name)
            return tmp_dir, ""
        return tmp_dir, base_name

    def retrieve(self, *args, **kwargs):
        raise NotImplemented()


def convert_checkpoint(tmp_dir: str, base_name: str):
    if not base_name or not base_name.endswith(".safetensors"):
        raise ValueError(f"convert failed, invalid file")
    tmp_path = os.path.join(tmp_dir, base_name)
    dump_dir = tmp_dir

    script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts")
    script_file = os.path.join(script_dir, "convert_original_stable_diffusion_to_diffusers.py")
    config_path = os.path.join(tmp_dir, "config.yaml")

    if not os.path.exists(script_file):
        raise ValueError("convert script not found")

    cmd = ["python",
           script_file,
           "--checkpoint_path",
           tmp_path,
           "--dump_path",
           dump_dir,
           "--from_safetensors",
           "--half"]

    if os.path.exists(config_path):
        cmd.extend(["--config_files", config_path])

    bar = tqdm(total=1, desc="convert")
    code = subprocess.call(cmd)
    if code != 0:
        raise ValueError("convert failed")
    bar.update(1)
    bar.close()


class FakeResource(Resource):
    def retrieve(self):
        pass


class FileResource(Resource):
    def retrieve(self, model_id: str, file: str = None, thumbnail: str = None, force: bool = False):
        if not model_id:
            raise ValueError("model_id is empty")
        model_id = valid_name(model_id)
        if not file and not thumbnail:
            raise ValueError("need file or thumbnail")

        if file is not None:
            file = valid_filename(file, valid_name)
            self.retrieve_model(model_id, file, force)
        if thumbnail is not None:
            self.retrieve_thumbnail(model_id, thumbnail)
        return self.hub.get_or_create_model_dir(model_id)

    def retrieve_model(self, model_id: str, file: str, force: bool = False):
        if not force and self.hub.contains(model_id):
            raise FileExistsError(f"model_id:{model_id} already exists, try force mode")
        if not os.path.isfile(file):
            raise ValueError(f"{file} is not a file")

        tmp_dir, base_name = upload_resource(file)
        if base_name:
            tmp_dir, base_name = self.convert(tmp_dir, base_name)

        self.hub.add_model(model_id, tmp_dir=tmp_dir)
        self.hub.add_meta(model_id, meta=ModelMeta(weight_file=base_name))

    def retrieve_thumbnail(self, model_id: str, thumbnail_file: str):
        if not self.hub.contains(model_id):
            raise FileNotFoundError((f"model_id:{model_id} not found"))

        img = Image.open(thumbnail_file)
        img = format_thumbnail(img)
        self.hub.add_thumbnail(model_id, img)


class URLResource(Resource):
    def retrieve(self,
                 model_id: str,
                 model_url: str,
                 remote_name: str = None,
                 thumbnail_url: str = None,
                 proxy=None,
                 force: bool = False):
        if not model_id:
            raise ValueError("model_id is empty")
        model_id = valid_name(model_id)
        if not model_url:
            raise ValueError("model_url is empty")
        if not force and self.hub.contains(model_id):
            raise FileExistsError(f"model_id:{model_id} already exists, try force mode")

        # download
        tmp_dir, base_name = download_resource(model_url,
                                               thumbnail_url,
                                               remote_name,
                                               force=force,
                                               proxy=proxy)
        tmp_dir, base_name = self.convert(tmp_dir, base_name)
        self.hub.add_model(model_id, tmp_dir=tmp_dir)
        self.hub.add_meta(model_id, meta=ModelMeta(weight_file=base_name))
        return self.hub.get_or_create_model_dir(model_id)


class CivitaiResource(Resource):
    def query_info(self, id: str, revision: str, proxy=None):
        if not revision:
            raise ValueError("revision is empty")
        url = f"https://civitai.com/api/v1/models/{id}"
        print(url)
        resp = json.loads(requests.get(url, proxies=proxy).text)
        model_name = format_name(resp["name"])
        model_type = resp["type"]
        versions = resp["modelVersions"]

        version = [v for v in versions if str(v["name"]) == revision]
        if len(version) == 0:
            raise ValueError(f"version {revision} not found")
        version = version[0]
        version_name = format_name(version["name"])
        trained_word = version.get("trainedWords")
        base_model = version.get("baseModel")

        files = []
        configs = []
        for f in version["files"]:
            if f["type"] != "Config":
                configs.append(f)
            if f["type"] != "Model":
                continue
            if not f["name"].endswith(".safetensors"):
                continue
            files.append(f)

        config = configs[0] if len(configs) > 0 else {}

        # choose small one
        files.sort(key=lambda x: float(x.get("sizeKB", 1000000000)))
        if len(files) == 0:
            raise ValueError(f"{id}/{revision} cannot find safetensors resource")
        file = files[0]

        file_name = file.get("name")
        model_url = file.get("downloadUrl")
        images = version.get("images", [])
        if len(images) == 0:
            thumbnail_url = None
        else:
            thumbnail_url = images[0]["url"]

        t, b = self.check_hub(model_type, base_model)

        return {
            "base_model": b,
            "model_url": model_url,
            "model_type": t,
            "model_name": model_name,
            "file_name": file_name,
            "config": config,
            "version_name": version_name,
            "trained_word": trained_word,
            "thumbnail_url": thumbnail_url
        }

    def check_hub(self, model_type: str, base_model: str) -> (ModelType, NetworkType):
        model_type_mapping = {
            "Checkpoint": ModelType.Checkpoint,
            "LORA": ModelType.Lora,
            "LoCon": ModelType.Lycoris,
            "TextualInversion": ModelType.Embedding,
        }
        base_model_mapping = {
            "SD 1.5": NetworkType.SD_1_5,
            "SDXL 1.0": NetworkType.SDXL_1_0,
        }

        t = model_type_mapping.get(model_type, None)
        b = base_model_mapping.get(base_model, None)

        if b is None or t is None:
            raise ValueError(f"{base_model} is not supported for Civitai downloader")
        if b.value != self.hub.network_type:
            raise ValueError(f"expected base_model is {self.hub.network_type}, but get {b.value}")
        if t.value != self.hub.model_type:
            raise ValueError(f"expected model_type is {self.hub.model_type}, but get {t.value}")
        return t.value, b.value

    def retrieve(self, id: str, revision: str, proxy=None, force=False, ):
        info = self.query_info(id, revision, proxy=proxy)
        model_url = info.get("model_url")
        thumbnail_url = info.get("thumbnail_url")
        config = info.get("config")

        model_id = os.path.join(info.get("model_name"), info.get("version_name"))
        model_id = format_name(model_id)
        if not force and self.hub.contains(model_id):
            raise FileExistsError(f"model_id:{model_id} already exists, try force mode")

        # download
        tmp_dir, base_name = download_resource(model_url,
                                               thumbnail_url,
                                               remote_name=info.get("file_name", None),
                                               force=force,
                                               proxy=proxy)
        if config:
            config_url = config.get("downloadUrl")
            config_file_name = config.get("name")
            if config_file_name.endswith(".yaml"):
                download_model(config_url, tmp_dir, remote_name="config.yaml")

        tmp_dir, base_name = self.convert(tmp_dir, base_name)
        self.hub.add_model(model_id, tmp_dir=tmp_dir)
        self.hub.add_meta(model_id, meta=ModelMeta(weight_file=base_name,
                                                   trained_word=info.get("trained_word")))
        return self.hub.get_or_create_model_dir(model_id)


def download_resource(model_url: str,
                      thumbnail_url: str = None,
                      remote_name: str = None,
                      force=False,
                      proxy=None) -> (str, str):
    folder = hashlib.md5(model_url.encode("utf-8")).hexdigest()
    paths = [".tmp", folder]

    if force:
        tmp_dir = get_or_create_dir(*paths)
        shutil.rmtree(tmp_dir)

    if exists_path(*paths):
        tmp_dir = get_or_create_dir(*paths)
        base_name = download_model_name(model_url, remote_name, proxy)
        if exists_path(*paths, base_name):
            return tmp_dir, base_name
        else:
            shutil.rmtree(tmp_dir)

    tmp_dir = get_or_create_dir(*paths)
    base_name = download_model(model_url, tmp_dir, remote_name, proxy=proxy)
    if thumbnail_url:
        download_thumbnail(thumbnail_url, tmp_dir, proxy=proxy)
    return tmp_dir, base_name


def upload_resource(file: str) -> (str, str):
    tmp_dir = get_or_create_dir(".tmp", hashlib.md5(file.encode("utf-8")).hexdigest())
    if file.endswith(".zip"):
        with zipfile.ZipFile(file, 'r') as f:
            f.extractall(tmp_dir)
        return tmp_dir, ""
    base_name = os.path.basename(file)
    shutil.copy2(file, os.path.join(tmp_dir, base_name))
    return tmp_dir, base_name


def download_model_name(url: str, remote_name: str = None, proxy=None) -> str:
    base_name = remote_name
    if not remote_name:
        base_name = _remote_name(url)
    return valid_filename(base_name, format_name)


def download_model(url: str, target_dir: str, remote_name: str = None, proxy=None) -> str:
    base_name = download_model_name(url, remote_name, proxy)
    _download_file(url, os.path.join(target_dir, base_name), proxy)
    return base_name


def download_thumbnail(url: str, target_dir: str, proxy=None) -> str:
    base_name = "thumbnail.jpg"
    target_file = os.path.join(target_dir, base_name)
    _download_image(url, target_file, proxy=proxy)
    return base_name


# todo: add proxy
def _remote_name(url: str) -> str:
    remote_name = ""
    try:
        remote_file = urlopen(url)
        _, params = cgi.parse_header(remote_file.info()['Content-Disposition'])
        remote_name = params['filename']
        if remote_name == "":
            raise ValueError("remote name is empty")
    except:
        remote_name = "pytorch_model.safetensors"
    finally:
        name = unquote(remote_name).replace(" ", "")
        return name


def _download_file(url: str, target_file: str, proxy=None):
    response = requests.get(url, stream=True, proxies=proxy)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    progress_bar = tqdm(total=total_size_in_bytes, unit_scale=True, unit_divisor=1024, desc="downloading", unit="")
    try:
        block_size = 1024
        with open(target_file, 'wb') as f:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
    finally:
        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            os.remove(target_file)
            raise ValueError(f"download file: {target_file} fails")


def _download_image(url: str, target_file: str, resize: bool = True, proxy=None):
    img = Image.open(BytesIO(requests.get(url, proxies=proxy).content))
    if resize:
        img = format_thumbnail(img)
    img = img.convert("RGB")
    img.save(target_file)


def format_thumbnail(img: Image) -> Image:
    w, h = img.size
    ratio = max(w, h) / 480
    w, h = int(w / ratio), int(h / ratio)
    return img.resize((w, h))


NUM_LETTER = re.compile("^(?!\d+$)[\da-zA-Z_]+$")


def valid_name(name: str):
    if not NUM_LETTER.search(name):
        raise ValueError(f"{name} is invalid, only numbers, letters, and underscores are allowed")
    return name


def valid_filename(filename: str, fn):
    base_name = os.path.basename(filename)
    dir_name = os.path.dirname(filename)

    names = base_name.split(".")
    if len(names) != 2:
        raise ValueError(f"invalid file:{filename}, lack extension")

    return os.path.join(dir_name, f"{fn(names[0])}.{names[1]}")


def format_name(name: str) -> str:
    def contain_chinese(string):
        for ch in string:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True

    name = name.replace(" ", "_").replace(".", "_").replace("__", "_").lower()
    parts = name.split("_")
    return "_".join([s for s in parts if not contain_chinese(s)])
