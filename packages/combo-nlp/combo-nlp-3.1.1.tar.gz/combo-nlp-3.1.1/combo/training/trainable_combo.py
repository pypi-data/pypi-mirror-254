from typing import Any, Dict, List, Optional, Type

import pytorch_lightning as pl
import torch
from torch import Tensor

from combo.config import FromParameters
from combo.data.dataset_loaders.dataset_loader import TensorDict
from combo.modules.model import Model
from combo.training import Scheduler


class TrainableCombo(pl.LightningModule, FromParameters):
    def __init__(self,
                 model: Model,
                 optimizer_type: Type = torch.optim.Adam,
                 optimizer_kwargs: Optional[Dict[str, Any]] = None,
                 scheduler_type: Type = Scheduler,
                 scheduler_kwargs: Optional[Dict[str, Any]] = None,
                 validation_metrics: List[str] = None):
        super().__init__()
        self.model = model
        self._optimizer_type = optimizer_type
        self._optimizer_kwargs = optimizer_kwargs if optimizer_kwargs else {}

        self._scheduler_type = scheduler_type
        self._scheduler_kwargs = scheduler_kwargs if scheduler_kwargs else {}

        self._validation_metrics = validation_metrics if validation_metrics else []

    def forward(self, batch: TensorDict) -> TensorDict:
        return self.model.batch_outputs(batch, self.model.training)

    def training_step(self, batch: TensorDict, batch_idx: int) -> Tensor:
        output = self.forward(batch)
        self.log("train_loss", output['loss'], on_step=True, on_epoch=True, prog_bar=True, logger=True)
        return output["loss"]

    def validation_step(self, batch: TensorDict, batch_idx: int) -> Tensor:
        output = self.forward(batch)
        metrics = self.model.get_metrics()
        for k in metrics.keys():
            if k in self._validation_metrics:
                self.log(k, metrics[k], on_epoch=True, prog_bar=True, logger=True)
        return output["loss"]

    def lr_scheduler_step(self, scheduler: torch.optim.lr_scheduler, metric: Optional[Any]) -> None:
        scheduler.step(metric=metric)

    def configure_optimizers(self):
        optimizer = self._optimizer_type(self.model.parameters(), **self._optimizer_kwargs)
        return ([optimizer],
                [{'scheduler': self._scheduler_type(optimizer, **self._scheduler_kwargs),
                  'interval': 'epoch'}])
