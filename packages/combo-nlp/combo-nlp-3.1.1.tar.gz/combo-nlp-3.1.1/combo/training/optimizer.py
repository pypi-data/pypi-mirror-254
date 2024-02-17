from typing import Tuple

from torch import optim
from combo.config import FromParameters, Registry


class Optimizer(FromParameters):
    def __init__(self):
        pass


@Registry.register("adam")
class Adam(Optimizer, optim.Adam):
    def __init__(self,
                 params,
                 lr: float = 0.001,
                 betas: Tuple[float, float] = (0.9, 0.999),
                 eps: float = 1e-08,
                 weight_decay: float = 0.):
        Optimizer.__init__(self)
        optim.Adam.__init__(self, params=params,
                            lr=lr, betas=betas, eps=eps, weight_decay=weight_decay)
        self.constructed_args = {
            "lr": lr,
            "betas": betas,
            "eps": eps,
            "weight_decay": weight_decay
        }
