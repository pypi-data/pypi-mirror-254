from PIL import Image
import gradio as gr
from dataclasses import dataclass

from .util import UI, OneHotLayoutUI
from artcraft.hub import (
    ModelType,
    NetworkType,
    CachedModelHub,
    UNAVAILABLE_SUFFIX
)
from artcraft.pipeline import (
    SDPipeline,
    enhance_factory,
    flush_gpu,
    SCHEDULER_LIST,
    UPSCALER_LIST,
    RESTORER_LIST,
    LCM_SCHEDULER_LIST,
    resize
)


def image2image(
        network_type: NetworkType,
        base_model: str,
        vae: str,
        lora_specs: list[tuple[str, str | float]],
        embedding_specs: list[tuple[str, float]],
        # ------
        image: Image,
        prompt: str,
        neg_prompt: str,
        scheduler: str,
        sampling_steps: int,
        cfg: float,
        clip_skip: int,
        strength: float,
        seed: int,
        image_num: int,
        # -----
        upscaler_method: str,
        restorer_method: str,
        enhance_scale: float,
        enhance_strength: float,
        process=gr.Progress(track_tqdm=True)):
    if not base_model:
        raise ValueError("base_model is empty")

    embedding_adapters = [i[0] for i in embedding_specs] if embedding_specs else []
    lora_adapters = [(k, float(v)) for k, v in lora_specs] if lora_specs else []

    memory_efficient = scheduler not in LCM_SCHEDULER_LIST[network_type]
    if network_type == NetworkType.SD_1_5:
        m = SDPipeline(memory_efficient=memory_efficient)
    else:
        raise ValueError(f"{network_type} not supported")

    m.init(base_model=base_model,
           vae=vae,
           clip_skip=clip_skip,
           lora_adapters=lora_adapters,
           embedding_adapters=embedding_adapters)

    enhance_method, enhance_type = enhance_factory(
        {"method": upscaler_method, "model_id": upscaler_method},
        {"method": restorer_method, "model_id": restorer_method},
    )
    res = m.image2image(image=image,
                        prompt=prompt,
                        neg_prompt=neg_prompt,
                        sampling_steps=sampling_steps,
                        guidance_scale=cfg,
                        clip_skip=clip_skip,
                        strength=strength,
                        seed=seed,
                        image_num=image_num,
                        # ---
                        enhance_type=enhance_type,
                        enhance_method=enhance_method,
                        enhance_scale=enhance_scale,
                        enhance_strength=enhance_strength,
                        # ---
                        lora_specs=lora_specs,
                        scheduler=scheduler)

    flush_gpu()
    return res


@dataclass
class LoadLoraUI(UI):
    hub: CachedModelHub = None

    def _build(self):
        with gr.Accordion("lora setting", visible=self.visible) as more:
            self.gallery = gr.Gallery(
                label="thumbnails",
                value=self.hub.thumbnails,
                object_fit="cover",
                min_width=400,
                height=350,
                columns=8,
                show_download_button=False)
            self.chosen = gr.Highlight(label="chosen", interactive=True)

        self.more = more

    def run(self):
        def select(evt: gr.SelectData, chosen):
            name = evt.value[1]
            if not chosen:
                chosen = []

            chosen_dict = {k: v for k, v in chosen}
            chosen_dict[name] = chosen_dict.get(name, "1.0")
            chosen = [[k, v] for k, v in chosen_dict.items()]
            return chosen

        def change(chosen):
            if not chosen:
                return
            res = []
            for k, v in chosen:
                try:
                    if not v:
                        continue
                    vv = float(v)
                    if vv == 0:
                        continue
                except ValueError:
                    gr.Warning("weight must be a number")
                    continue
                res.append([k, v])

            return res

        self.gallery.select(select, [self.chosen], [self.chosen])
        self.chosen.change(change, [self.chosen], [self.chosen])


def separate_adapters(lora_specs: list[tuple[str, str | float]], separates: list[str]) -> tuple[
    list[tuple[str, float]], list[tuple[str, float]]]:
    fuse, no_fuse = [], []
    for model_id, weight in lora_specs:
        if model_id.endswith(UNAVAILABLE_SUFFIX):
            continue
        if model_id in separates:
            fuse.append((model_id, float(weight)))
        else:
            no_fuse.append((model_id, float(weight)))
    return fuse, no_fuse


@dataclass
class LoadEmbeddingUI(UI):
    hub: CachedModelHub = None

    def _build(self):
        with gr.Accordion("embedding setting", visible=self.visible) as more:
            self.gallery = gr.Gallery(
                label="thumbnails",
                value=self.hub.thumbnails,
                object_fit="cover",
                min_width=400,
                height=320,
                columns=8,
                show_download_button=False)
            self.chosen = gr.Highlight(label="chosen", interactive=True)

        self.more = more

    def run(self):
        def select(evt: gr.SelectData, chosen):
            name = evt.value[1]
            if not chosen:
                chosen = []

            chosen_dict = {k: None for k, _ in chosen}
            chosen_dict[name] = chosen_dict.get(name, None)
            chosen = [[k, 1] for k, _ in chosen_dict.items()]
            return chosen

        def change(chosen):
            if not chosen:
                return
            res = []
            for k, v in chosen:
                try:
                    if v is None:
                        continue
                    vv = float(v)
                    if vv == 0:
                        continue
                except ValueError:
                    gr.Warning("weight must be a number")
                    continue
                res.append([k, 1])

            return res

        self.gallery.select(select, [self.chosen], [self.chosen])
        self.chosen.change(change, [self.chosen], [self.chosen])


@dataclass
class LoadModelUI(UI):
    network_type: NetworkType = None
    hubs: dict[tuple[NetworkType, ModelType], CachedModelHub] = None

    def _build(self):
        checkpoints = self.hubs.get((self.network_type, ModelType.Checkpoint)).model_ids
        default_checkpoint = checkpoints[0] if len(checkpoints) > 0 else None
        vaes = ["Auto"] + self.hubs.get((self.network_type, ModelType.Vae)).model_ids

        with gr.Group():
            with gr.Row():
                self.base_model = gr.Dropdown(choices=checkpoints, label="base model", value=default_checkpoint)
                self.vae = gr.Dropdown(choices=vaes, label="vae", value=vaes[0])
            with gr.Accordion("additional networks", open=False):
                with gr.Row():
                    self.enable_lora = gr.Checkbox(value=False, label="enable lora")
                    self.enable_embedding = gr.Checkbox(value=False, label="enable embedding")

    def run(self, load_lora, load_embedding):
        self.enable_lora.change(lambda enable: gr.update(visible=enable),
                                [self.enable_lora],
                                [load_lora.more])
        self.enable_embedding.change(lambda enable: gr.update(visible=enable),
                                     [self.enable_embedding],
                                     [load_embedding.more])


@dataclass
class ExtraNetworksUI(UI):
    network_type: NetworkType = None
    hubs: dict[tuple[NetworkType, ModelType], CachedModelHub] = None

    def _build(self):
        lora_hub = self.hubs.get((self.network_type, ModelType.Lora))
        embedding_hub = self.hubs.get((self.network_type, ModelType.Embedding))
        self.load_lora = LoadLoraUI(visible=False, hub=lora_hub).build()
        self.load_embedding = LoadEmbeddingUI(visible=False, hub=embedding_hub).build()

    def run(self):
        self.load_lora.run()
        self.load_embedding.run()


@dataclass
class InferenceUI(UI):
    network_type: NetworkType = None
    hubs: dict[tuple[NetworkType, ModelType], CachedModelHub] = None

    def _build(self):
        with gr.Group():
            with gr.Row():
                with gr.Column():
                    line = 5
                    self.prompt = gr.Textbox(label="prompt",
                                             placeholder="inputs prompt",
                                             lines=line, max_lines=line)
                    self.neg_prompt = gr.Text(label="neg prompt",
                                              placeholder="inputs negative prompt",
                                              lines=line, max_lines=line)
                self.image_copy = gr.Image(type="pil", visible=False)
                self.image = gr.Image(label="input image", height=337, type="pil")
            with gr.Row():
                self.strength = gr.Slider(0, 1, 0.2, step=0.01, label="strength")
                self.scale = gr.Slider(0.1, 2, 1, step=0.1, label="scale image")
            with gr.Row():
                schedule_list = SCHEDULER_LIST[self.network_type]
                self.scheduler = gr.Dropdown(choices=schedule_list, label="scheduler", value=schedule_list[0])
                self.sampling_steps = gr.Slider(1, 60, 25, step=1, label="sampling steps")
                self.width = gr.Slider(64, 2048, 480, step=8, label="width")
                self.height = gr.Slider(64, 2048, 640, step=8, label="height")

            with gr.Row():
                self.cfg = gr.Slider(0, 20, 7, step=0.1, label="CFG scale")
                self.clip_skip = gr.Slider(0, 12, 0, step=1, label="clip skip")

                self.image_num = gr.Number(1, precision=0, label="image num")
                self.seed = gr.Number(-1, precision=0, label="random seed")

            with gr.Accordion("high res fix", open=False):
                with gr.Row():
                    self.upscaler = gr.Dropdown(label="upscaler", choices=UPSCALER_LIST, value=UPSCALER_LIST[0])
                    self.restorer = gr.Dropdown(label="restorer", choices=RESTORER_LIST, value=RESTORER_LIST[0])
                    self.fix_scale = gr.Slider(1, 2, 1, step=0.1, label="scale")
                    self.fix_strength = gr.Slider(0, 1, 0.0, step=0.01, label="strength")

        self.inference = gr.Button("Inference", variant="primary")
        self.gallery = gr.Gallery(label="output", columns=4, object_fit="contain", height=600, show_share_button=True)
        # todo: all args, system info

    def run(self, network_type, base_model, vae, load_lora, load_embedding):
        model_args = [
            network_type,
            base_model,
            vae,
            load_lora.chosen,
            load_embedding.chosen
        ]
        inference_args = [
            self.image,
            self.prompt,
            self.neg_prompt,
            self.scheduler,
            self.sampling_steps,
            self.cfg,
            self.clip_skip,
            self.strength,
            self.seed,
            self.image_num,
        ]
        upscale_args = [
            self.upscaler,
            self.restorer,
            self.fix_scale,
            self.fix_strength
        ]

        inputs = model_args + inference_args + upscale_args
        self.inference.click(image2image, inputs, [self.gallery])

        def get_image_size(img):
            w, h = 0, 0
            if img is not None:
                w, h = img.size
            return gr.update(value=w), gr.update(value=h)

        def scale(img, img_copy, scale):
            input_img = img_copy if img_copy is not None else img
            return resize(input_img, scale), input_img

        self.scale.change(scale, [self.image, self.image_copy, self.scale], [self.image, self.image_copy])
        self.image.change(get_image_size, [self.image], [self.width, self.height])


@dataclass
class _Image2ImageUI(UI):
    network_type: NetworkType = None
    hubs: dict[tuple[NetworkType, ModelType], CachedModelHub] = None

    def _build(self):
        self.load_model = LoadModelUI(hubs=self.hubs, network_type=self.network_type).build()
        self.extra_networks = ExtraNetworksUI(hubs=self.hubs,
                                              network_type=self.network_type).build()
        gr.Markdown("## Inference")
        self.inference = InferenceUI(hubs=self.hubs, network_type=self.network_type).build()

    def run(self, network_type):
        self.load_model.run(self.extra_networks.load_lora, self.extra_networks.load_embedding)
        self.extra_networks.run()
        self.inference.run(network_type, self.load_model.base_model, self.load_model.vae,
                           self.extra_networks.load_lora, self.extra_networks.load_embedding)


@dataclass
class Image2ImageUI(UI):
    config: dict[NetworkType, list[ModelType]] = None
    hubs: dict[tuple[NetworkType, ModelType], CachedModelHub] = None

    def _build(self):
        network_types = list(self.config.keys())
        self.network_type = gr.Dropdown(choices=network_types,
                                        value=network_types[0],
                                        interactive=True,
                                        label="network type")
        blocks = [_Image2ImageUI(hubs=self.hubs, network_type=NetworkType.SD_1_5),
                  _Image2ImageUI(hubs=self.hubs, network_type=NetworkType.SDXL_1_0)]
        gr.Markdown("## Load Model")
        self.page = OneHotLayoutUI(blocks=blocks, dropdown=self.network_type).build()

    def run(self):
        self.page.run(self.network_type)
