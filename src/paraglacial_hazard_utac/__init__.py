"""paraglacial-hazard-utac -- paraglacial and geophysical hazard science.

GenesisAeon Package 102. Companion to glacial-seismicity-utac (P101):
extends GIA/seismicity with a real contrasting case (Western Alps), and
adds two more real paraglacial hazard domains -- permafrost-driven
rock-slope instability and glacial lake outburst floods (GLOFs).
Deliberately has no UTAC/CREP/AFET bridge -- see DISCLAIMER.md.

All citations independently re-verified 2026-08-14 via direct paper/DOI
lookup -- no confidence-tier split was needed this time, every claim in
this package checked out against its primary source on the first pass.
"""

from .constants import (
    BALLANTYNE_2002_CITATION,
    FEY_2025_CITATION,
    GLOF_EXPOSED_POPULATION_MILLIONS,
    GROSSET_2023_CITATION,
    GRUBER_HAEBERLI_2007_CITATION,
    LUTZOW_2023_CITATION,
    PACKAGE_ID,
    TAYLOR_2023_CITATION,
)
from .gia_context import (
    WESTERN_ALPS,
    GIAContextCase,
    is_deformation_seismicity_paradox,
    is_gia_seismicity_driver,
)
from .glof import (
    GLOBAL_EXPOSURE,
    HISTORIC_RECORD,
    GLOFExposure,
    GLOFHistoricRecord,
    event_frequency_vs_exposure_mismatch_note,
    top4_exposed_population_millions,
)
from .slope_instability import (
    paraglacial_activity_decay,
    permafrost_overrepresentation_factor,
    recently_deglaciated_overrepresentation_factor,
    rockfall_overrepresentation_factor,
)

__version__ = "1.0.1"

__all__ = [
    "BALLANTYNE_2002_CITATION",
    "FEY_2025_CITATION",
    "GLOBAL_EXPOSURE",
    "GLOF_EXPOSED_POPULATION_MILLIONS",
    "GROSSET_2023_CITATION",
    "GRUBER_HAEBERLI_2007_CITATION",
    "HISTORIC_RECORD",
    "LUTZOW_2023_CITATION",
    "PACKAGE_ID",
    "TAYLOR_2023_CITATION",
    "WESTERN_ALPS",
    "GIAContextCase",
    "GLOFExposure",
    "GLOFHistoricRecord",
    "event_frequency_vs_exposure_mismatch_note",
    "is_deformation_seismicity_paradox",
    "is_gia_seismicity_driver",
    "paraglacial_activity_decay",
    "permafrost_overrepresentation_factor",
    "recently_deglaciated_overrepresentation_factor",
    "rockfall_overrepresentation_factor",
    "top4_exposed_population_millions",
]
