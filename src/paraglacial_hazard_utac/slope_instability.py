"""Permafrost degradation and paraglacial rock-slope instability.

Core module: Ballantyne (2002)'s foundational paraglacial-activity
concept, Fey, Wichmann & Zangerl (2025)'s real Eastern Alps rockfall
dataset, and Gruber & Haeberli (2007)'s destabilization mechanism.
"""

from __future__ import annotations

import math

from .constants import (
    BALLANTYNE_2002_CITATION,
    FEY_2025_CITATION,
    FEY_NOTE,
    FEY_PERMAFROST_AREA_PCT_OF_TOTAL,
    FEY_RECENTLY_DEGLACIATED_AREA_PCT_OF_TOTAL,
    FEY_ROCKFALL_COUNT,
    FEY_ROCKFALL_PCT_IN_PERMAFROST_AREA,
    FEY_ROCKFALL_PCT_IN_RECENTLY_DEGLACIATED_AREA,
    GRUBER_HAEBERLI_2007_CITATION,
    GRUBER_HAEBERLI_MECHANISM_NOTE,
    PARAGLACIAL_CONCEPT_NOTE,
)


def rockfall_overrepresentation_factor(
    event_pct_in_zone: float, area_pct_of_total: float
) -> float:
    """How over-represented a hazard zone is among rockfall events, relative to its area share.

    A factor of 1.0 means events are exactly proportional to area (no
    special hazard concentration); >1.0 means the zone produces more
    rockfalls than its area share alone would predict. Using Fey et al.
    (2025)'s own numbers: permafrost terrain (22% of area) hosts 76% of
    rockfalls -> factor ~3.5; recently-deglaciated terrain (4.7% of
    area) hosts 40% of rockfalls -> factor ~8.5.
    """
    if area_pct_of_total <= 0:
        raise ValueError(f"area_pct_of_total must be positive, got {area_pct_of_total}")
    return event_pct_in_zone / area_pct_of_total


def permafrost_overrepresentation_factor() -> float:
    """Fey et al. (2025)'s real permafrost-terrain rockfall over-representation factor."""
    return rockfall_overrepresentation_factor(
        FEY_ROCKFALL_PCT_IN_PERMAFROST_AREA, FEY_PERMAFROST_AREA_PCT_OF_TOTAL
    )


def recently_deglaciated_overrepresentation_factor() -> float:
    """Fey et al. (2025)'s real recently-deglaciated-terrain rockfall over-representation factor."""
    return rockfall_overrepresentation_factor(
        FEY_ROCKFALL_PCT_IN_RECENTLY_DEGLACIATED_AREA,
        FEY_RECENTLY_DEGLACIATED_AREA_PCT_OF_TOTAL,
    )


def paraglacial_activity_decay(
    years_since_deglaciation: float, half_life_years: float = 100.0
) -> float:
    """Illustrative exponential decline of paraglacial slope activity since deglaciation.

    NOT a fitted equation from Ballantyne (2002) -- the paper proposes a
    qualitative general model (activity highest shortly after
    deglaciation, declining as the landscape re-stabilizes) without a
    single universal decay constant. This is a simplified exponential
    stand-in for that qualitative relationship, matching the pattern
    used elsewhere in this ecosystem (e.g. glacier-buffer-utac's
    buffer_sensitivity_multiplier) for illustrating a real qualitative
    trend without claiming a fitted formula. Returns 1.0 at the moment
    of deglaciation, decaying toward 0 as years_since_deglaciation grows.
    """
    if years_since_deglaciation < 0:
        raise ValueError(
            f"years_since_deglaciation must be non-negative, got {years_since_deglaciation}"
        )
    if half_life_years <= 0:
        raise ValueError(f"half_life_years must be positive, got {half_life_years}")
    decay_constant = math.log(2) / half_life_years
    return math.exp(-decay_constant * years_since_deglaciation)


CONCEPT_CITATION = BALLANTYNE_2002_CITATION
CONCEPT_NOTE = PARAGLACIAL_CONCEPT_NOTE
ROCKFALL_DATA_CITATION = FEY_2025_CITATION
ROCKFALL_DATA_NOTE = FEY_NOTE
ROCKFALL_DATA_EVENT_COUNT = FEY_ROCKFALL_COUNT
MECHANISM_CITATION = GRUBER_HAEBERLI_2007_CITATION
MECHANISM_NOTE = GRUBER_HAEBERLI_MECHANISM_NOTE
