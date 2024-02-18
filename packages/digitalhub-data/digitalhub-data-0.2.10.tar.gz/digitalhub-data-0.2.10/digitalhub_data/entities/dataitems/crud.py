"""
Module for performing operations on Dataitem objects.
"""
from __future__ import annotations

import typing

from digitalhub_core.context.builder import check_context, get_context
from digitalhub_core.utils.api import api_ctx_delete, api_ctx_read, api_ctx_update
from digitalhub_core.utils.generic_utils import parse_entity_key
from digitalhub_core.utils.io_utils import read_yaml
from digitalhub_data.entities.dataitems.entity import dataitem_from_dict, dataitem_from_parameters

if typing.TYPE_CHECKING:
    from digitalhub_data.entities.dataitems.entity import Dataitem


def create_dataitem(**kwargs) -> Dataitem:
    """
    Create a new data item with the provided parameters.

    Parameters
    ----------
    **kwargs
        Keyword arguments.

    Returns
    -------
    Dataitem
        Object instance.
    """
    return dataitem_from_parameters(**kwargs)


def create_dataitem_from_dict(obj: dict) -> Dataitem:
    """
    Create a new Dataitem instance from a dictionary.

    Parameters
    ----------
    obj : dict
        Dictionary to create the Dataitem from.

    Returns
    -------
    Dataitem
        Dataitem object.
    """
    check_context(obj.get("project"))
    return dataitem_from_dict(obj)


def new_dataitem(
    project: str,
    name: str,
    kind: str,
    uuid: str | None = None,
    description: str | None = None,
    source: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = True,
    key: str | None = None,
    path: str | None = None,
    **kwargs,
) -> Dataitem:
    """
    Create a new object instance.

    Parameters
    ----------
    project : str
        Name of the project.
    name : str
        Identifier of the dataitem.
    kind : str
        The type of the dataitem.
    uuid : str
        UUID.
    description : str
        Description of the dataitem.
    source : str
        Remote git source for object.
    labels : list[str]
        List of labels.
    embedded : bool
        Flag to determine if object must be embedded in project.
    key : str
        Representation of the dataitem, e.g. store://etc.
    path : str
        Path to the dataitem on local file system or remote storage.
    **kwargs
        Spec keyword arguments.

    Returns
    -------
    Dataitem
       Object instance.
    """
    obj = create_dataitem(
        project=project,
        name=name,
        kind=kind,
        uuid=uuid,
        description=description,
        source=source,
        labels=labels,
        embedded=embedded,
        key=key,
        path=path,
        **kwargs,
    )
    obj.save()
    return obj


def get_dataitem(project: str, name: str, uuid: str | None = None) -> Dataitem:
    """
    Get object from backend.

    Parameters
    ----------
    project : str
        Name of the project.
    name : str
        The name of the dataitem.
    uuid : str
        UUID.

    Returns
    -------
    Dataitem
        Object instance.

    """
    api = api_ctx_read(project, "dataitems", name, uuid=uuid)
    obj = get_context(project).read_object(api)
    return create_dataitem_from_dict(obj)


def get_dataitem_from_key(key: str) -> Dataitem:
    """
    Get dataitem from key.

    Parameters
    ----------
    key : str
        Key of the dataitem.
        It's format is store://<project>/dataitems/<kind>/<name>:<uuid>.
    """
    project, name, uuid = parse_entity_key(key)
    return get_dataitem(project, name, uuid)


def import_dataitem(file: str) -> Dataitem:
    """
    Get object from file.

    Parameters
    ----------
    file : str
        Path to the file.

    Returns
    -------
    Dataitem
        Object instance.
    """
    obj: dict = read_yaml(file)
    check_context(obj.get("project"))
    return create_dataitem_from_dict(obj)


def delete_dataitem(project: str, name: str, uuid: str | None = None) -> dict:
    """
    Delete dataitem from the backend. If the uuid is not specified, delete all versions.

    Parameters
    ----------
    project : str
        Name of the project.
    name : str
        The name of the dataitem.
    uuid : str
        UUID.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_delete(project, "dataitems", name, uuid=uuid)
    return get_context(project).delete_object(api)


def update_dataitem(dataitem: Dataitem) -> dict:
    """
    Update a dataitem.

    Parameters
    ----------
    dataitem : Dataitem
        The dataitem to update.

    Returns
    -------
    dict
        Response from backend.
    """
    api = api_ctx_update(dataitem.project, "dataitems", dataitem.name, uuid=dataitem.id)
    return get_context(dataitem.project).update_object(dataitem.to_dict(), api)
