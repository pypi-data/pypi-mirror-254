import pathlib
import tempfile
import unittest
from irisml.tasks.load_strs_from_text_file import Task


class TestLoadStrsFromTextFile(unittest.TestCase):
    def test_simple(self):
        with tempfile.NamedTemporaryFile() as f:
            temp_filepath = pathlib.Path(f.name)

            temp_filepath.write_text('hello\nworld')
            outputs = Task(Task.Config(filepath=temp_filepath)).execute(Task.Inputs())
            self.assertEqual(outputs.strs, ['hello', 'world'])
            self.assertEqual(outputs.num_strs, 2)

            # With a trailing newline
            temp_filepath.write_text('hello\nworld \n')
            outputs = Task(Task.Config(filepath=temp_filepath)).execute(Task.Inputs())
            self.assertEqual(outputs.strs, ['hello', 'world'])
            self.assertEqual(outputs.num_strs, 2)

            # With a trailing newline and empty line
            temp_filepath.write_text('hello\nworld\n\n')
            outputs = Task(Task.Config(filepath=temp_filepath)).execute(Task.Inputs())
            self.assertEqual(outputs.strs, ['hello', 'world'])
            self.assertEqual(outputs.num_strs, 2)

            # empty file
            temp_filepath.write_text('')
            outputs = Task(Task.Config(filepath=temp_filepath)).execute(Task.Inputs())
            self.assertEqual(outputs.strs, [])
            self.assertEqual(outputs.num_strs, 0)

            # empty file with newline
            temp_filepath.write_text('\n')
            outputs = Task(Task.Config(filepath=temp_filepath)).execute(Task.Inputs())
            self.assertEqual(outputs.strs, [])
            self.assertEqual(outputs.num_strs, 0)

    def test_not_found(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir = pathlib.Path(temp_dir)

            with self.assertRaises(FileNotFoundError):
                Task(Task.Config(filepath=temp_dir / 'not_found.txt')).execute(Task.Inputs())

            outputs = Task(Task.Config(filepath=temp_dir / 'not_found.txt', allow_not_found=True)).execute(Task.Inputs())
            self.assertEqual(outputs.strs, [])
            self.assertEqual(outputs.num_strs, 0)
