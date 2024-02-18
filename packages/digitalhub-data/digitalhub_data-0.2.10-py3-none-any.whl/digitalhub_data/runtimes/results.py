"""
RunResultsData module.
"""
from __future__ import annotations

import typing

from digitalhub_core.runtimes.results import RunResults

if typing.TYPE_CHECKING:
    from digitalhub_core.entities.artifacts.entity import Artifact
    from digitalhub_data.entities.dataitems.entity import Dataitem


class RunResultsData(RunResults):
    """
    A class representing a run results.
    """

    def __init__(
        self,
        artifacts: list[Artifact] | None = None,
        dataitems: list[Dataitem] | None = None,
    ) -> None:
        """
        Constructor.

        Parameters
        ----------
        dataitems : list[Dataitem]
            The dataitems.
        """
        super().__init__(artifacts)
        self.dataitems = dataitems

    def get_dataitems(self) -> list[Dataitem]:
        """
        Get dataitems.

        Returns
        -------
        list[Dataitem]
            List of dataitems.
        """
        return self.dataitems

    def get_dataitem_by_key(self, key: str) -> Dataitem:
        """
        Get dataitem by key.

        Parameters
        ----------
        key : str
            Key.

        Returns
        -------
        Dataitem
            Dataitem.
        """
        for dataitem in self.dataitems:
            if dataitem.name == key:
                return dataitem
