import torch
from collections import defaultdict

from ..pipeline import flush_gpu
from .scheme import PipelineResource, UpscalerResource, Scheme


class ResourceCacheNotFound(Exception):
    def __init__(self, message):
        self.message = message


class ResourceCacheNotLoaded(Exception):
    def __init__(self):
        super(ResourceCacheNotLoaded, self).__init__()


class ResourceCache:
    schemes = {}
    pipelines = defaultdict(PipelineResource)
    upscalers = defaultdict(UpscalerResource)

    @classmethod
    def get_pipeline(cls, scheme: Scheme):
        name = PipelineResource.resource_id(scheme)
        if name not in cls.pipelines:
            raise ResourceCacheNotFound(name)
        r = cls.pipelines.get(name)
        return r

    @classmethod
    def get_upscaler(cls, scheme: Scheme):
        name = UpscalerResource.resource_id(scheme)
        if name not in cls.upscalers:
            raise ResourceCacheNotFound(name)
        r = cls.upscalers.get(name)
        return r

    @classmethod
    def load(cls):
        cls._load_pipeline()
        cls._load_upscaler()

    @classmethod
    def add_schemes(cls, *schemes):
        for scheme in schemes:
            cls._add_pipeline(scheme)
            cls._add_upscaler(scheme)
            cls.schemes[scheme.name] = scheme

    @classmethod
    def clear(cls):
        cls.pipelines = defaultdict(PipelineResource)
        cls.upscalers = defaultdict(UpscalerResource)
        cls.schemes = {}
        flush_gpu()
        print(f">> clear:{torch.cuda.memory_reserved() / 1024 / 1024} M")

    @classmethod
    def _load_pipeline(cls):
        for name, r in cls.pipelines.items():
            print("-" * 50)
            print(f"Load Pipeline: {name}")

            base_model, vae, clip_skip, adapt_model = name
            r.load(base_model, vae, clip_skip, adapt_model)
            print("-" * 50)

    @classmethod
    def _load_upscaler(cls):
        for name, r in cls.upscalers.items():
            print("-" * 50)
            print(f"Load Upscaler: {name}")

            upscaler_method, restorer_method = name
            r.load(upscaler_method, restorer_method)
            print("-" * 50)

    @classmethod
    def _add_pipeline(cls, scheme: Scheme):
        try:
            uniq_id = PipelineResource.resource_id(scheme)

            _ = cls.pipelines[uniq_id]
            for lora, weight in scheme.lora_specs:
                if weight > 0:
                    cls.pipelines[uniq_id].loras.add(lora)
            for embedding in scheme.embedding_specs:
                cls.pipelines[uniq_id].embeddings.add(embedding)
            print("**************")
            print(scheme.lora_specs)
            print(scheme.embedding_specs)
            print(cls.pipelines[uniq_id].loras)
            print(cls.pipelines[uniq_id].embeddings)
            print("**************")
        except Exception as e:
            raise ValueError(e)

    @classmethod
    def _add_upscaler(cls, scheme: Scheme):
        uniq_id = UpscalerResource.resource_id(scheme)
        _ = cls.upscalers[uniq_id]


def load(*schemes):
    ResourceCache.add_schemes(*schemes)
    ResourceCache.load()
    print(f">> load done:{torch.cuda.memory_reserved() / 1024 / 1024} M")
