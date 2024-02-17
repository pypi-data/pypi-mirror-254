import pathlib
import tempfile
import unittest
import torch
from irisml.tasks.load_float_tensor_jsonl import Task


class TestLoadFloatTensorJsonl(unittest.TestCase):
    def test_simple(self):
        with tempfile.NamedTemporaryFile() as f:
            path = pathlib.Path(f.name)
            path.write_text('{"key": [1.0, 2.0, 3.0]}\n{"key": [4.0, 5.0, 6.0]}\n')
            outputs = Task(Task.Config(path=path, key_name='key')).execute(Task.Inputs())
            self.assertIsInstance(outputs.data, torch.Tensor)
            self.assertEqual(outputs.data.shape, (2, 3))
            self.assertEqual(outputs.data.tolist(), [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
