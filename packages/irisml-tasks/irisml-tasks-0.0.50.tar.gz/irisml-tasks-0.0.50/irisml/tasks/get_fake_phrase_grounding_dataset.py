import dataclasses
import logging
import random
import typing
import irisml.core
import torch
import PIL.Image
import PIL.ImageColor
import PIL.ImageDraw

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Generate a fake phrase grounding dataset.

    An image has a random number of objects. Each object is a bounding box with a random color.

    Configs:
        num_images (int): The number of images to make. Default: 100
        num_max_boxes (int): The max number of objects per image. Default: 10
        image_sizes ([(int, int), ...]): A list of candidate image sizes. Default: [(320, 320)]
        random_seed (int): The random seed. Default: 0
    """
    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Config:
        num_images: int = 100
        num_max_boxes: int = 10  # The max number of objects per image.
        image_sizes: typing.List[typing.Tuple[int, int]] = dataclasses.field(default_factory=lambda: [(320, 320)])
        random_seed: int = 0

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset

    class FakeDataset(torch.utils.data.Dataset):
        def __init__(self, targets: typing.List[typing.Tuple[str, typing.List[typing.List]]], sizes: typing.List[typing.Tuple[int, int]]):
            assert len(targets) == len(sizes)
            self._targets = targets
            self._sizes = sizes

        def __len__(self):
            return len(self._targets)

        def __getitem__(self, index):
            targets = self._targets[index]
            size = self._sizes[index]

            image = PIL.Image.new('RGB', size)
            draw = PIL.ImageDraw.Draw(image)
            for t in targets:
                draw.rectangle((t[1][0] * size[0], t[1][1] * size[1], t[1][2] * size[0], t[1][3] * size[1]), fill=t[0])
            box_text = [f'a {t[0]} box' for t in targets]
            caption = 'This image has ' + ', '.join(box_text)
            current = len('This image has ')
            text_span = []
            for text in box_text:
                text_span.append((current, current + len(text)))
                assert caption[current:current + len(text)] == text
                current += len(text) + 2

            new_targets = [(span, torch.tensor([t[1]])) for span, t in zip(text_span, targets)]
            return (caption, image), new_targets

    def execute(self, inputs):
        rng = random.Random(self.config.random_seed)

        def _random_box(image_width, image_height):
            # Make sure the bounding box size is at least 1 pixel.
            cx = rng.uniform(1 / image_width / 2, 1 - 1 / image_width / 2)
            cy = rng.uniform(1 / image_height / 2, 1 - 1 / image_height / 2)
            w = rng.uniform(1 / image_width, min(1 - cx, cx) * 2)
            h = rng.uniform(1 / image_height, min(1 - cy, cy) * 2)
            return [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2]

        if not self.config.image_sizes:
            raise ValueError("Image sizes setting is empty.")

        for c in self.config.image_sizes:
            if len(c) != 2 or c[0] <= 0 or c[1] <= 0:
                raise ValueError(f"Invalid image size configs: {self.config.image_sizes}")

        sizes = rng.choices(self.config.image_sizes, k=self.config.num_images)
        color_names = list(PIL.ImageColor.colormap.keys())
        targets = []
        for i in range(self.config.num_images):
            boxes = [_random_box(*sizes[i]) for _ in range(rng.randrange(self.config.num_max_boxes + 1))]
            colors = rng.choices(color_names, k=len(boxes))
            targets.append([(color, box) for color, box in zip(colors, boxes)])
        dataset = Task.FakeDataset(targets, sizes)
        return self.Outputs(dataset)

    def dry_run(self, inputs):
        return self.execute(inputs)
