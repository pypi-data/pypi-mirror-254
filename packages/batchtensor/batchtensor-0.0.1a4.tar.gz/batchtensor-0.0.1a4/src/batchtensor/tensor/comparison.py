r"""Contain some comparison functions for tensors."""

from __future__ import annotations

__all__ = ["argsort_along_batch", "argsort_along_seq"]

from typing import Any

import torch

from batchtensor.constants import BATCH_DIM, SEQ_DIM


def argsort_along_batch(
    tensor: torch.Tensor, descending: bool = False, **kwargs: Any
) -> torch.Tensor:
    r"""Return the indices that sort a tensor along the batch dimension
    in ascending order by value.

    Note:
        This function assumes the batch dimension is the first
            dimension.

    Args:
        tensor: The input tensor.
        descending: Controls the sorting order (ascending or
            descending).
        kwargs: Additional keywords arguments for ``torch.argsort``.

    Returns:
        The indices that sort a tensor along the batch dimension

    Example usage:

    ```pycon
    >>> import torch
    >>> from batchtensor.tensor import argsort_along_batch
    >>> tensor = torch.tensor([[2, 6], [0, 3], [4, 9], [8, 1], [5, 7]])
    >>> out = argsort_along_batch(tensor)
    >>> out
    tensor([[1, 3], [0, 1], [2, 0], [4, 4], [3, 2]])
    >>> out = argsort_along_batch(tensor, descending=True)
    >>> out
    tensor([[3, 2], [4, 4], [2, 0], [0, 1], [1, 3]])

    ```
    """
    return torch.argsort(tensor, dim=BATCH_DIM, descending=descending, **kwargs)


def argsort_along_seq(
    tensor: torch.Tensor, descending: bool = False, **kwargs: Any
) -> torch.Tensor:
    r"""Return the indices that sort a tensor along the sequence
    dimension in ascending order by value.

    Note:
        This function assumes the sequence dimension is the second
            dimension.

    Args:
        tensor: The input tensor.
        descending: Controls the sorting order (ascending or
            descending).
        kwargs: Additional keywords arguments for ``torch.argsort``.

    Returns:
        The indices that sort a tensor along the sequence dimension.

    Example usage:

    ```pycon
    >>> import torch
    >>> from batchtensor.tensor import argsort_along_seq
    >>> tensor = torch.tensor([[7, 3, 0, 8, 5], [1, 9, 6, 4, 2]])
    >>> out = argsort_along_seq(tensor)
    >>> out
    tensor([[2, 1, 4, 0, 3],
            [0, 4, 3, 2, 1]])
    >>> out = argsort_along_seq(tensor, descending=True)
    >>> out
    tensor([[3, 0, 4, 1, 2],
            [1, 2, 3, 4, 0]])

    ```
    """
    return torch.argsort(tensor, dim=SEQ_DIM, descending=descending, **kwargs)
