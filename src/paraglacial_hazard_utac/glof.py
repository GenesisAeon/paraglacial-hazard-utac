"""Glacial Lake Outburst Flood (GLOF) exposure and historical record.

Core module: Taylor, Robinson, Dunning et al. (2023) for present-day
population exposure, Lutzow, Veh & Korup (2023) for the historical
event database. The two paint different pictures on purpose -- see
GLOF_NOTE.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    GLOF_EXPOSED_POPULATION_MILLIONS,
    GLOF_EXPOSED_POPULATION_PCT_IN_TOP4_COUNTRIES,
    GLOF_HISTORIC_DATABASE_COUNTRY_COUNT,
    GLOF_HISTORIC_DATABASE_EVENT_COUNT,
    GLOF_HISTORIC_DATABASE_YEAR_RANGE,
    GLOF_HMA_POPULATION_WITHIN_10KM_MILLIONS,
    GLOF_NOTE,
    GLOF_PCT_IN_ICELAND,
    GLOF_PCT_IN_NW_NORTH_AMERICA,
    GLOF_TOP4_EXPOSED_COUNTRIES,
    LUTZOW_2023_CITATION,
    TAYLOR_2023_CITATION,
)


@dataclass(frozen=True)
class GLOFExposure:
    """Present-day human population exposure to GLOF risk (Taylor et al. 2023)."""

    exposed_population_millions: float
    top4_countries: tuple[str, ...]
    top4_share_pct: float
    hma_within_10km_millions: float
    citation: str


@dataclass(frozen=True)
class GLOFHistoricRecord:
    """Historical GLOF event record, 850-2022 CE (Lutzow, Veh & Korup 2023)."""

    event_count: int
    country_count: int
    year_range: tuple[int, int]
    nw_north_america_share_pct: float
    iceland_share_pct: float
    citation: str


GLOBAL_EXPOSURE = GLOFExposure(
    exposed_population_millions=GLOF_EXPOSED_POPULATION_MILLIONS,
    top4_countries=GLOF_TOP4_EXPOSED_COUNTRIES,
    top4_share_pct=GLOF_EXPOSED_POPULATION_PCT_IN_TOP4_COUNTRIES,
    hma_within_10km_millions=GLOF_HMA_POPULATION_WITHIN_10KM_MILLIONS,
    citation=TAYLOR_2023_CITATION,
)

HISTORIC_RECORD = GLOFHistoricRecord(
    event_count=GLOF_HISTORIC_DATABASE_EVENT_COUNT,
    country_count=GLOF_HISTORIC_DATABASE_COUNTRY_COUNT,
    year_range=GLOF_HISTORIC_DATABASE_YEAR_RANGE,
    nw_north_america_share_pct=GLOF_PCT_IN_NW_NORTH_AMERICA,
    iceland_share_pct=GLOF_PCT_IN_ICELAND,
    citation=LUTZOW_2023_CITATION,
)


def event_frequency_vs_exposure_mismatch_note() -> str:
    """Explicit note: historic event frequency and human exposure are different risk axes."""
    return GLOF_NOTE


def top4_exposed_population_millions() -> float:
    """Approximate population exposed in the top-4 GLOF-exposed countries."""
    return GLOBAL_EXPOSURE.exposed_population_millions * (GLOBAL_EXPOSURE.top4_share_pct / 100.0)
