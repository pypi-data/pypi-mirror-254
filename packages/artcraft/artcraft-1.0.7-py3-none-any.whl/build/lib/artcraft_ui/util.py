import gradio as gr
from typing import Callable
from abc import abstractmethod, ABC
from dataclasses import dataclass, field

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class Arg:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


@dataclass
class UI:
    name: str = ""
    visible: bool = True
    before_build_hooks: list[Callable] = field(default_factory=list)
    after_build_hooks: list[Callable] = field(default_factory=list)

    @abstractmethod
    def _build(self):
        raise NotImplementedError

    def build(self):
        for hook in self.before_build_hooks:
            hook()
        self._build()
        for hook in self.after_build_hooks:
            hook()
        return self

    def run(self, *args, **kwargs):
        pass


@dataclass
class BasicBlocksUI(ABC, UI):
    blocks: list[UI] = field(default_factory=list)

    def run(self, *args, inputs: Arg | list[Arg] | None = None):
        for i, block in enumerate(self.blocks):
            if isinstance(inputs, list):
                arg = inputs[i]
                if arg is not None:
                    block.run(*arg.args, **arg.kwargs)
                else:
                    block.run()
            elif isinstance(inputs, Arg):
                arg = inputs
                block.run(*arg.args, **arg.kwargs)
            else:
                block.run(*args)


class CombinedTabsLayoutUI(BasicBlocksUI):
    def _build(self):
        with gr.Tabs(visible=self.visible):
            for block in self.blocks:
                with gr.TabItem(block.name):
                    block.build()


@dataclass
class MultiColumnsLayoutUI(BasicBlocksUI):
    scales: list[int] = field(default_factory=list)

    def _build(self):
        if len(self.blocks) != len(self.scales):
            raise ValueError("length of blocks and scales not equal")

        with gr.Row(visible=self.visible) as row:
            for i, block in enumerate(self.blocks):
                with gr.Column(scale=self.scales[i]):
                    block.build()


@dataclass
class OneHotLayoutUI(BasicBlocksUI):
    dropdown: gr.component = None

    def _build(self):
        self.columns = []
        for i in range(len(self.blocks)):
            with gr.Column(visible=i == 0 and self.visible) as row:
                self.blocks[i].build()

            self.columns.append(row)

    def run(self, *args, **kwargs):
        super(OneHotLayoutUI, self).run(*args, **kwargs)

        def choose(evt: gr.SelectData):
            res = [gr.update(visible=False)] * len(self.blocks)
            res[evt.index] = gr.update(visible=True)
            return res

        self.dropdown.select(choose, [], self.columns)


###############
# image
###############
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
