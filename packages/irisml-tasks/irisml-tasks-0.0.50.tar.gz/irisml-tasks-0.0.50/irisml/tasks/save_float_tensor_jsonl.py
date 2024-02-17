import dataclasses
import json
import logging
import pathlib
import torch
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Save a 2D float tensor to a JSONL file.

    The input tensor is expected to be a 2D float tensor. Each row of the tensor
    is converted to a JSON object and written to the output file.

    Config:
        path (Path): Path to the output file.
        key_name (str): Name of the key to use for each item in the list.
    """
    VERSION = '0.1.1'
    CACHE_ENABLED = False

    @dataclasses.dataclass
    class Inputs:
        data: torch.Tensor

    @dataclasses.dataclass
    class Config:
        path: pathlib.Path
        key_name: str

    def execute(self, inputs):
        if inputs.data.dim() != 2:
            raise ValueError(f"Expected 2D tensor, got {inputs.data.dim()}D")

        self.config.path.parent.mkdir(parents=True, exist_ok=True)
        with self.config.path.open('w') as f:
            for item in inputs.data:
                json.dump({self.config.key_name: item.tolist()}, f)
                f.write('\n')

        logger.info(f"Saved {len(inputs.data)} items to {self.config.path}")
        return self.Outputs()
