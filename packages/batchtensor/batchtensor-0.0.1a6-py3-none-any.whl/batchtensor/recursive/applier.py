r"""Contain the main applier that call other appliers."""

from __future__ import annotations

__all__ = ["Applier"]

from typing import TYPE_CHECKING, Any

from coola.utils import str_indent, str_mapping

from batchtensor.recursive.base import BaseApplier

if TYPE_CHECKING:
    from collections.abc import Callable, Mapping

    from batchtensor.recursive import ApplyState


class Applier(BaseApplier[Any]):
    """Implement the default equality tester."""

    registry: dict[type, BaseApplier] = {}

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}(\n  {str_indent(str_mapping(self.registry))}\n)"

    @classmethod
    def add_applier(cls, data_type: type, applier: BaseApplier, exist_ok: bool = False) -> None:
        r"""Add an applier for a given data type.

        Args:
            data_type: Specifies the data type for this test.
            applier: Specifies the applier object.
            exist_ok: If ``False``, ``RuntimeError`` is raised if the
                data type already exists. This parameter should be set
                to ``True`` to overwrite the applier for a type.

        Raises:
            RuntimeError: if a applier is already registered for the
                data type and ``exist_ok=False``.

        Example usage:

        ```pycon
        >>> from batchtensor.recursive import Applier, SequenceApplier
        >>> Applier.add_applier(list, SequenceApplier(), exist_ok=True)

        ```
        """
        if data_type in cls.registry and not exist_ok:
            msg = (
                f"An applier ({cls.registry[data_type]}) is already registered for the data "
                f"type {data_type}. Please use `exist_ok=True` if you want to overwrite the "
                "applier for this type"
            )
            raise RuntimeError(msg)
        cls.registry[data_type] = applier

    def apply(self, data: Any, func: Callable, state: ApplyState) -> Any:
        return self.find_applier(type(data)).apply(data, func, state)

    @classmethod
    def has_applier(cls, data_type: type) -> bool:
        r"""Indicate if an applier is registered for the given data type.

        Args:
            data_type: Specifies the data type to check.

        Returns:
            ``True`` if an applier is registered, otherwise ``False``.

        Example usage:

        ```pycon
        >>> from batchtensor.recursive import Applier
        >>> Applier.has_applier(list)
        True
        >>> Applier.has_applier(str)
        False

        ```
        """
        return data_type in cls.registry

    @classmethod
    def find_applier(cls, data_type: Any) -> BaseApplier:
        r"""Find the applier associated to an object.

        Args:
            data_type: Specifies the data type to get.

        Returns:
            The applier associated to the data type.

        Example usage:

        ```pycon
        >>> from batchtensor.recursive import Applier
        >>> Applier.find_applier(list)
        SequenceApplier()

        ```
        """
        for object_type in data_type.__mro__:
            applier = cls.registry.get(object_type, None)
            if applier is not None:
                return applier
        msg = f"Incorrect data type: {data_type}"
        raise TypeError(msg)


def register_appliers(mapping: Mapping[type, BaseApplier]) -> None:
    for typ, op in mapping.items():
        if not Applier.has_applier(typ):  # pragma: no cover
            Applier.add_applier(typ, op)
