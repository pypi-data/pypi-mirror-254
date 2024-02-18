"""Aggregate models exposed at the top level."""
from typing import Literal, Union

from pydantic import BaseModel, Field
from pytket.passes import BasePass

from quantinuum_schemas.aer import (
    AerCompilationRequest,
    AerConfig,
    AerSimulationRequest,
)
from quantinuum_schemas.qulacs import (
    QulacsCompilationRequest,
    QulacsConfig,
    QulacsSimulationRequest,
)

CompilationRequestData = AerCompilationRequest | QulacsCompilationRequest
SimulationRequestData = AerSimulationRequest | QulacsSimulationRequest
BackendConfig = AerConfig | QulacsConfig


class CompilationRequest(BaseModel):
    data: CompilationRequestData = Field(..., discriminator="name")


class SimulationRequest(BaseModel):
    data: SimulationRequestData = Field(..., discriminator="name")
