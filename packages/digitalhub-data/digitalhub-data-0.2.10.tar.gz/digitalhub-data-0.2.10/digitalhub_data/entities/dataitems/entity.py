"""
Dataitem module.
"""
from __future__ import annotations

import shutil
import typing
from pathlib import Path

from digitalhub_core.context.builder import get_context
from digitalhub_core.entities._base.entity import Entity
from digitalhub_core.entities._builders.metadata import build_metadata
from digitalhub_core.entities._builders.spec import build_spec
from digitalhub_core.entities._builders.status import build_status
from digitalhub_core.stores.builder import get_default_store, get_store
from digitalhub_core.utils.api import api_ctx_create, api_ctx_update
from digitalhub_core.utils.exceptions import EntityError
from digitalhub_core.utils.generic_utils import build_uuid, get_timestamp
from digitalhub_core.utils.io_utils import write_yaml
from digitalhub_core.utils.uri_utils import map_uri_scheme
from digitalhub_data.entities.dataitems.metadata import DataitemMetadata
from digitalhub_data.entities.dataitems.status import DataitemStatus

if typing.TYPE_CHECKING:
    import pandas as pd
    from digitalhub_core.context.context import Context
    from digitalhub_data.entities.dataitems.spec import DataitemSpec


class Dataitem(Entity):
    """
    A class representing a dataitem.
    """

    def __init__(
        self,
        project: str,
        name: str,
        uuid: str,
        kind: str,
        metadata: DataitemMetadata,
        spec: DataitemSpec,
        status: DataitemStatus,
    ) -> None:
        """
        Constructor.

        Parameters
        ----------
        project : str
            Name of the project.
        name : str
            Name of the object.
        uuid : str
            Version of the object.
        kind : str
            Kind of the object.
        metadata : DataitemMetadata
            Metadata of the object.
        spec : DataitemSpec
            Specification of the object.
        status : DataitemStatus
            Status of the object.
        """
        super().__init__()
        self.project = project
        self.name = name
        self.id = uuid
        self.kind = kind
        self.metadata = metadata
        self.spec = spec
        self.status = status

        # Add attributes to be used in the to_dict method
        self._obj_attr.extend(["project", "name", "id"])

    #############################
    #  Save / Export
    #############################

    def save(self, update: bool = False) -> dict:
        """
        Save dataitem into backend.

        Parameters
        ----------
        uuid : str
            Specify uuid for the dataitem to update

        Returns
        -------
        dict
            Mapping representation of Dataitem from backend.
        """
        obj = self.to_dict()

        if not update:
            api = api_ctx_create(self.project, "dataitems")
            return self._context().create_object(obj, api)

        self.metadata.updated = obj["metadata"]["updated"] = get_timestamp()
        api = api_ctx_update(self.project, "dataitems", self.name, self.id)
        return self._context().update_object(obj, api)

    def export(self, filename: str | None = None) -> None:
        """
        Export object as a YAML file.

        Parameters
        ----------
        filename : str
            Name of the export YAML file. If not specified, the default value is used.

        Returns
        -------
        None
        """
        obj = self.to_dict()
        if filename is None:
            filename = f"{self.kind}_{self.name}_{self.id}.yml"
        pth = Path(self.project) / filename
        pth.parent.mkdir(parents=True, exist_ok=True)
        write_yaml(pth, obj)

    #############################
    #  Dataitem Methods
    #############################

    def as_df(self, file_format: str | None = None, **kwargs) -> pd.DataFrame:
        """
        Read dataitem as a pandas DataFrame. If the dataitem is not local, it will be downloaded
        to a temporary folder and deleted after the method is executed. If no file_format is passed,
        the function will try to infer it from the dataitem.spec.path attribute.
        The path of the dataitem is specified in the spec attribute, and must be a store aware path.
        If the dataitem is stored on s3 bucket, the path must be s3://<bucket>/<path_to_dataitem>.
        If the dataitem is stored on database (Postgres is the only one supported), the path must
        be sql://postgres/<database>/<schema>/<table/view>.

        Parameters
        ----------
        file_format : str
            Format of the file. (Supported csv and parquet).
        **kwargs
            Keyword arguments.

        Returns
        -------
        pd.DataFrame
            Pandas DataFrame.
        """
        if self.spec.path is None:
            raise EntityError("Path is not specified.")

        store = get_store(self.spec.path)
        tmp_path = False

        # Download dataitem if not local
        if not self._check_local(self.spec.path):
            path = store.download(self.spec.path)
            tmp_path = True
        else:
            path = self.spec.path

        # Check file format and get dataitem as DataFrame
        extension = self._get_extension(self.spec.path, file_format)
        df = store.read_df(path, extension, **kwargs)

        # Delete tmp folder
        if tmp_path:
            pth = Path(path)
            if pth.is_file():
                pth = pth.parent
            shutil.rmtree(pth)

        return df

    def write_df(self, target_path: str | None = None, df: pd.DataFrame | None = None, **kwargs) -> str:
        """
        Write pandas DataFrame as parquet.
        If no target_path is passed, the dataitem will be written into the default store.
        If no DataFrame is passed, the dataitem will be written into the target_path.

        Parameters
        ----------
        target_path : str
            Path to write the dataframe to
        df : pd.DataFrame
            DataFrame to write.
        **kwargs
            Keyword arguments.

        Returns
        -------
        str
            Path to the written dataframe.
        """
        if target_path is None:
            target_path = f"{self.project}/dataitems/{self.kind}/{self.name}.parquet"
            store = get_default_store()
        else:
            store = get_store(target_path)
        if df is None:
            df = self.as_df()
        return store.write_df(df, target_path, **kwargs)

    #############################
    #  Context
    #############################

    def _context(self) -> Context:
        """
        Get context.

        Returns
        -------
        Context
            Context.
        """
        return get_context(self.project)

    #############################
    #  Helper Methods
    #############################

    @staticmethod
    def _check_local(path: str) -> bool:
        """
        Check if path is local.

        Parameters
        ----------
        path : str
            Path to check.

        Returns
        -------
        bool
            True if local, False otherwise.
        """
        return map_uri_scheme(path) == "local"

    @staticmethod
    def _get_extension(path: str, file_format: str | None = None) -> str:
        """
        Get extension of path.

        Parameters
        ----------
        path : str
            Path to get extension from.
        file_format : str
            File format.

        Returns
        -------
        str
            File extension.

        Raises
        ------
        EntityError
            If file format is not supported.
        """
        if file_format is not None:
            return file_format

        scheme = map_uri_scheme(path)
        if scheme == "sql":
            return "parquet"

        ext = Path(path).suffix[1:]
        if ext is not None:
            return ext
        raise EntityError("Unknown file format. Only csv and parquet are supported.")

    #############################
    #  Static interface methods
    #############################

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
        project = obj.get("project")
        name = obj.get("name")
        kind = obj.get("kind")
        uuid = build_uuid(obj.get("id"))
        metadata = build_metadata(DataitemMetadata, **obj.get("metadata", {}))
        spec = build_spec(
            "dataitems",
            kind,
            layer_digitalhub="digitalhub_data",
            validate=validate,
            **obj.get("spec", {}),
        )
        status = build_status(DataitemStatus, **obj.get("status", {}))
        return {
            "project": project,
            "name": name,
            "uuid": uuid,
            "kind": kind,
            "metadata": metadata,
            "spec": spec,
            "status": status,
        }


def dataitem_from_parameters(
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
    uuid = build_uuid(uuid)
    key = key if key is not None else f"store://{project}/dataitems/{kind}/{name}:{uuid}"
    metadata = build_metadata(
        DataitemMetadata,
        project=project,
        name=name,
        version=uuid,
        description=description,
        source=source,
        labels=labels,
        embedded=embedded,
    )
    spec = build_spec(
        "dataitems",
        kind,
        layer_digitalhub="digitalhub_data",
        key=key,
        path=path,
        **kwargs,
    )
    status = build_status(DataitemStatus)
    return Dataitem(
        project=project,
        name=name,
        uuid=uuid,
        kind=kind,
        metadata=metadata,
        spec=spec,
        status=status,
    )


def dataitem_from_dict(obj: dict) -> Dataitem:
    """
    Create dataitem from dictionary.

    Parameters
    ----------
    obj : dict
        Dictionary to create dataitem from.

    Returns
    -------
    Dataitem
        Dataitem object.
    """
    return Dataitem.from_dict(obj)
