import json
import pathlib
import tempfile
import unittest
import torch
from irisml.tasks.save_float_tensor_jsonl import Task


class TestSaveFloatTensorJsonl(unittest.TestCase):
    def test_simple(self):
        input_data = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        with tempfile.NamedTemporaryFile() as f:
            temp_file = pathlib.Path(f.name)
            Task(Task.Config(path=temp_file, key_name='float')).execute(Task.Inputs(data=input_data))

            with open(temp_file, 'r') as f:
                lines = [json.loads(line) for line in f]
                self.assertEqual(lines, [{'float': [1.0, 2.0, 3.0]}, {'float': [4.0, 5.0, 6.0]}])
