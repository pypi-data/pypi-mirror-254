import pathlib
import tempfile
import unittest
from irisml.tasks.save_strs_text import Task


class TestSaveStrsText(unittest.TestCase):
    def test_simple(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir = pathlib.Path(temp_dir)
            Task(Task.Config(path=temp_dir / 'new_dir' / 'new_file.txt')).execute(Task.Inputs(['hello', 'world']))
            self.assertTrue((temp_dir / 'new_dir' / 'new_file.txt').exists())
            self.assertEqual((temp_dir / 'new_dir' / 'new_file.txt').read_text(), 'hello\nworld')

    def test_none_inputs(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = pathlib.Path(temp_dir) / 'new_dir' / 'new_file.txt'
            Task(Task.Config(path=temp_path)).execute(Task.Inputs(None))
            self.assertFalse(temp_path.exists())
