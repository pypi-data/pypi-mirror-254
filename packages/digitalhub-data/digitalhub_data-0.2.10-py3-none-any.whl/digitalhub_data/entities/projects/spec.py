"""
Project base specification module.
"""
from __future__ import annotations

from digitalhub_core.entities.projects.spec import ProjectParams, ProjectSpec


class ProjectSpecData(ProjectSpec):
    """
    Project specification.
    """

    def __init__(
        self,
        context: str | None = None,
        functions: list | None = None,
        artifacts: list | None = None,
        workflows: list | None = None,
        dataitems: list | None = None,
    ) -> None:
        """
        Constructor.

        Parameters
        ----------
        dataitems : list
            List of project's dataitems.
        """
        super().__init__(context, functions, artifacts, workflows)
        self.dataitems = dataitems if dataitems is not None else []


class ProjectParamsData(ProjectParams):
    """
    Parameters model for project.
    """

    dataitems: list = None
    """List of project's dataitems."""


SPEC_REGISTRY = {
    "project": [ProjectSpecData, ProjectParamsData],
}
