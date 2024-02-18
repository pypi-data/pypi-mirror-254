"""Definition of MRI measurements."""

from typing import List

from pymetadata.identifiers.miriam import BQB

from ..node import Choice, DType, InfoNode, MeasurementType
from ..units import (
    AMOUNT_UNITS,
    AUC_DIV_UNITS,
    AUC_UNITS,
    AUMC_UNITS,
    CLEARANCE_UNITS,
    CONCENTRATION_PER_DOSE_UNITS,
    CONCENTRATION_UNITS,
    DIMENSIONLESS,
    FLOW_UNITS,
    NO_UNIT,
    PRESSURE_AUC_UNITS,
    PRESSURE_UNITS,
    RATE_UNITS,
    RATIO_UNITS,
    TIME_UNITS,
    VD_UNITS,
)


IMAGING_MEASUREMENT_NODES: List[InfoNode] = [
    MeasurementType(
        sid="mri-measurement",
        name="MRI measurement",
        description="measurement via MRI",
        parents=["measurement"],
        dtype=DType.ABSTRACT,
        annotations=[],
    ),
    MeasurementType(
        sid="ct-measurement",
        name="CT measurement",
        description="measurement via CT",
        parents=["measurement"],
        dtype=DType.ABSTRACT,
        annotations=[],
    ),
    MeasurementType(
        sid="relative-signal-intensity",
        name="relative signal intensity",
        description="Relative signal intensity normalized to zero time point before"
        "tracer injection",
        parents=["mri measurement"],
        dtype=DType.NUMERIC,
        units=[DIMENSIONLESS],
        annotations=[],
    ),
    MeasurementType(
        sid="maximum-relative-signal-intensity",
        name="maximum relative signal intensity",
        description="Maximum of relative signal intensity normalized to zero time point before"
        "tracer injection",
        parents=["mri measurement"],
        dtype=DType.NUMERIC,
        units=[DIMENSIONLESS],
        annotations=[],
    ),
    MeasurementType(
        sid="attenuation",
        name="attenuation",
        description="Attenuation",
        parents=["ct measurement"],
        dtype=DType.NUMERIC,
        units=[DIMENSIONLESS],
        annotations=[],
    ),
]
