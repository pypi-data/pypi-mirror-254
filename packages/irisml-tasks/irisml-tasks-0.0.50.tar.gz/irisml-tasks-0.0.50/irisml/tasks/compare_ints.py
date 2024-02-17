import dataclasses
import logging
import irisml.core
from typing import Optional

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """ Compare two int values.
    when is_equal=true, it tests for equality, otherwise it tests for greater than or less than.

    Config:
        is_equal (bool): Whether the two values should be equal.
        greater (bool): Whether the first value should be greater than the second.
        equal_allowed (bool): Whether equal values are allowed, when testing for greater than or less than.
    Inputs:
        val1 (int): value 1
        val2 (int): value 2
    """
    VERSION = '0.1.1'

    @dataclasses.dataclass
    class Inputs:
        val1: int
        val2: int

    @dataclasses.dataclass
    class Outputs:
        result: bool

    @dataclasses.dataclass
    class Config:
        equal_allowed: Optional[bool] = True
        greater: Optional[bool] = True
        is_equal: Optional[bool] = False

    def execute(self, inputs):
        if self.config.is_equal:
            return self.Outputs(inputs.val1 == inputs.val2)

        if self.config.equal_allowed and inputs.val1 == inputs.val2:
            return self.Outputs(True)

        return self.Outputs(inputs.val1 > inputs.val2 if self.config.greater else inputs.val1 < inputs.val2)

    def dry_run(self, inputs):
        return self.execute(inputs)
