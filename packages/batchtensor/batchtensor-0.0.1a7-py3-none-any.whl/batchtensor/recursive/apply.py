r"""Contain the main function to recursively apply a function on nested
data."""

from __future__ import annotations

__all__ = ["recursive_apply"]


from typing import TYPE_CHECKING, Any

from batchtensor.recursive.applier import Applier
from batchtensor.recursive.state import ApplyState

if TYPE_CHECKING:
    from collections.abc import Callable

    from batchtensor.recursive import BaseApplier


_applier = Applier()


def recursive_apply(data: Any, func: Callable, applier: BaseApplier | None = None) -> Any:
    r"""Recursively apply a function on all the items in a nested data.

    Args:
        data: Specifies the input data.
        func: Specifies the function to apply on each item.
        applier: Specifies an optional ``BaseApplier`` to customize the
            logic. By default, ``Applier`` is used.

    Returns:
        The transformed data.

     Example usage:

    ```pycon
    >>> from batchtensor.recursive import recursive_apply
    >>> out = recursive_apply({"a": 1, "b": "abc"}, str)
    >>> out
    {'a': '1', 'b': 'abc'}

    ```
    """
    applier = applier or _applier
    return _applier.apply(data=data, func=func, state=ApplyState(applier))
