"""
Adapted from COMBO
Author: Mateusz Klimaszewski
"""

import torch
import os


class ConfigurationError(Exception):
    def __init__(self, message: str):
        super().__init__()
        self.message = message


def file_exists(*paths):
    """Check whether paths exists."""
    for path in paths:
        if path is None:
            raise ConfigurationError("File cannot be None")
        if not os.path.exists(path):
            raise ConfigurationError(f"Could not find the file at path: '{path}'")


def check_size_match(size_1: torch.Size, size_2: torch.Size, tensor_1_name: str, tensor_2_name: str):
    """Check if tensors' sizes are the same."""
    if size_1 != size_2:
        raise ConfigurationError(
            f"{tensor_1_name} must match {tensor_2_name}, but got {size_1} "
            f"and {size_2} instead"
        )