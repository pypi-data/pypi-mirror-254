import torch

from combo.config import Registry
from combo.config.from_parameters import register_arguments, FromParameters


@Registry.register('base_scheduler')
class Scheduler(torch.optim.lr_scheduler.LambdaLR, FromParameters):
    pass_down_parameters = ['optimizer']

    @register_arguments
    def __init__(self,
                 optimizer: torch.optim.Optimizer,
                 patience: int = 6,
                 decreases: int = 2,
                 threshold: float = 1e-3,
                 last_epoch: int = -1,
                 verbose: bool = False):
        super().__init__(optimizer, [self._lr_lambda], last_epoch, verbose)
        self.patience = patience
        self.decreases = decreases
        self.threshold = threshold
        self.start_patience = patience
        self.best_score = 0.0

    @staticmethod
    def _lr_lambda(idx: int) -> float:
        return 1.0 / (1.0 + idx * 1e-4)

    def step(self, metric: float = None) -> None:
        super().step()

        if metric is not None:
            if metric - self.best_score > self.threshold:
                self.best_score = metric if metric > self.best_score else self.best_score
                self.patience = self.start_patience
            else:
                if self.patience <= 1:
                    if self.decreases == 0:
                        # The Trainer should trigger early stopping
                        self.patience = 0
                    else:
                        self.patience = self.start_patience
                        self.decreases -= 1
                        self.threshold /= 2
                        self.base_lrs = [x / 2 for x in self.base_lrs]
                else:
                    self.patience -= 1
