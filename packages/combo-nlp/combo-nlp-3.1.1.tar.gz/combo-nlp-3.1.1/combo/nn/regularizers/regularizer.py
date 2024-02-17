import re
from typing import List, Tuple, Dict, Any

import torch

from combo.config import FromParameters, Registry
from combo.config.from_parameters import register_arguments, resolve
from combo.nn.regularizers import Regularizer
from combo.utils.checks import ConfigurationError


@Registry.register('base_regularizer')
class RegularizerApplicator(FromParameters):
    """
    Applies regularizers to the parameters of a Module based on regex matches.
    """
    @register_arguments
    def __init__(self, regexes: List[Tuple[str, Regularizer]] = None) -> None:
        """
        # Parameters
        regexes : `List[Tuple[str, Regularizer]]`, optional (default = `None`)
            A sequence of pairs (regex, Regularizer), where each Regularizer
            applies to the parameters its regex matches (and that haven't previously
            been matched).
        """
        self._regularizers = regexes or []

    def __call__(self, module: torch.nn.Module) -> torch.Tensor:
        """
        # Parameters
        module : `torch.nn.Module`, required
            The module to regularize.
        """
        accumulator = 0.0
        for name, parameter in module.named_parameters():
            # We first check if the parameter needs gradient updates or not
            if parameter.requires_grad:
                # For each parameter find the first matching regex.
                for regex, regularizer in self._regularizers:
                    if re.search(regex, name):
                        penalty = regularizer(parameter)
                        accumulator = accumulator + penalty
                        break
        return accumulator

    @classmethod
    def from_parameters(cls,
                        parameters: Dict[str, Any] = None,
                        constructor_method_name: str = None,
                        pass_down_parameters: Dict[str, Any] = None):
        regexes = parameters.get('regexes', [])
        regexes_to_pass = []
        for regex, regularizer_dict in regexes:
            if isinstance(regularizer_dict, dict):
                if 'type' not in regularizer_dict:
                    raise ConfigurationError('Regularizer dict does not have the type field')
                resolved_regularizer = resolve(regularizer_dict, pass_down_parameters)
                regexes_to_pass.append((regex, resolved_regularizer))
            else:
                regexes_to_pass.append((regex, regularizer_dict))
        return cls(regexes_to_pass)
