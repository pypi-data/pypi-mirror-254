from __future__ import annotations

import typing

from digitalhub_core.entities._builders.metadata import build_metadata
from digitalhub_core.entities._builders.spec import build_spec
from digitalhub_core.entities._builders.status import build_status
from digitalhub_core.entities.projects.entity import CTX_ENTITIES, FUNC_MAP, Project
from digitalhub_core.entities.projects.metadata import ProjectMetadata
from digitalhub_core.entities.projects.status import ProjectStatus
from digitalhub_core.utils.generic_utils import build_uuid
from digitalhub_data.entities.dataitems.crud import delete_dataitem, get_dataitem, new_dataitem

if typing.TYPE_CHECKING:
    from digitalhub_core.entities.projects.spec import ProjectSpec
    from digitalhub_data.entities.dataitems.entity import Dataitem


CTX_ENTITIES.append("dataitems")
FUNC_MAP["dataitems"] = get_dataitem


class ProjectData(Project):
    def __init__(
        self,
        name: str,
        kind: str,
        metadata: ProjectMetadata,
        spec: ProjectSpec,
        status: ProjectStatus,
        local: bool = False,
    ) -> None:
        """
        Constructor.
        """
        super().__init__(name, kind, metadata, spec, status, local)

    #############################
    #  Dataitems
    #############################

    def new_dataitem(self, **kwargs) -> Dataitem:
        """
        Create a Dataitem.

        Parameters
        ----------
        **kwargs
            Keyword arguments.

        Returns
        -------
        Dataitem
           Object instance.
        """
        kwargs["project"] = self.name
        kwargs["kind"] = "dataitem"
        obj = new_dataitem(**kwargs)
        self._add_object(obj, "dataitems")
        return obj

    def get_dataitem(self, name: str, uuid: str | None = None) -> Dataitem:
        """
        Get a Dataitem from backend.

        Parameters
        ----------
        name : str
            Identifier of the dataitem.
        uuid : str
            Identifier of the dataitem version.

        Returns
        -------
        Dataitem
            Instance of Dataitem class.
        """
        obj = get_dataitem(
            project=self.name,
            name=name,
            uuid=uuid,
        )
        self._add_object(obj, "dataitems")
        return obj

    def delete_dataitem(self, name: str, uuid: str | None = None) -> None:
        """
        Delete a Dataitem from project.

        Parameters
        ----------
        name : str
            Identifier of the dataitem.
        uuid : str
            Identifier of the dataitem version.

        Returns
        -------
        None
        """
        delete_dataitem(self.name, name, uuid=uuid)
        self._delete_object(name, "dataitems", uuid=uuid)

    def set_dataitem(self, dataitem: Dataitem) -> None:
        """
        Set a Dataitem.

        Parameters
        ----------
        dataitem : Dataitem
            Dataitem to set.

        Returns
        -------
        None
        """
        self._add_object(dataitem, "dataitems")

    @staticmethod
    def _parse_dict(
        obj: dict,
        validate: bool = True,
    ) -> dict:
        """
        Get dictionary and parse it to a valid entity dictionary.

        Parameters
        ----------
        entity : str
            Entity type.
        obj : dict
            Dictionary to parse.

        Returns
        -------
        dict
            A dictionary containing the attributes of the entity instance.
        """
        # Override methods to search in digitalhub_data
        name = build_uuid(obj.get("name"))
        kind = obj.get("kind")
        metadata = build_metadata(ProjectMetadata, **obj.get("metadata", {}))
        spec = build_spec(
            "projects",
            kind,
            layer_digitalhub="digitalhub_data",
            validate=validate,
            **obj.get("spec", {}),
        )
        status = build_status(ProjectStatus, **obj.get("status", {}))
        local = obj.get("local", False)
        return {
            "name": name,
            "kind": kind,
            "metadata": metadata,
            "spec": spec,
            "status": status,
            "local": local,
        }


def project_from_parameters(
    name: str,
    kind: str,
    description: str | None = None,
    source: str | None = None,
    labels: list[str] | None = None,
    local: bool = False,
    context: str | None = None,
    **kwargs,
) -> ProjectData:
    """
    Create project.

    Parameters
    ----------
    name : str
        Identifier of the project.
    kind : str
        The type of the project.
    description : str
        Description of the project.
    source : str
        Remote git source for object.
    labels : list[str]
        List of labels.
    local : bool
        Flag to determine if object will be exported to backend.
    context : str
        The context of the project.
    **kwargs
        Spec keyword arguments.

    Returns
    -------
    ProjectData
        ProjectData object.
    """
    name = build_uuid(name)
    spec = build_spec(
        "projects",
        kind,
        layer_digitalhub="digitalhub_data",
        context=context,
        **kwargs,
    )
    metadata = build_metadata(
        ProjectMetadata,
        name=name,
        description=description,
        labels=labels,
        source=source,
    )
    status = build_status(ProjectStatus)
    return ProjectData(
        name=name,
        kind=kind,
        metadata=metadata,
        spec=spec,
        status=status,
        local=local,
    )


def project_from_dict(obj: dict) -> ProjectData:
    """
    Create project from dictionary.

    Parameters
    ----------
    obj : dict
        Dictionary to create project from.

    Returns
    -------
    ProjectData
        ProjectData object.
    """
    return ProjectData.from_dict(obj)
