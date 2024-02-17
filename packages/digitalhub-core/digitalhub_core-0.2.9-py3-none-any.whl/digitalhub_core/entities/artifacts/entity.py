"""
Artifact module.
"""
from __future__ import annotations

import typing
from pathlib import Path
from urllib.parse import urlparse

from digitalhub_core.context.builder import get_context
from digitalhub_core.entities._base.entity import Entity
from digitalhub_core.entities._builders.metadata import build_metadata
from digitalhub_core.entities._builders.spec import build_spec
from digitalhub_core.entities._builders.status import build_status
from digitalhub_core.entities.artifacts.metadata import ArtifactMetadata
from digitalhub_core.entities.artifacts.status import ArtifactStatus
from digitalhub_core.stores.builder import get_store
from digitalhub_core.utils.api import api_ctx_create, api_ctx_update
from digitalhub_core.utils.exceptions import EntityError
from digitalhub_core.utils.generic_utils import build_uuid, get_timestamp
from digitalhub_core.utils.io_utils import write_yaml
from digitalhub_core.utils.uri_utils import map_uri_scheme

if typing.TYPE_CHECKING:
    from digitalhub_core.context.context import Context
    from digitalhub_core.entities.artifacts.spec import ArtifactSpec


class Artifact(Entity):
    """
    A class representing a artifact.
    """

    def __init__(
        self,
        project: str,
        name: str,
        uuid: str,
        kind: str,
        metadata: ArtifactMetadata,
        spec: ArtifactSpec,
        status: ArtifactStatus,
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
        metadata : ArtifactMetadata
            Metadata of the object.
        spec : ArtifactSpec
            Specification of the object.
        status : ArtifactStatus
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
        Save artifact into backend.

        Parameters
        ----------
        update : bool
            Flag to indicate update.

        Returns
        -------
        dict
            Mapping representation of Artifact from backend.
        """
        obj = self.to_dict()

        if not update:
            api = api_ctx_create(self.project, "artifacts")
            return self._context().create_object(obj, api)

        self.metadata.updated = obj["metadata"]["updated"] = get_timestamp()
        api = api_ctx_update(self.project, "artifacts", self.name, self.id)
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
    #  Artifacts Methods
    #############################

    def as_file(self, target: str | None = None) -> str:
        """
        Get artifact as file. In the case of a local store, the store returns the current
        path of the artifact. In the case of a remote store, the artifact is downloaded in
        a temporary directory.

        Parameters
        ----------
        target : str
            Target path is the remote path of the artifact where it is stored

        Returns
        -------
        str
            Path of the artifact (temporary or not).
        """
        # Check if target path is provided and if it is remote
        trg = self._parameter_or_default(target, self.spec.target_path)
        self._check_remote(trg)

        # If local store, return local artifact path
        # Check if source path is provided and if it is local
        store = get_store(trg)
        if store.is_local():
            src = self._parameter_or_default(None, self.spec.src_path)
            self._check_local(src)
            return src

        return store.download(trg)

    def download(self, target: str | None = None, dst: str | None = None, overwrite: bool = False) -> str:
        """
        Download artifact from backend.

        Parameters
        ----------
        target : str
            Target path is the remote path of the artifact
        dst : str
            Destination path as filename
        overwrite : bool
            Specify if overwrite an existing file

        Returns
        -------
        str
            Path of the downloaded artifact.
        """

        # Check if target path is provided and if it is remote
        trg = self._parameter_or_default(target, self.spec.target_path)
        self._check_remote(trg)

        # Check if download destination path is specified and rebuild it if necessary
        if dst is None:
            filename = urlparse(trg).path.split("/")[-1]
            dst = f"{self.project}/artifacts/{self.kind}/{filename}"

        # Check if destination path exists for overwrite
        self._check_overwrite(dst, overwrite)

        # Download artifact and return path
        store = get_store(trg)
        return store.download(trg, dst)

    def upload(self, source: str | None = None, target: str | None = None) -> str:
        """
        Upload artifact to backend.

        Parameters
        ----------
        source : str
            Source path is the local path of the artifact
        target : str
            Target path is the remote path of the artifact

        Returns
        -------
        str
            Path of the uploaded artifact.
        """
        # Check if target path is provided and if it is remote
        trg = self._parameter_or_default(target, self.spec.target_path)
        self._check_remote(trg)

        # Check if source path is provided and if it is local
        src = self._parameter_or_default(source, self.spec.src_path)
        self._check_local(src)

        # Get store
        store = get_store(trg)
        if store.is_local():
            raise EntityError("Cannot target local store for upload.")

        # Upload artifact and return remote path
        return store.upload(src, trg)

    #############################
    #  Private Helpers
    #############################

    @staticmethod
    def _parameter_or_default(parameter: str | None = None, default: str | None = None) -> str:
        """
        Check whether a parameter is specified or not. If not, return the default value. If also
        the default value is not specified, raise an exception. If parameter is specified, but
        default value is not, return the parameter and set the default value to the parameter.

        Parameters
        ----------
        parameter : str
            Parameter to check.
        default : str
            Default value.

        Returns
        -------
        str
            Parameter or default value.

        Raises
        ------
        EntityError
            If parameter and default value are not specified.
        """
        if parameter is None:
            if default is None:
                raise EntityError("Path is not specified.")
            return default
        return parameter

    @staticmethod
    def _check_local(path: str) -> None:
        """
        Check through URI scheme if given path is local or not.

        Parameters
        ----------
        path : str
            Path of some source.

        Returns
        -------
        None

        Raises
        ------
        EntityError
            If source path is not local.
        """
        if map_uri_scheme(path) != "local":
            raise EntityError("Only local paths are supported for source paths.")

    @staticmethod
    def _check_remote(path: str) -> None:
        """
        Check through URI scheme if given path is remote.

        Parameters
        ----------
        path : str
            Path of some source.

        Returns
        -------
        None

        Raises
        ------
        EntityError
            If source path is local.
        """
        if map_uri_scheme(path) == "local":
            raise EntityError("Only remote paths are supported for target paths.")

    @staticmethod
    def _check_overwrite(dst: str, overwrite: bool) -> None:
        """
        Check if destination path exists for overwrite.

        Parameters
        ----------
        dst : str
            Destination path as filename.
        overwrite : bool
            Specify if overwrite an existing file.

        Returns
        -------
        None

        Raises
        ------
        Exception
            If destination path exists and overwrite is False.
        """
        if Path(dst).is_file() and not overwrite:
            raise EntityError(f"File {dst} already exists.")

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
        metadata = build_metadata(ArtifactMetadata, **obj.get("metadata", {}))
        spec = build_spec(
            "artifacts",
            kind,
            layer_digitalhub="digitalhub_core",
            validate=validate,
            **obj.get("spec", {}),
        )
        status = build_status(ArtifactStatus, **obj.get("status", {}))
        return {
            "project": project,
            "name": name,
            "uuid": uuid,
            "kind": kind,
            "metadata": metadata,
            "spec": spec,
            "status": status,
        }


def artifact_from_parameters(
    project: str,
    name: str,
    kind: str,
    uuid: str | None = None,
    description: str | None = None,
    source: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = True,
    key: str | None = None,
    src_path: str | None = None,
    target_path: str | None = None,
    **kwargs,
) -> Artifact:
    """
    Create an instance of the Artifact class with the provided parameters.

    Parameters
    ----------
    project : str
        Name of the project.
    name : str
        Identifier of the artifact.
    kind : str
        The type of the artifact.
    uuid : str
        UUID.
    description : str
        Description of the artifact.
    source : str
        Remote git source for object.
    labels : list[str]
        List of labels.
    embedded : bool
        Flag to determine if object must be embedded in project.
    key : str
        Representation of "artifacts"act like store://etc..
    src_path : str
        Path to the artifact on local file system.
    targeth_path : str
        Destination path of the artifact.
    **kwargs
        Spec keyword arguments.

    Returns
    -------
    Artifact
        Artifact object.
    """
    uuid = build_uuid(uuid)
    metadata = build_metadata(
        ArtifactMetadata,
        project=project,
        name=name,
        version=uuid,
        description=description,
        source=source,
        labels=labels,
        embedded=embedded,
    )
    key = key if key is not None else f"store://{project}/artifacts/{kind}/{name}:{uuid}"
    spec = build_spec(
        "artifacts",
        kind,
        layer_digitalhub="digitalhub_core",
        key=key,
        src_path=src_path,
        target_path=target_path,
        **kwargs,
    )
    status = build_status(ArtifactStatus)
    return Artifact(
        project=project,
        name=name,
        uuid=uuid,
        kind=kind,
        metadata=metadata,
        spec=spec,
        status=status,
    )


def artifact_from_dict(obj: dict) -> Artifact:
    """
    Create artifact from dictionary.

    Parameters
    ----------
    obj : dict
        Dictionary to create artifact from.

    Returns
    -------
    Artifact
        Artifact object.
    """
    return Artifact.from_dict(obj)
