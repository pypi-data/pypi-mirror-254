import itertools
import unittest
from irisml.tasks.compare import Task


class TestCompare(unittest.TestCase):
    TEST_CASES = [(1, 0), (0, 0), (0, 1)]

    def test_is_equal(self):
        for equal_allowed, greater in itertools.product([True, False], [True, False]):
            self._base_test([False, True, False], equal_allowed, greater, True)

    def test_greater(self):
        self._base_test([True, False, False], False, True, False)

    def test_greater_or_equal(self):
        self._base_test([True, True, False], True, True, False)

    def test_less(self):
        self._base_test([False, False, True], False, False, False)

    def test_less_or_equal(self):
        self._base_test([False, True, True], True, False, False)

    def _base_test(self, expected, equal_allowed, greater, is_equal):
        for test_case, result in zip(self.TEST_CASES, expected):
            outputs = Task(Task.Config(equal_allowed=equal_allowed, greater=greater, is_equal=is_equal)).execute(Task.Inputs(test_case[0], test_case[1]))
            self.assertEqual(outputs.result, result)
