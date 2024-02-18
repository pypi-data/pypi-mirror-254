from __future__ import annotations

import typing

from digitalhub_core.entities._builders.metadata import build_metadata
from digitalhub_core.entities._builders.spec import build_spec
from digitalhub_core.entities._builders.status import build_status
from digitalhub_core.entities.projects.metadata import ProjectMetadata
from digitalhub_core.entities.projects.status import ProjectStatus
from digitalhub_core.utils.generic_utils import build_uuid
from digitalhub_data.entities.projects.entity import CTX_ENTITIES, FUNC_MAP, ProjectData
from digitalhub_ml.entities.models.crud import delete_model, get_model, new_model

if typing.TYPE_CHECKING:
    from digitalhub_core.entities.projects.spec import ProjectSpec
    from digitalhub_ml.entities.models.entity import Model


CTX_ENTITIES.append("models")
FUNC_MAP["models"] = get_model


class ProjectMl(ProjectData):
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
    #  Models
    #############################

    def new_model(self, **kwargs) -> Model:
        """
        Create a Model.

        Parameters
        ----------
        **kwargs
            Keyword arguments.

        Returns
        -------
        Model
           Object instance.
        """
        kwargs["project"] = self.name
        kwargs["kind"] = "model"
        obj = new_model(**kwargs)
        self._add_object(obj, "models")
        return obj

    def get_model(self, name: str, uuid: str | None = None) -> Model:
        """
        Get a Model from backend.

        Parameters
        ----------
        name : str
            Identifier of the model.
        uuid : str
            Identifier of the model version.

        Returns
        -------
        Model
            Instance of Model class.
        """
        obj = get_model(
            project=self.name,
            name=name,
            uuid=uuid,
        )
        self._add_object(obj, "models")
        return obj

    def delete_model(self, name: str, uuid: str | None = None) -> None:
        """
        Delete a Model from project.

        Parameters
        ----------
        name : str
            Identifier of the model.
        uuid : str
            Identifier of the model version.

        Returns
        -------
        None
        """
        delete_model(self.name, name, uuid=uuid)
        self._delete_object(name, "models", uuid=uuid)

    def set_model(self, model: Model) -> None:
        """
        Set a Model.

        Parameters
        ----------
        model : Model
            Model to set.

        Returns
        -------
        None
        """
        self._add_object(model, "models")

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
        # Override methods to search in digitalhub_ml
        name = build_uuid(obj.get("name"))
        kind = obj.get("kind")
        metadata = build_metadata(ProjectMetadata, **obj.get("metadata", {}))
        spec = build_spec(
            "projects",
            kind,
            layer_digitalhub="digitalhub_ml",
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
        layer_digitalhub="digitalhub_ml",
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
