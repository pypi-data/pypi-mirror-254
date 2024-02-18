import os
import threading
import gradio as gr
from artcraft.hub import (
    ModelType,
    NetworkType,
    CachedModelHub
)

CACHED_CONFIG: dict[NetworkType, list[ModelType]] = {
    NetworkType.SD_1_5.value:
        [ModelType.Lora, ModelType.Vae, ModelType.Embedding, ModelType.Checkpoint],
    NetworkType.SDXL_1_0.value:
        [ModelType.Lora, ModelType.Vae, ModelType.Embedding, ModelType.Checkpoint],
    NetworkType.Other.value:
        [ModelType.UpScaler, ModelType.Adapter]
}

RELOAD_EVENT = threading.Event()
RELOAD_DONE_EVENT = threading.Event()


def reload_notify():
    RELOAD_EVENT.set()
    RELOAD_DONE_EVENT.wait()
    RELOAD_DONE_EVENT.clear()


def prepare(block, watch_file):
    block.dev_mode = True
    block.set_reload(RELOAD_EVENT, RELOAD_DONE_EVENT, os.path.basename(watch_file).split(".")[0])


def init_hubs(config: dict[NetworkType, list[ModelType]]):
    hubs = {}

    for base_model, types in config.items():
        for model_type in types:
            cached = CachedModelHub(base_model, model_type)
            cached.update()
            hubs[(base_model, model_type)] = cached

    return hubs
