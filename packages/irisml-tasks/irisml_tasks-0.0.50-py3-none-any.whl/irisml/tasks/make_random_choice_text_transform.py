import dataclasses
import random
import typing
import irisml.core


class Task(irisml.core.TaskBase):
    """Make a text transform function that randomly chooses one of the substrings separated by the delimiter.

    Config:
        delimiter (str): The delimiter to split the text by.
    """
    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Config:
        delimiter: str = '<|>'

    @dataclasses.dataclass
    class Outputs:
        transform: typing.Callable[[str], str]

    def execute(self, inputs):
        return self.Outputs(transform=RandomChoiceTransform(self.config.delimiter))

    def dry_run(self, inputs):
        return self.execute(inputs)


class RandomChoiceTransform:
    def __init__(self, delimiter):
        self._delimiter = delimiter

    def __call__(self, text):
        return random.choice(text.split(self._delimiter))
