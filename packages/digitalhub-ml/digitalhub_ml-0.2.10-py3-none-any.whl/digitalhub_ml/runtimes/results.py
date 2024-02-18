"""
RunResultsML module.
"""
from __future__ import annotations

import typing

from digitalhub_data.runtimes.results import RunResultsData

if typing.TYPE_CHECKING:
    from digitalhub_core.entities.artifacts.entity import Artifact
    from digitalhub_data.entities.dataitems.entity import Dataitem
    from digitalhub_ml.entities.models.entity import Model


class RunResultsML(RunResultsData):
    """
    A class representing a run results.
    """

    def __init__(
        self,
        artifacts: list[Artifact] | None = None,
        dataitems: list[Dataitem] | None = None,
        models: list[Model] | None = None,
    ) -> None:
        """
        Constructor.

        Parameters
        ----------
        dataitems : list[Dataitem]
            The dataitems.
        """
        super().__init__(artifacts, dataitems)
        self.models = models

    def get_models(self) -> list[Model]:
        """
        Get models.

        Returns
        -------
        list[Model]
            List of models.
        """
        return self.models

    def get_model_by_key(self, key: str) -> Model:
        """
        Get model by key.

        Parameters
        ----------
        key : str
            Key.

        Returns
        -------
        Model
            Model.
        """
        for model in self.models:
            if model.name == key:
                return model
