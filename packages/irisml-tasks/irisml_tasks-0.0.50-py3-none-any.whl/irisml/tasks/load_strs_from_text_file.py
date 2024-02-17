import dataclasses
import logging
import pathlib
import typing
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Load lines from a text file.

    Each line is stripped of whitespace and empty lines are removed.

    Config:
        filepath (Path): Path to the text file.
        allow_not_found (bool): If True, allow the file to not exist. If False, raise an error if the file does not exist. Default: False
    """
    VERSION = '0.1.1'
    CACHE_ENABLED = False

    @dataclasses.dataclass
    class Config:
        filepath: pathlib.Path
        allow_not_found: bool = False

    @dataclasses.dataclass
    class Outputs:
        strs: typing.List[str]
        num_strs: int

    def execute(self, inputs):
        if not self.config.filepath.exists():
            if self.config.allow_not_found:
                logger.warning(f"File not found: {self.config.filepath}")
                return self.Outputs(strs=[], num_strs=0)
            else:
                raise FileNotFoundError(f"File not found: {self.config.filepath}")

        logger.info(f"Loading lines from {self.config.filepath}")
        lines = self.config.filepath.read_text().splitlines()
        lines = [line.strip() for line in lines if line.strip()]
        logger.info(f"Loaded {len(lines)} lines from {self.config.filepath}")
        return self.Outputs(strs=lines, num_strs=len(lines))

    def dry_run(self, inputs):
        return self.execute(inputs)
