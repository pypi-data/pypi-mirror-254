import gradio as gr
from dataclasses import dataclass

from .globals import reload_notify
from .util import (
    UI,
    MultiColumnsLayoutUI,
    CombinedTabsLayoutUI,
    OneHotLayoutUI,
    Arg
)
from artcraft.hub import (
    FileResource,
    URLResource,
    CivitaiResource,
    FakeResource,
    ModelType,
    NetworkType,
    ModelHub,
    CachedModelHub,
    ModelMeta
)

PROXY = None


@dataclass
class FakeResourceUI(UI):
    name: str = "Fake"
    hub: ModelHub = None

    def _build(self):
        with gr.Group(visible=self.visible):
            self.btn = gr.Button("Upload", variant="primary")

    def run(self, gallery):
        self.btn.click(self.get_resource, None, None)

    def get_resource(self, pr=gr.Progress(track_tqdm=True)):
        FakeResource(self.hub).retrieve()


@dataclass
class FileResourceUI(UI):
    name: str = "File"
    hub: ModelHub = None

    def _build(self):
        with gr.Group(visible=self.visible):
            self.model_id = gr.Text(label="model_id")
            with gr.Row():
                self.file = gr.File(label="file", file_types=["image", ".safetensors", ".zip"])
                self.thumbnail_file = gr.Image(label="thumbnail", type="filepath")
            with gr.Accordion("more", open=False):
                self.force = gr.Checkbox(label="force")
        self.btn = gr.Button("Upload", variant="primary")

    def run(self, gallery):
        self.btn.click(fn=self.get_resource,
                       inputs=[self.model_id, self.file, self.thumbnail_file, self.force],
                       outputs=[gallery]). \
            success(reload_notify, None, None). \
            success(None, _js="window.location.reload()")

    def get_resource(self, model_id, file, thumbnail_file, force, pr=gr.Progress(track_tqdm=True)):
        file = file.name if file is not None else file
        FileResource(self.hub).retrieve(model_id=model_id,
                                        file=file,
                                        thumbnail=thumbnail_file,
                                        force=force)
        gr.Info(f"🍺 Add {model_id} ok, page will be reload")
        return gr.update()


@dataclass
class URLResourceUI(UI):
    name: str = "URL"
    hub: ModelHub = None

    def _build(self):
        with gr.Group(visible=self.visible):
            self.model_id = gr.Text(label="model_id")
            self.url = gr.Text(label="url")
            with gr.Accordion("more", open=False):
                self.force = gr.Checkbox(label="force")
                self.remote_name = gr.Text(label="remote_name")
                self.thumbnail_url = gr.Text(label="thumbnail_url")
        self.btn = gr.Button("Download", variant="primary")

    def run(self, gallery):
        self.btn.click(fn=self.get_resource,
                       inputs=[self.model_id, self.url, self.remote_name, self.thumbnail_url, self.force],
                       outputs=[gallery]). \
            success(reload_notify, None, None). \
            success(None, _js="window.location.reload()")

    def get_resource(self, model_id, url, remote_name, thumbnail, force, pr=gr.Progress(track_tqdm=True)):
        URLResource(self.hub).retrieve(model_id=model_id,
                                       model_url=url,
                                       remote_name=remote_name,
                                       thumbnail_url=thumbnail,
                                       proxy=PROXY,
                                       force=force)
        gr.Info(f"🍺 Add {model_id} ok, page will be reload")
        return gr.update()


@dataclass
class CivitaiResourceUI(UI):
    name: str = "Civitai"
    hub: ModelHub = None

    def _build(self):
        with gr.Group(visible=self.visible):
            self.model_id = gr.Text(label="model_id")
            self.revision = gr.Text(label="revision")
            with gr.Accordion("more", open=False):
                self.force = gr.Checkbox(label="force")

        self.btn = gr.Button("Download", variant="primary")

    def run(self, gallery):
        self.btn.click(fn=self.get_resource,
                       inputs=[self.model_id, self.revision, self.force],
                       outputs=[gallery]). \
            success(reload_notify, None, None). \
            success(None, _js="window.location.reload()")

    def get_resource(self, model_id, revision, force, pr=gr.Progress(track_tqdm=True)):
        CivitaiResource(self.hub).retrieve(id=model_id, revision=revision, proxy=PROXY, force=force)
        gr.Info(f"🍺 Add {model_id} ok, page will be reload")
        return gr.update()


@dataclass
class ThumbnailsUI(UI):
    hub: CachedModelHub = None

    def _build(self):
        gr.Markdown("### Thumbnails")
        self.gallery = gr.Gallery(
            visible=self.visible,
            value=self.hub.thumbnails,
            object_fit="cover",
            show_label=False,
            min_width=100,
            height=440,
            columns=6,
            show_download_button=False)

    def run(self, model_id, sub_path, weight_file, trained_words):
        def sel(evt: gr.SelectData):
            _model_id = evt.value[1]
            meta = self.hub.get_meta(_model_id)
            words = ",".join(meta.trained_word)
            return gr.update(value=_model_id), \
                   gr.update(value=meta.sub_path), \
                   gr.update(value=meta.weight_file), \
                   gr.update(value=words)

        self.gallery.select(sel, [], [model_id, sub_path, weight_file, trained_words])


@dataclass
class ModelMetaUI(UI):
    hub: CachedModelHub = None

    def _build(self):
        gr.Markdown("### Meta Info")
        with gr.Group(visible=self.visible):
            self.model_id = gr.Text(label="model id", max_lines=1, interactive=False)
            self.sub_path = gr.Text(label="sub path", max_lines=1)
            self.weight_file = gr.Text(label="weight file", max_lines=1)
            self.trained_word = gr.Text(label="trained word", info="separated by commas", max_lines=1)

        with gr.Row():
            self.remove_btn = gr.Button("🗑️ Remove", variant="primary", min_width=50)
            self.update_btn = gr.Button("🔧 Modify", variant="primary", min_width=50)

    def run(self, *args, **kwargs):
        def modify(model_id, sub_path, weight_file, trained_word):
            self.hub.add_meta(model_id, ModelMeta(sub_path, weight_file, trained_word.split(",")))
            gr.Info(f"🔧 Modify {model_id} ok, page will be reload")

        def remove(model_id):
            self.hub.remove_model(model_id)
            gr.Info(f"🗑️ Remove {model_id} ok, page will be reload")

        self.update_btn.click(modify, [self.model_id, self.sub_path, self.weight_file, self.trained_word], None). \
            success(reload_notify, None, None). \
            success(None, _js="window.location.reload()")

        self.remove_btn.click(remove, [self.model_id], None). \
            success(reload_notify, None, None). \
            success(None, _js="window.location.reload()")


@dataclass
class ModelsDetailUI(UI):
    hub: CachedModelHub = None

    def _build(self):
        with gr.Column(visible=self.visible):
            self.model_meta = ModelMetaUI(name="model_meta", hub=self.hub)
            self.thumbnails = ThumbnailsUI(name="thumbnails", hub=self.hub)
            self.model_zoo = MultiColumnsLayoutUI(
                name="model_zoo",
                blocks=[self.model_meta, self.thumbnails],
                scales=[1, 3])
            self.model_zoo.build()

            gr.Markdown("### Download / Upload Model")
            blocks = [
                FileResourceUI(hub=self.hub),
                CivitaiResourceUI(hub=self.hub),
                URLResourceUI(hub=self.hub),
            ]
            self.tabs = CombinedTabsLayoutUI(name=self.name, blocks=blocks)
            self.tabs.build()

    def run(self):
        self.model_zoo.run(inputs=[Arg(),
                                   Arg(self.model_meta.model_id,
                                       self.model_meta.sub_path,
                                       self.model_meta.weight_file,
                                       self.model_meta.trained_word)])
        self.tabs.run(self.thumbnails.gallery)


@dataclass
class HubUI(UI):
    config: dict[NetworkType, list[ModelType]] = None
    hubs: dict[tuple[NetworkType, ModelType], CachedModelHub] = None

    def _build(self):
        base_models = list(self.config.keys())
        dropdown = gr.Dropdown(choices=base_models, value=base_models[0],
                               interactive=True, label="network type")
        gr.Markdown("## Model Zoo")
        blocks = []

        for base_model, types in self.config.items():
            inner_blocks = []
            for model_type in types:
                cached = self.hubs.get((base_model, model_type))
                inner_blocks.append(ModelsDetailUI(model_type, hub=cached))
            blocks.append(CombinedTabsLayoutUI(blocks=inner_blocks))

        self.hub = OneHotLayoutUI(dropdown=dropdown, blocks=blocks)
        self.hub.build()

    def run(self):
        self.hub.run()
