"""
Model base specification module.
"""
from __future__ import annotations

from digitalhub_core.entities._base.spec import Spec, SpecParams


class ModelSpec(Spec):
    """
    Model specifications.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """


class ModelParams(SpecParams):
    """
    Model parameters.
    """


SPEC_REGISTRY = {
    "model": [ModelSpec, ModelParams],
}
