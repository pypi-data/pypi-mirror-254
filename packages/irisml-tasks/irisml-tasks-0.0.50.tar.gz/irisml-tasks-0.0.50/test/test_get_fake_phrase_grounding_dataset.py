import unittest
import PIL.Image
import torch
from irisml.tasks.get_fake_phrase_grounding_dataset import Task


class TestGetFakePhraseGroundingDataset(unittest.TestCase):
    def test_simple(self):
        outputs = Task(Task.Config(num_images=100, num_max_boxes=10)).execute(None)
        dataset = outputs.dataset
        self.assertEqual(len(dataset), 100)
        self.assertIsInstance(dataset[0][0][0], str)
        self.assertIsInstance(dataset[0][0][1], PIL.Image.Image)
        self.assertIsInstance(dataset[0][1][0], tuple)
        self.assertEqual(len(dataset[0][1][0][0]), 2)
        self.assertIsInstance(dataset[0][1][0][0][0], int)
        self.assertIsInstance(dataset[0][1][0][0][1], int)
        self.assertIsInstance(dataset[0][1][0][1], torch.Tensor)

    def test_multiple_image_sizes(self):
        outputs = Task(Task.Config(image_sizes=[(8, 8), (24, 24), (16, 16), (64, 2)])).execute(None)
        image_sizes_set = set(image.size for (_, image), _ in outputs.dataset)
        self.assertEqual(image_sizes_set, {(8, 8), (24, 24), (16, 16), (64, 2)})

    def test_random_seed(self):
        outputs1 = Task(Task.Config(num_images=100, random_seed=0)).execute(Task.Inputs())
        outputs2 = Task(Task.Config(num_images=100, random_seed=0)).execute(Task.Inputs())

        targets1 = [d[1][0][1].tolist() if d[1] else None for d in outputs1.dataset]
        targets2 = [d[1][0][1].tolist() if d[1] else None for d in outputs2.dataset]
        self.assertEqual(targets1, targets2)

        outputs3 = Task(Task.Config(num_images=100, random_seed=1)).execute(Task.Inputs())
        targets3 = [d[1][0][1].tolist() if d[1] else None for d in outputs3.dataset]
        self.assertNotEqual(targets1, targets3)
