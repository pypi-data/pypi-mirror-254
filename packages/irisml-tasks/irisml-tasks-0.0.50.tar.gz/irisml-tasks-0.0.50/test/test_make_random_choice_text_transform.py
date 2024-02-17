import unittest
from irisml.tasks.make_random_choice_text_transform import Task


class TestMakeRandomChoiceTextTransform(unittest.TestCase):
    def test_simple(self):
        transform = Task(Task.Config()).execute(Task.Inputs()).transform

        self.assertEqual(transform('abc'), 'abc')
        self.assertIn(transform('a<|>b<|>c'), ['a', 'b', 'c'])

        all_results = set(transform('a<|>b<|>c') for _ in range(100))
        self.assertEqual(all_results, {'a', 'b', 'c'})
