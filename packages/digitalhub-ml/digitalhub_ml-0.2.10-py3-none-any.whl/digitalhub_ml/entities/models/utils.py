"""
Models utils module.
"""
from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from digitalhub_ml.entities.models.entity import Model


def get_model_info(model: Model) -> dict:
    """
    Get the information of an model.

    Parameters
    ----------
    model : Model
        The model.

    Returns
    -------
    dict
        The information of the model.
    """
    return {
        "id": f"store://{model.project}/models/{model.kind}/{model.name}:{model.id}",
        "key": model.name,
        "kind": model.kind,
    }
