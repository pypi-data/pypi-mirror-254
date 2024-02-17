import dataclasses
import logging
import pathlib
import typing
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Save a list of strings to a text file.

    If the input is None, the task will be skipped.

    Config:
        path (Path): Path to the output file.
    """
    VERSION = '0.1.1'
    CACHE_ENABLED = False

    @dataclasses.dataclass
    class Inputs:
        strs: typing.Optional[typing.List[str]]

    @dataclasses.dataclass
    class Config:
        path: pathlib.Path

    def execute(self, inputs):
        if inputs.strs is None:
            logger.info("inputs.strs is None, skipping")
            return self.Outputs()

        self.config.path.parent.mkdir(parents=True, exist_ok=True)
        self.config.path.write_text('\n'.join(inputs.strs))
        logger.info(f"Saved {len(inputs.strs)} items to {self.config.path}")
        return self.Outputs()
