"""
Adapted from COMBO
https://gitlab.clarin-pl.eu/syntactic-tools/combo/-/blob/master/combo/models/base.py
"""

import torch
from combo.config.from_parameters import FromParameters
from typing import Dict, List, Optional, Union


class Predictor(torch.nn.Module, FromParameters):
    def forward(self,
                x: Union[torch.Tensor, List[torch.Tensor]],
                mask: Optional[torch.BoolTensor] = None,
                labels: Optional[Union[torch.Tensor, List[torch.Tensor]]] = None,
                sample_weights: Optional[Union[torch.Tensor, List[torch.Tensor]]] = None) -> Dict[str, torch.Tensor]:
        raise NotImplementedError()
