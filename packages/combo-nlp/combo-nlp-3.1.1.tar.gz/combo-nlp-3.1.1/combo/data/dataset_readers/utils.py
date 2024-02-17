import torch.distributed as dist


def is_distributed() -> bool:
    """
    Checks if the distributed process group is available and has been initialized
    """
    return dist.is_available() and dist.is_initialized()


class MalformedFileException(Exception):
    def __init__(self, message):
        super().__init__(message)
