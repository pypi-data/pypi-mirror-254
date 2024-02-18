import os
import torch
from typing import Callable
from ..hub import ModelHub, NetworkType, ModelType, must_exists
from .diffusion import BasePipeline

ADAPTER_LIST = [
    "None",
    must_exists("ip_adapter_full_face_sd15", NetworkType.Other, ModelType.Adapter),
    must_exists("ip_adapter_plus_face_sd15", NetworkType.Other, ModelType.Adapter),
    must_exists("ip_adapter_faceid_sd15", NetworkType.Other, ModelType.Adapter),
    must_exists("ip_adapter_faceid_plus_sd15", NetworkType.Other, ModelType.Adapter),
    must_exists("ip_adapter_faceid_plusv2_sd15", NetworkType.Other, ModelType.Adapter),
]


def image_adapter_factory(pipe, adapt_model):
    hub = ModelHub(NetworkType.Other, ModelType.Adapter)
    model_dir = hub.extract_model_path(adapt_model)
    image_encoder = os.path.join(model_dir, "image_encoder")

    if adapt_model == "ip_adapter_full_face_sd15":
        ckpt_path = os.path.join(model_dir, "ip-adapter-full-face_sd15.bin")
        from .ip_adapter.ip_adapter import IPAdapterFull
        return IPAdapterFull(pipe,
                             image_encoder_path=image_encoder,
                             ip_ckpt=ckpt_path, device="cuda", num_tokens=257)

    elif adapt_model == "ip_adapter_plus_face_sd15":
        ckpt_path = os.path.join(model_dir, "ip-adapter-plus-face_sd15.bin")
        from .ip_adapter.ip_adapter import IPAdapterPlus
        return IPAdapterPlus(pipe,
                             image_encoder_path=image_encoder,
                             ip_ckpt=ckpt_path,
                             device="cuda",
                             num_tokens=16)

    elif adapt_model == "ip_adapter_faceid_sd15":
        ckpt_path = os.path.join(model_dir, "ip-adapter-faceid_sd15.bin")
        from .ip_adapter.ip_adapter_faceid import IPAdapterFaceID
        return IPAdapterFaceID(pipe, ckpt_path, device="cuda")

    elif adapt_model == "ip_adapter_faceid_plus_sd15":
        ckpt_path = os.path.join(model_dir, "ip-adapter-faceid-plus_sd15.bin")
        from .ip_adapter.ip_adapter_faceid import IPAdapterFaceIDPlus
        return IPAdapterFaceIDPlus(pipe,
                                   image_encoder_path=image_encoder,
                                   ip_ckpt=ckpt_path,
                                   device="cuda")

    elif adapt_model == "ip_adapter_faceid_plusv2_sd15":
        ckpt_path = os.path.join(model_dir, "ip-adapter-faceid-plusv2_sd15.bin")
        from .ip_adapter.ip_adapter_faceid import IPAdapterFaceIDPlus
        return IPAdapterFaceIDPlus(pipe,
                                   image_encoder_path=image_encoder,
                                   ip_ckpt=ckpt_path,
                                   device="cuda")
    else:
        raise ValueError(f"adapt model {adapt_model} not found")


class IPAdapterPipeline(BasePipeline):
    def __init__(self, memory_efficient=True):
        super(IPAdapterPipeline, self).__init__(NetworkType.SD_1_5, memory_efficient)

    def init(self,
             base_model: str,
             vae: str,
             clip_skip: int,
             adapt_model: str,
             lora_fuse_adapters: list[str] = (),
             lora_adapters: list[str] = (),
             embedding_adapters: list[str] = (),
             **kwargs):
        hub = ModelHub(self.network_type, ModelType.Checkpoint)
        base_model_path = hub.extract_model_path(base_model)

        from diffusers import StableDiffusionPipeline

        self.pipe = StableDiffusionPipeline.from_pretrained(
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
        self.model = image_adapter_factory(self.pipe, adapt_model)

    def text2image(self,
                   reference_image,
                   adapt_scale: float = 0.5,
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
                   scheduler: str = "Auto",
                   lora_specs: list[tuple[str, float]] = ()):
        self.set_scheduler(scheduler)
        self.set_lora(lora_specs)
        images = self.model.generate(
            pil_image=reference_image,
            prompt=prompt,
            negative_prompt=neg_prompt,
            guidance_scale=guidance_scale,
            seed=seed,
            width=width, height=height,
            num_inference_steps=sampling_steps,
            num_samples=image_num,
            scale=adapt_scale)
        torch.cuda.empty_cache()
        print(f">> after adapt:{torch.cuda.memory_reserved() / 1024 / 1024} M")

        images = self._high_res_fix(images, prompt, neg_prompt, sampling_steps, guidance_scale, clip_skip,
                                    seed, image_num, enhance_type, enhance_method, enhance_scale, enhance_strength)
        torch.cuda.empty_cache()
        self.unset_lora(lora_specs)
        return images
