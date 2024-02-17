import unittest
import torch
from irisml.tasks.get_fake_image_classification_multilabel_dataset import Task


class TestGetFakeImageClassificationMultilabelDataset(unittest.TestCase):
    def test_simple(self):
        outputs = Task(Task.Config(num_images=100, num_classes=5)).execute(Task.Inputs())
        self.assertEqual(len(outputs.dataset), 100)
        self.assertEqual(outputs.num_classes, 5)
        self.assertEqual(len(outputs.class_names), 5)

        first_image, first_target = outputs.dataset[0]
        self.assertEqual(first_image.size, (224, 224))
        self.assertEqual(first_target.size(), (5,))
        self.assertEqual(first_target.dtype, torch.int)
        self.assertTrue(x in [0, 1] for x in first_target)
