import unittest
from irisml.tasks.if_else import Task


class TestIfElse(unittest.TestCase):
    def test_simple(self):
        outputs = Task(Task.Config()).execute(Task.Inputs(condition=True, then_float=1.0, else_float=2.0))
        self.assertEqual(outputs.result_float, 1.0)
        self.assertIsNone(outputs.result_int)
        self.assertIsNone(outputs.result_str)
        self.assertIsNone(outputs.result_str_list)

        outputs = Task(Task.Config()).execute(Task.Inputs(condition=False, then_float=1.0, else_float=2.0))
        self.assertEqual(outputs.result_float, 2.0)

        outputs = Task(Task.Config()).execute(Task.Inputs(condition=True, then_str_list=['a', 'b'], else_str_list=['c', 'd']))
        self.assertEqual(outputs.result_str_list, ['a', 'b'])
        self.assertIsNone(outputs.result_float)
        self.assertIsNone(outputs.result_int)
        self.assertIsNone(outputs.result_str)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            Task(Task.Config()).execute(Task.Inputs(condition=True))

        with self.assertRaises(ValueError):
            Task(Task.Config()).execute(Task.Inputs(condition=True, then_float=1.0, then_int=2))

        with self.assertRaises(ValueError):
            Task(Task.Config()).execute(Task.Inputs(condition=True, then_float=1.0, then_str='a', else_float=2.0, else_str='b'))
