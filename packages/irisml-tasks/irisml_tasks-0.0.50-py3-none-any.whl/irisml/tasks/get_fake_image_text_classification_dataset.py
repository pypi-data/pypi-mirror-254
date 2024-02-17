import dataclasses
import logging
import random
import typing
import PIL.Image
import PIL.ImageColor
import torch.utils.data
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Generate a fake image-text classification dataset.

    A generated dataset returns ((image: PIL.Image, text: str), class_id: torch.LongTensor[]) pairs.

    Images are 224x224 pixels, and are filled with a single color. The color is chosen randomly from the list of
    colors in PIL.ImageColor.colormap, and the list is shuffled with the given random seed.

    Config:
        num_images (int): Number of images to generate. Default: 100.
        num_classes (int): Number of classes to generate. Default: 10.
        random_seed (int): Random seed. Default: 0.
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
        def __init__(self, num_images, num_classes, random_seed):
            color_names = list(PIL.ImageColor.colormap.keys())
            if num_classes > len(color_names):
                raise ValueError(f"The maximum number of classes is {len(color_names)}")

            rng = random.Random(random_seed)
            self._classes = rng.choices(color_names, k=num_classes)
            self._targets = [rng.randint(0, num_classes - 1) for _ in range(num_images)]

            logger.debug(f"Generated classes: {self._classes} (random_seed={random_seed})")

        @property
        def class_names(self):
            return self._classes

        def __len__(self):
            return len(self._targets)

        def __getitem__(self, index):
            if index >= len(self._targets):
                raise IndexError

            color_name = self._classes[self._targets[index]]
            image = PIL.Image.new('RGB', (224, 224), color=color_name)
            text = f"Color is {color_name}"
            return (image, text), torch.tensor(self._targets[index], dtype=torch.long)

    def execute(self, inputs):
        dataset = Task.FakeDataset(self.config.num_images, self.config.num_classes, self.config.random_seed)
        return self.Outputs(dataset, len(dataset.class_names), dataset.class_names)

    def dry_run(self, inputs):
        return self.execute(inputs)
