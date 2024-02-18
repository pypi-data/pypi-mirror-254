from collections.abc import Collection
from typing import Optional, Union

import atoti as tt
from atoti._docs_utils import (
    STANDARD_EXTERNAL_TABLE_OPTIONS_KWARGS as _STANDARD_EXTERNAL_TABLE_OPTIONS_KWARGS,
)
from atoti.directquery._external_table_options import ExternalTableOptions
from atoti_core import SetOrDeprecatedSequence, doc

from .table import SynapseTable


class SynapseTableOptions(ExternalTableOptions[SynapseTable]):
    @doc(**_STANDARD_EXTERNAL_TABLE_OPTIONS_KWARGS)
    def __init__(
        self,
        *,
        array_conversion: Optional[
            Union[tt.MultiColumnArrayConversion, tt.MultiRowArrayConversion]
        ] = None,
        clustering_columns: SetOrDeprecatedSequence[str] = frozenset(),
        keys: Optional[Collection[str]] = None,
    ) -> None:
        """Additional options about the external table to create.

        Args:
            {array_conversion}
            {clustering_columns}
            {keys}

        See Also:
            :meth:`atoti.Session.add_external_table`.
        """
        super().__init__(
            array_conversion=array_conversion,
            clustering_columns=clustering_columns,
            keys=keys,
        )
