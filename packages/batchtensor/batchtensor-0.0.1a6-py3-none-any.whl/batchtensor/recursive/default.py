r"""Contain the default applier."""

from __future__ import annotations

__all__ = ["DefaultApplier"]


from typing import TYPE_CHECKING, Any

from batchtensor.recursive.applier import register_appliers
from batchtensor.recursive.base import BaseApplier

if TYPE_CHECKING:
    from collections.abc import Callable

    from batchtensor.recursive import ApplyState


class DefaultApplier(BaseApplier[Any]):
    r"""Define the default applier.

    Example usage:

    ```pycon
    >>> from batchtensor.recursive import DefaultApplier, Applier, ApplyState
    >>> state = ApplyState(applier=Applier())
    >>> applier = DefaultApplier()
    >>> applier
    DefaultApplier()
    >>> out = applier.apply([1, "abc"], str, state)
    >>> out
    "[1, 'abc']"

    ```
    """

    def apply(self, data: Any, func: Callable, state: ApplyState) -> Any:
        return func(data)


register_appliers({object: DefaultApplier()})
