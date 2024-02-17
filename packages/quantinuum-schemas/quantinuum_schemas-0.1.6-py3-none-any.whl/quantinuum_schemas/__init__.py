"""Aggregate models exposed at the top level."""
from typing import Union

from pydantic import BaseModel, Field

from quantinuum_schemas.aer import AerSimulateRequest
from quantinuum_schemas.qulacs import QulacsSimulateRequest


class SimulateRequest(BaseModel):
    """A generic simulation request."""

    request: Union[AerSimulateRequest, QulacsSimulateRequest] = Field(
        ..., discriminator="backend"
    )
