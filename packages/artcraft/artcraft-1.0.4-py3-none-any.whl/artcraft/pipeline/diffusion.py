import gc
import torch
from PIL import Image
from typing import Callable

from ..hub import ModelType, NetworkType, ModelHub, UNAVAILABLE_SUFFIX, must_exists

LCM_SCHEDULER_LIST = {
    NetworkType.SD_1_5: [must_exists("LCM", NetworkType.SD_1_5, ModelType.Lora)],
    NetworkType.SDXL_1_0: [must_exists("LCM", NetworkType.SDXL_1_0, ModelType.Lora)]
}
SD15_SCHEDULERS = ['Auto', 'Euler', 'Euler a', 'DDIM', 'UniPC', 'DPM++ SDE Karras', 'DPM++ 2M Karras',
                   'DPM++ 2M SDE', 'DPM++ 2M SDE Karras'] + LCM_SCHEDULER_LIST[NetworkType.SD_1_5]
SDXL10_SCHEDULERS = ['Auto'] + LCM_SCHEDULER_LIST[NetworkType.SDXL_1_0]

SCHEDULER_LIST = {
    NetworkType.SD_1_5: SD15_SCHEDULERS,
    NetworkType.SDXL_1_0: SDXL10_SCHEDULERS,
}


class BasePipeline:
    def __init__(self, network_type: NetworkType, memory_efficient=False):
        self.network_type = network_type
        self.memory_efficient = memory_efficient
        self.pipe = None

    def init_lora(self, fuse: list[str], no_fuse: list[str]):
        hub = ModelHub(self.network_type, ModelType.Lora)
        print(f">> before init:{torch.cuda.memory_reserved() / 1024 / 1024} M")

        for model_id in fuse:
            self.pipe.load_lora_weights(hub.extract_model_path(model_id), adapter_name=model_id)
            print(f">> load lora: <{model_id}>")
        self.pipe.fuse_lora()
        torch.cuda.empty_cache()
        print(f">> after fuse:{torch.cuda.memory_reserved() / 1024 / 1024} M")

        for model_id in no_fuse:
            lora_path = hub.extract_model_path(model_id)
            self.pipe.load_lora_weights(lora_path, adapter_name=model_id)
            print(f">> load lora: <{model_id}>")
            torch.cuda.empty_cache()
            print(f">> after no_fuse:{torch.cuda.memory_reserved() / 1024 / 1024} M")

        if self.memory_efficient:
            self.pipe.set_lora_device(no_fuse, "cpu")
            torch.cuda.empty_cache()
            print(f">> move <{no_fuse}> to cpu")
            print(f">> after save:{torch.cuda.memory_reserved() / 1024 / 1024} M")

    def set_lora(self, lora_specs: list[tuple[str, float]] | None):
        if not lora_specs:
            lora_specs = []

        names = [s[0] for s in lora_specs]
        weights = [float(s[1]) for s in lora_specs]

        if self.memory_efficient:
            self.pipe.set_lora_device(names, "cuda")
            torch.cuda.empty_cache()
            print(f">> after set:{torch.cuda.memory_reserved() / 1024 / 1024} M")
        self.pipe.set_adapters(adapter_names=names, adapter_weights=weights)

    def unset_lora(self, lora_specs: list[tuple[str, float]] | None):
        if not lora_specs:
            return

        if self.memory_efficient:
            names = [s[0] for s in lora_specs]
            self.pipe.set_lora_device(names, "cpu")
            torch.cuda.empty_cache()
            print(f">> move {names} to cpu")
            print(f">> after unset:{torch.cuda.memory_reserved() / 1024 / 1024} M")

    def set_vae(self, vae):
        if vae is None or vae == "Auto":
            return
        hub = ModelHub(NetworkType.SD_1_5, ModelType.Vae)
        if not hub.contains(vae):
            raise FileNotFoundError(f"vae:{vae} not found")
        vae_path = hub.get_or_create_model_dir(vae)
        from diffusers import AutoencoderKL
        self.pipe.vae = AutoencoderKL.from_pretrained(vae_path, torch_dtype=torch.float16)

        # todo: unload embedding https://github.com/huggingface/diffusers/issues/6013

    def init_textual_inversion(self, embedding_tags: list[str] | None):
        if not len(embedding_tags):
            return
        embedding_tags = list(set(embedding_tags))
        paths, tokens = [], []
        hub = ModelHub(self.network_type, ModelType.Embedding)
        for name in embedding_tags:
            embedding_path = hub.extract_model_path(name)
            paths.append(embedding_path)
            words = hub.extract_meta(name).trained_word
            if len(words) == 0:
                raise ValueError(f"{name} lacks trained word")
            tokens.append(words[0])
        self.pipe.load_textual_inversion(pretrained_model_name_or_path=paths, token=tokens)

        # todo: see  StableDiffusionPipeline

    def init_clip_skip(self, model_path, num=0):
        if 0 < num < 12:
            from transformers import CLIPTextModel
            self.pipe.text_encoder = CLIPTextModel.from_pretrained(
                model_path,
                subfolder="text_encoder",
                num_hidden_layers=12 - num,
                torch_dtype=torch.float16)

    def set_scheduler(self, method):
        if method not in SCHEDULER_LIST[self.network_type]:
            raise ValueError(f"invalid scheduler:{method}")
        # see more https://huggingface.co/docs/diffusers/v0.20.0/en/api/schedulers/overview
        pipe = self.pipe
        if method.endswith(UNAVAILABLE_SUFFIX):
            raise FileNotFoundError(method)
        if method == "Euler":
            from diffusers import EulerDiscreteScheduler
            pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config)
        if method == "Euler a":
            from diffusers import EulerAncestralDiscreteScheduler
            pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
        if method == "DDIM":
            from diffusers import DDIMScheduler
            pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)
        if method == "DPM++ 2M Karras":
            from diffusers import DPMSolverMultistepScheduler
            pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config, use_karras_sigmas=True)
        if method == "DPM++ SDE Karras":
            from diffusers import DPMSolverSinglestepScheduler
            pipe.scheduler = DPMSolverSinglestepScheduler(pipe.scheduler.config, use_karras_sigmas=True)
        if method == "DPM++ 2M SDE":
            from diffusers import DPMSolverMultistepScheduler
            pipe.scheduler = DPMSolverMultistepScheduler(pipe.scheduler.config, algorithm_type="sde-dpmsolver++")
        if method == "DPM++ 2M SDE Karras":
            from diffusers import DPMSolverMultistepScheduler
            pipe.scheduler = DPMSolverMultistepScheduler(pipe.scheduler.config, algorithm_type="sde-dpmsolver++",
                                                         use_karras_sigmas=True)
        if method == "UniPC":
            from diffusers import UniPCMultistepScheduler
            pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)
        if method == "LCM":
            from diffusers import LCMScheduler
            pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)

    def _high_res_fix(self,
                      image: torch.Tensor | list[Image],
                      prompt: str = "",
                      neg_prompt: str = "",
                      sampling_steps: int = 30,
                      guidance_scale: float = 7.5,
                      clip_skip=0,  # todo
                      seed=-1,
                      image_num: int = 1,
                      # ---
                      enhance_type: str = "pil",
                      enhance_method: Callable = None,
                      enhance_scale: float = 1.0,
                      enhance_strength: float = 0.0):

        # 1. upscale
        enhanced = image
        if enhance_method is not None and enhance_scale > 1.0:
            if enhance_type == "latent":
                enhanced = enhance_method(image, enhance_scale)
            elif enhance_type == "pil":
                enhanced = [enhance_method(i, enhance_scale) for i in image]
            else:
                raise ValueError(f"invalid enhance type: {enhance_type}")
            torch.cuda.empty_cache()
            print(f">> after upscale:{torch.cuda.memory_reserved() / 1024 / 1024} M")

        # 2. image to image
        if enhance_strength >= 0.05:
            enhanced = self._image2image(image=enhanced,
                                         prompt=prompt,
                                         neg_prompt=neg_prompt,
                                         sampling_steps=sampling_steps,
                                         guidance_scale=guidance_scale,
                                         clip_skip=clip_skip,
                                         seed=seed,
                                         strength=enhance_strength,
                                         image_num=image_num)
            torch.cuda.empty_cache()
            print(f">> after reimage:{torch.cuda.memory_reserved() / 1024 / 1024} M")
        return enhanced

    def _image2image(self,
                     image: torch.Tensor | list[Image],
                     prompt: str = "",
                     neg_prompt: str = "",
                     sampling_steps: int = 30,
                     guidance_scale: float = 7.5,
                     clip_skip=0,  # todo
                     seed=-1,
                     strength=0.1,
                     image_num: int = 1,
                     output_type: str = "pil"):
        generator = torch.Generator(device="cuda").manual_seed(seed)

        if isinstance(image, torch.Tensor):
            return self.pipe.img2img(
                image=image,
                prompt=prompt, negative_prompt=neg_prompt,
                strength=strength,
                guidance_scale=guidance_scale,
                num_inference_steps=sampling_steps,
                generator=generator,
                num_images_per_prompt=image_num,
                output_type=output_type).images

        assert len(image) == image_num
        images = []
        for i in image:
            images.extend(self.pipe.img2img(
                image=i,
                prompt=prompt, negative_prompt=neg_prompt,
                strength=strength,
                guidance_scale=guidance_scale,
                num_inference_steps=sampling_steps,
                generator=generator,
                num_images_per_prompt=1,
                output_type=output_type).images)
        return images

    def _text2image(self,
                    prompt: str = "",
                    neg_prompt: str = "",
                    sampling_steps: int = 30,
                    guidance_scale: float = 7.5,
                    clip_skip=0,  # todo
                    seed=-1,
                    width: int = 480,
                    height: int = 640,
                    image_num: int = 1,
                    output_type: str = "pil"):
        generator = torch.Generator(device="cuda").manual_seed(seed)

        return self.pipe.text2img(
            prompt=prompt, negative_prompt=neg_prompt,
            width=width, height=height,
            guidance_scale=guidance_scale,
            num_inference_steps=sampling_steps,
            generator=generator,
            num_images_per_prompt=image_num,
            output_type=output_type).images


class SDPipeline(BasePipeline):
    def __init__(self, memory_efficient: bool):
        super(SDPipeline, self).__init__(NetworkType.SD_1_5, memory_efficient)

    def init(self,
             base_model: str,
             vae: str,
             clip_skip: int,
             lora_fuse_adapters: list[str] = (),
             lora_adapters: list[str] = (),
             embedding_adapters: list[str] = (),
             **kwargs):
        hub = ModelHub(self.network_type, ModelType.Checkpoint)
        base_model_path = hub.extract_model_path(base_model)

        from artcraft.pipeline.custom import StableDiffusionLongPromptWeightingPipeline
        self.pipe = StableDiffusionLongPromptWeightingPipeline.from_pretrained(
            base_model_path,
            torch_dtype=torch.float16,
            local_files_only=True,
            safety_checker=None,
            feature_extractor=None,
            requires_safety_checker=False)

        self.init_clip_skip(base_model_path, clip_skip)
        self.init_textual_inversion(embedding_adapters)
        self.set_vae(vae)
        self.pipe.to("cuda")
        self.init_lora(lora_fuse_adapters, lora_adapters)

    def text2image(self,
                   prompt: str = "",
                   neg_prompt: str = "",
                   sampling_steps: int = 30,
                   guidance_scale: float = 7.5,
                   clip_skip=0,  # todo
                   seed=-1,
                   width: int = 480,
                   height: int = 640,
                   image_num: int = 1,
                   # -----------
                   enhance_type: str = "pil",
                   enhance_method: Callable = None,
                   enhance_scale: float = 1.0,
                   enhance_strength: float = 0.0,
                   # -----------
                   scheduler: str = "auto",
                   lora_specs: list[tuple[str, float]] = ()):
        self.set_scheduler(scheduler)
        self.set_lora(lora_specs)
        images = self._text2image(prompt, neg_prompt, sampling_steps, guidance_scale, clip_skip,
                                  seed, width, height, image_num, enhance_type)
        torch.cuda.empty_cache()
        print(f">> after text2img:{torch.cuda.memory_reserved() / 1024 / 1024} M")

        images = self._high_res_fix(images, prompt, neg_prompt, sampling_steps, guidance_scale, clip_skip,
                                    seed, image_num, enhance_type, enhance_method, enhance_scale, enhance_strength)
        torch.cuda.empty_cache()
        print(f">> after high_res_fix:{torch.cuda.memory_reserved() / 1024 / 1024} M")
        self.unset_lora(lora_specs)
        return images

    def image2image(self,
                    image: Image,
                    prompt: str = "",
                    neg_prompt: str = "",
                    sampling_steps: int = 30,
                    guidance_scale: float = 7.5,
                    clip_skip=0,  # todo
                    strength=0.1,
                    seed=-1,
                    image_num: int = 1,
                    # -----------
                    enhance_type: str = "pil",
                    enhance_method: Callable = None,
                    enhance_scale: float = 1.0,
                    enhance_strength: float = 0.0,
                    # -----------
                    scheduler: str = "auto",
                    lora_specs: list[tuple[str, str | float]] = ()):
        self.set_scheduler(scheduler)
        self.set_lora(lora_specs)
        images = self._image2image([image], prompt, neg_prompt, sampling_steps, guidance_scale, clip_skip,
                                   seed, strength, image_num, output_type=enhance_type)
        images = self._high_res_fix(images, prompt, neg_prompt, sampling_steps, guidance_scale, clip_skip,
                                    seed, image_num, enhance_type, enhance_method, enhance_scale, enhance_strength)
        self.unset_lora(lora_specs)
        return images


def flush_gpu():
    gc.collect()
    torch.cuda.empty_cache()
