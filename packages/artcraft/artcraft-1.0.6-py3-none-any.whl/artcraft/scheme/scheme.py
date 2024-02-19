import dataclasses
from typing import Callable
from pydantic import BaseModel
from ..pipeline import SDPipeline, IPAdapterPipeline, enhance_factory


class Scheme(BaseModel):
    name: str
    tags: list[tuple[str, float]]

    # model
    network_type: str
    base_model: str
    vae: str = "Auto"
    clip_skip: int = 0
    adapt_model: str = "None"
    lora_specs: list[tuple[str, float]] = []
    embedding_specs: list[str] = []
    # restore
    upscaler_method: str = "None"
    restorer_method: str = "None"
    enhance_scale: float = 1.6
    enhance_strength: float = 0.15
    # run args
    prompt_template: str = ""
    neg_prompt_template: str = ""
    cfg: float = 7.0
    scheduler: str = "Auto"
    sampling_steps: int = 35
    # adapt
    adapt_scale: float = 0.5


@dataclasses.dataclass
class PipelineResource:
    loras: set[str] = dataclasses.field(default_factory=set)
    embeddings: set[str] = dataclasses.field(default_factory=set)
    pipeline: SDPipeline | IPAdapterPipeline = None

    @classmethod
    def resource_id(cls, scheme: Scheme):
        return scheme.base_model, scheme.vae, scheme.clip_skip, scheme.adapt_model

    def load(self, base_model, vae, clip_skip, adapt_model):
        if adapt_model == "None":
            p = SDPipeline(memory_efficient=True)
            p.init(base_model, vae, clip_skip,
                   lora_adapters=list(self.loras),
                   embedding_adapters=list(self.embeddings))
            self.pipeline = p
        else:
            p = IPAdapterPipeline(memory_efficient=True)
            p.init(base_model, vae, clip_skip,
                   adapt_model=adapt_model,
                   lora_adapters=list(self.loras),
                   embedding_adapters=list(self.embeddings))
            self.pipeline = p


@dataclasses.dataclass
class UpscalerResource:
    enhance_method: Callable = None
    enhance_type: str = "pil"

    @classmethod
    def resource_id(cls, scheme: Scheme):
        return scheme.upscaler_method, scheme.restorer_method

    def load(self, upscaler_method, restorer_method):
        enhance_method, enhance_type = enhance_factory(
            {"method": upscaler_method, "model_id": upscaler_method},
            {"method": restorer_method, "model_id": restorer_method})
        self.enhance_method, self.enhance_type = enhance_method, enhance_type
