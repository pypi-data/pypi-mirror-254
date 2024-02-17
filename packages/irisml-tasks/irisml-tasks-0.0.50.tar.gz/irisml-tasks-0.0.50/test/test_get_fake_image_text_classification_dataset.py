import unittest
import PIL.Image
import torch
from irisml.tasks.get_fake_image_text_classification_dataset import Task


class TestGetFakeImageTextClassificationDataset(unittest.TestCase):
    def test_simple(self):
        outputs = Task(Task.Config(num_images=10, num_classes=2)).execute(Task.Inputs())

        self.assertEqual(len(outputs.dataset), 10)
        self.assertEqual(len(outputs.dataset[0]), 2)
        self.assertIsInstance(outputs.dataset[0][0][0], PIL.Image.Image)
        self.assertIsInstance(outputs.dataset[0][0][1], str)
        self.assertIsInstance(outputs.dataset[0][1], torch.Tensor)
        self.assertEqual(outputs.dataset[0][1].ndim, 0)

        self.assertEqual(outputs.num_classes, 2)
        self.assertEqual(len(outputs.class_names), 2)
