import os
import cv2
import torch
import torch.nn as nn
import dataclasses
import numpy as np
from PIL import Image
from realesrgan import RealESRGANer
from basicsr.archs.rrdbnet_arch import RRDBNet

from ..hub import ModelHub, NetworkType, ModelType, must_exists

INTERPOLATION_MAPPING = {
    "Lanczos": Image.Resampling.LANCZOS,
    "Nearest": Image.Resampling.NEAREST,
    "Bilinear": Image.Resampling.BILINEAR,
    "Bicubic": Image.Resampling.BICUBIC,
}

LATENT_INTERPOLATION_MAPPING = {
    "Latent_Nearest": "nearest",
    "Latent_Bilinear": "bilinear",
    "Latent_Bicubic": "bicubic",
}

UPSCALER_LIST = ["None",
                 must_exists("RealESRGAN_x4plus", NetworkType.Other, ModelType.UpScaler),
                 must_exists("RealESRGAN_x4plus_anime_6B", NetworkType.Other, ModelType.UpScaler),
                 "Latent_Nearest", "Latent_Bilinear", "Latent_Bicubic",
                 "Lanczos", "Nearest", "Bilinear", "Bicubic"]
RESTORER_LIST = ["None",
                 must_exists("gfpgan/v1_3", NetworkType.Other, ModelType.UpScaler)]


def enhance_factory(upscaler_params, restorer_params):
    upscaler = upscaler_factory(**upscaler_params)
    restorer = restorer_factory(**restorer_params)

    enhance_method, enhance_type = None, "pil"
    if restorer is not None and upscaler is not None:
        restorer.bg_upsampler = upscaler
        if isinstance(upscaler, LatentInterpolation):
            raise ValueError("latent upscaler incompatible with restorer")
        enhance_method = restorer.enhance
    elif upscaler is not None:
        enhance_method = upscaler.enhance
        if isinstance(upscaler, LatentInterpolation):
            enhance_type = "latent"
    elif restorer is not None:
        enhance_method = restorer.enhance
    return enhance_method, enhance_type


def upscaler_factory(method: str, **kwargs):
    assert method in UPSCALER_LIST
    match method:
        case "RealESRGAN_x4plus" | "RealESRGAN_x4plus_anime_6B":
            model_id = kwargs["model_id"]
            return RealESRUpscaler.from_local(model_id)
        case "Lanczos" | "Nearest" | "Bilinear" | "Bicubic":
            return Interpolation(method)
        case "Latent_Nearest" | "Latent_Bilinear" | "Latent_Bicubic":
            return LatentInterpolation(method)
        case "None":
            return None
        case _:
            raise ValueError(f"upscaler:{method} not found")


def restorer_factory(method: str, **kwargs):
    assert method in RESTORER_LIST
    match method:
        case "gfpgan/v1_3":
            model_id = kwargs["model_id"]
            return GFPGANRestorer.from_local(model_id)
        case "None":
            return None
        case _:
            raise ValueError(f"restorer:{method} not found")


@dataclasses.dataclass
class Interpolation:
    method: str

    def enhance(self, img: Image, outscale: float) -> Image:
        return resize(img, outscale, INTERPOLATION_MAPPING.get(self.method, None))


@dataclasses.dataclass
class LatentInterpolation:
    method: str

    def enhance(self, latent: torch.Tensor, outscale: float):
        upsampler = nn.Upsample(scale_factor=outscale, mode=LATENT_INTERPOLATION_MAPPING.get(self.method))
        latents = upsampler(latent)
        return latents


@dataclasses.dataclass
class LatentDiffusion:
    def enhance(self, img: Image, outscale: float) -> Image:
        raise NotImplementedError


class RealESRUpscaler:
    def __init__(self, model_path: str):
        weight_file = os.path.basename(model_path)
        if weight_file == "RealESRGAN_x4plus.pth":
            m = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
        elif weight_file == "RealESRGAN_x4plus_anime_6B.pth":
            m = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=6, num_grow_ch=32, scale=4)
        else:
            raise ValueError(f"unknown RealESRGANer:{weight_file}")
        self.upscaler = RealESRGANer(scale=4,
                                     model_path=model_path,
                                     dni_weight=None,
                                     model=m,
                                     tile=0,
                                     tile_pad=10,
                                     pre_pad=0,
                                     half=False,
                                     gpu_id=None)

    @classmethod
    def from_local(cls, model_id):
        hub = ModelHub(network_type=NetworkType.Other, model_type=ModelType.UpScaler)
        return cls(hub.extract_model_path(model_id))

    def enhance(self, img: Image, outscale: float) -> Image:
        cv_img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
        output, _ = self.upscaler.enhance(cv_img, outscale=outscale)
        out = Image.fromarray(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
        res = resize(out, outscale, size= img.size)
        print("[realesr]", img.size, res.size)
        return res


class GFPGANRestorer:
    bg_upsampler = None

    def __init__(self, model_dir: str):
        from artcraft.pipeline.my_gfpgan.utils import MyGFPGANer

        self.restorer = MyGFPGANer(model_dir=model_dir,
                                   weight_file="GFPGANv1.3.pth",
                                   upscale=2,
                                   arch='clean',
                                   channel_multiplier=2,
                                   bg_upsampler=self.bg_upsampler)

    @classmethod
    def from_local(cls, model_id):
        hub = ModelHub(network_type=NetworkType.Other, model_type=ModelType.UpScaler)
        return cls(hub.extract_model_path(model_id))

    def enhance(self, img: Image, outscale: float):
        sz = img.size
        img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
        _, _, output = self.restorer.enhance(img, has_aligned=False, only_center_face=False, paste_back=True)
        out = Image.fromarray(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
        res = resize(out, outscale, size=sz)
        return res


def resize(img: Image, outscale: float, method=Image.Resampling.LANCZOS, size: (int, int) = None) -> Image:
    if img is None:
        return None
    if size is None:
        w, h = img.size
    else:
        w, h = size[0], size[1]
    ww, hh = int(w * outscale / 8) * 8, int(h * outscale / 8) * 8
    return img.resize((ww, hh), method)
