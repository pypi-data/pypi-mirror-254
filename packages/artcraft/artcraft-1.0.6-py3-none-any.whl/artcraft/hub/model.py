import os
import re
import json
import enum
import shutil
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from pathlib import Path
from dataclasses import dataclass, asdict, field

UNAVAILABLE_SUFFIX = "(unavailable)"


class NetworkType(str, enum.Enum):
    SD_1_5 = "sd1.5"
    SDXL_1_0 = "sdxl1.0"
    Other = "other"


class ModelType(str, enum.Enum):
    Vae = "vae"
    Adapter = "adapter"
    UpScaler = "upscaler"
    Checkpoint = "checkpoint"
    Lora = "lora"
    Lycoris = "lycoris"
    Embedding = "embedding"
    ControlNet = "controlnet"


@dataclass
class ModelMeta:
    sub_path: str = ""
    weight_file: str = ""
    trained_word: list[str] = field(default_factory=list)


class ModelHub:
    def __init__(self, network_type: str, model_type: str):
        self.network_type = NetworkType(network_type).value
        self.model_type = ModelType(model_type).value

    def contains(self, model_id) -> bool:
        return exists_path(self.network_type, self.model_type, model_id)

    def get_or_create_model_dir(self, model_id: str) -> str:
        return get_or_create_dir(
            self.network_type,
            self.model_type,
            model_id)

    def extract_model_path(self, model_id: str):
        if not self.contains(model_id):
            raise FileNotFoundError(f"{model_id} not found")
        model_dir = self.get_or_create_model_dir(model_id)
        weight_file = self.extract_meta(model_id).weight_file
        return os.path.join(model_dir, weight_file)

    def add_model(self, model_id: str, tmp_dir: str):
        if not model_id:
            raise ValueError("model id is empty")
        if not tmp_dir or not os.path.exists(tmp_dir):
            raise ValueError(f"tmp_dir:{tmp_dir} not found")
        target_dir = self.get_or_create_model_dir(model_id)
        if os.path.isfile(tmp_dir):
            shutil.copy2(tmp_dir, target_dir)
        else:
            shutil.copytree(tmp_dir, target_dir, dirs_exist_ok=True)

    def remove_model(self, model_id: str):
        if not model_id:
            raise ValueError("model id is empty")
        if not self.contains(model_id):
            raise FileNotFoundError("model id not found")
        root = self.get_or_create_model_dir("")
        trash = os.path.join(root, ".trash")
        with open(trash, "a") as f:
            f.write(model_id + "\n")

    def add_meta(self, model_id: str, meta: ModelMeta) -> ModelMeta:
        if not model_id:
            raise ValueError("model id is empty")
        model_dir = self.get_or_create_model_dir(model_id)
        meta_file = os.path.join(model_dir, "model_meta.json")
        with open(meta_file, "w") as f:
            json.dump(asdict(meta), f)
        return meta

    def extract_meta(self, model_id: str) -> ModelMeta:
        model_dir = self.get_or_create_model_dir(model_id)
        meta_file = os.path.join(model_dir, "model_meta.json")
        try:
            with open(meta_file) as f:
                return ModelMeta(**json.load(f))
        except:
            return ModelMeta()

    def add_thumbnail(self, model_id: str, image: Image):
        model_dir = self.get_or_create_model_dir(model_id)
        thumbnail_file = os.path.join(model_dir, "thumbnail.jpg")
        image.save(thumbnail_file, quality=100)

    def extract_thumbnail(self, model_id: str) -> Image:
        model_dir = self.get_or_create_model_dir(model_id)
        thumbnail_file = os.path.join(model_dir, "thumbnail.jpg")
        try:
            return Image.open(thumbnail_file)
        except:
            return None

    # level order traverse
    def find_models(self) -> list[str]:
        model_ids = []
        root = self.get_or_create_model_dir("")
        queue = [root]
        while len(queue) > 0:
            _dir = queue.pop(0)
            has_file = False
            if os.path.isfile(_dir):
                continue

            for sub_dir in os.listdir(_dir):
                f = os.path.join(_dir, sub_dir)
                if os.path.isfile(f) and sub_dir != ".trash":
                    model_ids.append(os.path.relpath(_dir, root))
                    has_file = True
                    break

            if not has_file:
                for sub_dir in os.listdir(_dir):
                    f = os.path.join(_dir, sub_dir)
                    queue.append(f)

        trash = os.path.join(root, ".trash")
        try:
            with open(trash, "r") as f:
                deleted = [line.strip("\n") for line in f.readlines()]
                model_ids = [i for i in model_ids if i not in deleted]
        except:
            pass
        return model_ids


class CachedModelHub(ModelHub):
    info = None

    def update(self):
        info = {}
        for model_id in self.find_models():
            meta = self.extract_meta(model_id)
            thumbnail = self.extract_thumbnail(model_id)
            if thumbnail is None:
                thumbnail = DEFAULT_THUMBNAIL
            info[model_id] = (meta, thumbnail)
        self.info = info

    @property
    def model_ids(self):
        return [model_id for model_id in self.info.keys()]

    @property
    def thumbnails(self):
        return [(thumbnail, model_id) for model_id, (_, thumbnail) in self.info.items()]

    def get_meta(self, model_id: str):
        return self.info[model_id][0]


def get_or_create_dir(*paths: str, cache_dir: str = None, exists_ok=True):
    if not cache_dir:
        # todo: replace artcraft to artcraft
        cache_dir = os.environ.get("ARTCRAFT_CACHE", Path.home().joinpath(".cache", "artcraft"))
    _path = os.path.join(cache_dir, *paths)

    if not os.path.exists(_path):
        Path(_path).mkdir(parents=True)
    elif not exists_ok:
        raise FileExistsError(f"file {_path} exists")
    return _path


def exists_path(*paths: str, cache_dir: str = None):
    cache_dir = get_or_create_dir(cache_dir=cache_dir)
    _path = os.path.join(cache_dir, *paths)
    if not os.path.exists(_path):
        return False
    else:
        return True


def must_exists(model_id: str, network_type: NetworkType, model_type: ModelType):
    hub = ModelHub(network_type, model_type)
    try:
        hub.extract_model_path(model_id)
    except FileNotFoundError:
        print(f"{network_type}:{model_type}:{model_id} cannot found, please download/upload if you want use it.")
        return model_id + UNAVAILABLE_SUFFIX
    return model_id


def camel2snake(string):
    return re.sub(r'(?!^)([A-Z]+)', r'_\1', string).lower()


def add_text(img: Image, text: str, font=None):
    drawing = ImageDraw.Draw(img)
    # position
    _, _, w, h = drawing.textbbox((0, 0), text=text, font=font)
    pos = (img.size[0] // 2 - w // 2, img.size[1] // 2 - h // 2)
    # add text
    drawing.text(pos, text, fill=(33, 33, 33), font=font)
    return img


def default_thumbnail() -> Image:
    img = Image.new("RGB", (480, 854), 0x7F7F7F)
    font = ImageFont.load_default(size=84)
    img = add_text(img, "Thumbnail", font=font)
    return img


DEFAULT_THUMBNAIL = default_thumbnail()
