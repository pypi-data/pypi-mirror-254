"""
Re-implemented AllenNLP BatchSampler
https://github.com/allenai/allennlp/blob/main/allennlp/data/samplers/batch_sampler.py
"""
from typing import Sequence, Iterable, List, Optional
from torch import Tensor

from combo.config import Registry, FromParameters


@Registry.register('base_batch_sampler')
class BatchSampler(FromParameters):
    def get_batch_indices(self, instances: Sequence[Tensor]) -> Iterable[List[int]]:
        raise NotImplementedError

    def get_num_batches(self, instances: Sequence[Tensor]) -> int:
        raise NotImplementedError

    def get_batch_size(self) -> Optional[int]:
        """
        Not all `BatchSamplers` define a consistent `batch_size`, but those that
        do should override this method.
        """
        return None
