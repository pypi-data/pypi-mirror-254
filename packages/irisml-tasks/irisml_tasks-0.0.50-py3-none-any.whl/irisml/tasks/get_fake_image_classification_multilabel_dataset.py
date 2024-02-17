import dataclasses
import logging
import random
import typing
import PIL.Image
import PIL.ImageDraw
import torch
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Generate a fake image classification dataset with multiple labels per image.

    The dataset consists of 224x224 RGB images with random color boxes drawn on them.

    Config:
        num_images (int): Number of images to generate. Default: 100
        num_classes (int): Number of classes to generate. Default: 10
        random_seed (int): Random seed. Default: 0
    """
    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Config:
        num_images: int = 100
        num_classes: int = 10
        random_seed: int = 0

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset
        num_classes: int
        class_names: typing.List[str]

    class FakeDataset(torch.utils.data.Dataset):
        def __init__(self, image_labels: typing.List[typing.List[int]], colors: typing.List[typing.Tuple[int, int, int]], random_seed: int):
            self._image_labels = image_labels
            self._colors = colors
            self._random_seed = random_seed
            rng = random.Random(self._random_seed)
            box_center_xy = [(rng.randint(0, 224), rng.randint(0, 224)) for _ in range(len(colors))]
            self._boxes = [(max(0, x - 16), max(0, y - 16), min(224, x + 16), min(224, y + 16)) for x, y in box_center_xy]

        def __len__(self):
            return len(self._image_labels)

        def __getitem__(self, index):
            targets = self._image_labels[index]
            return self._generate_image(targets), torch.zeros(len(self._colors), dtype=torch.int).scatter_(0, torch.tensor(targets), 1)

        def _generate_image(self, targets):
            image = PIL.Image.new('RGB', (224, 224), color=(255, 255, 255))
            draw = PIL.ImageDraw.Draw(image)
            for i, target in enumerate(targets):
                draw.rectangle(self._boxes[i], fill=self._colors[target])
            return image

    def execute(self, inputs):
        if not self.config.num_images or not self.config.num_classes:
            raise ValueError(f"Invalid settings: num_images={self.config.num_images}, num_classes={self.config.num_classes}")

        if self.config.num_images < self.config.num_classes:
            logger.info(f"Some classes will be empty: num_images={self.config.num_images}, num_classes={self.config.num_classes}")

        rng = random.Random(self.config.random_seed)
        image_labels = [random.sample(range(self.config.num_classes), rng.randint(0, self.config.num_classes)) for _ in range(self.config.num_images)]
        colors = [(rng.randint(0, 255), rng.randint(0, 255), rng.randint(0, 255)) for _ in range(self.config.num_classes)]

        return self.Outputs(
            dataset=self.FakeDataset(image_labels, colors, self.config.random_seed),
            num_classes=self.config.num_classes,
            class_names=[f'class_{i}' for i in range(self.config.num_classes)],
        )

    def dry_run(self, inputs):
        return self.execute(inputs)
