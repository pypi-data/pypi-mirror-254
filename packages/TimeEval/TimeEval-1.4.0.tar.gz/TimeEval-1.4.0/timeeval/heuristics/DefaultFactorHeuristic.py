from pathlib import Path
from typing import Union, Any

from timeeval import Algorithm
from timeeval.datasets import Dataset
from .base import TimeEvalParameterHeuristic


class DefaultFactorHeuristic(TimeEvalParameterHeuristic):
    def __init__(self, factor: float = 1.0, zero_fb: float = 1.0):
        if zero_fb == 0:
            raise ValueError("You cannot supply a zero_fb of 0!")
        self.factor = factor
        self.zero_fb = zero_fb

    def __call__(self, algorithm: Algorithm, dataset_details: Dataset, dataset_path: Path, **kwargs) -> Any:  # type: ignore[no-untyped-def]
        param_name = kwargs["param_name"]
        try:
            default = algorithm.param_schema[param_name]["defaultValue"]
        except KeyError as e:
            raise ValueError(f"Could not find the default value for parameter {param_name}") from e

        if default == 0:
            default = self.zero_fb

        default_type = type(default)
        return default_type(self.factor * default)
