from abc import ABC
from collections.abc import Collection
from typing import Generic, Optional, Union

from atoti_core import SetOrDeprecatedSequence

from ..directquery import MultiColumnArrayConversion, MultiRowArrayConversion
from ._external_table import ExternalTableT_co


class ExternalTableOptions(Generic[ExternalTableT_co], ABC):
    def __init__(
        self,
        *,
        array_conversion: Optional[
            Union[MultiColumnArrayConversion, MultiRowArrayConversion]
        ] = None,
        clustering_columns: SetOrDeprecatedSequence[str],
        keys: Optional[Collection[str]] = None,
    ) -> None:
        self._array_conversion = array_conversion
        self._clustering_columns = frozenset(clustering_columns)
        self._keys = keys
