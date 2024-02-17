import dataclasses
import json
import logging
import pathlib
import torch
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Load a 2D float tensor from a JSONL file.

    This task is paired with the `save_float_tensor_jsonl` task.

    Config:
        path (Path): Path to the JSONL file.
        key_name (str): Name of the key to extract from each JSON object.
    """
    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Config:
        path: pathlib.Path
        key_name: str

    @dataclasses.dataclass
    class Outputs:
        data: torch.Tensor

    def execute(self, inputs):
        logger.info(f"Loading {self.config.path}")
        data = []
        with open(self.config.path) as f:
            for line in f:
                if not line.strip():
                    continue
                data.append(json.loads(line)[self.config.key_name])

        data = torch.tensor(data)
        logger.info(f"Loaded {len(data)} lines. Shape: {data.shape}")

        return self.Outputs(data=data)

    def dry_run(self, inputs):
        return self.Outputs(data=torch.zeros(0, 1))
