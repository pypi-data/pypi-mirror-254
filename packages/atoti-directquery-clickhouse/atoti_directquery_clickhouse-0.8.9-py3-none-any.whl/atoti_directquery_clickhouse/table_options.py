from collections.abc import Collection
from typing import Optional

from atoti._docs_utils import (
    STANDARD_EXTERNAL_TABLE_OPTIONS_KWARGS as _STANDARD_EXTERNAL_TABLE_OPTIONS_KWARGS,
)
from atoti.directquery._external_table_options import ExternalTableOptions
from atoti_core import SetOrDeprecatedSequence, doc

from .table import ClickhouseTable


class ClickhouseTableOptions(ExternalTableOptions[ClickhouseTable]):
    @doc(**_STANDARD_EXTERNAL_TABLE_OPTIONS_KWARGS)
    def __init__(
        self,
        *,
        clustering_columns: SetOrDeprecatedSequence[str] = frozenset(),
        keys: Optional[Collection[str]] = None,
    ) -> None:
        """Additional options about the external table to create.

        Args:
            {clustering_columns}
            {keys}

        See Also:
            :meth:`atoti.Session.add_external_table`.
        """
        super().__init__(clustering_columns=clustering_columns, keys=keys)
