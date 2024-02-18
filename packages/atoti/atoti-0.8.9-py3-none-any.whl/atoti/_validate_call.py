from typing import Callable, TypeVar

from atoti_core import PYDANTIC_CONFIG as _PYDANTIC_CONFIG
from pydantic import validate_call as __validate_call
from pydantic.dataclasses import dataclass
from typing_extensions import ParamSpec

_P = ParamSpec("_P")
_R = TypeVar("_R")


_validate_call = __validate_call(config=_PYDANTIC_CONFIG)


@dataclass(frozen=True)
class _Test:  # pylint: disable=keyword-only-dataclass
    ...


def validate_call(function: Callable[_P, _R], /) -> Callable[_P, _R]:
    if function.__module__ == _Test.__init__.__module__:
        # The constructors of Pydantic dataclasses are already validated.
        return function

    return _validate_call(function)
