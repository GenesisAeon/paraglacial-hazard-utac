"""GIA context module -- direct extension of P101 (glacial-seismicity-utac).

Adds one real, contrasting case: the Western Alps, where GIA explains
much of the observed geodetic deformation but does NOT drive the
observed seismicity (Grosset, Mazzotti & Vernant 2023) -- unlike
Alaska's Fairweather Fault (P101), where GIA-induced stress plausibly
did help promote a specific large earthquake.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import GROSSET_2023_CITATION, GROSSET_NOTE


@dataclass(frozen=True)
class GIAContextCase:
    """Whether GIA explains regional deformation and/or drives seismicity in a region.

    These are two independent questions -- a region can have real,
    substantial GIA-driven deformation while GIA plays no meaningful
    role in triggering earthquakes there (see WESTERN_ALPS below).
    """

    region: str
    explains_deformation: bool
    drives_seismicity: bool
    note: str
    citation: str


WESTERN_ALPS = GIAContextCase(
    region="Western Alps",
    explains_deformation=True,
    drives_seismicity=False,
    note=GROSSET_NOTE,
    citation=GROSSET_2023_CITATION,
)


def is_gia_seismicity_driver(case: GIAContextCase) -> bool:
    """Whether GIA drives seismicity in this region (independent of explaining deformation)."""
    return case.drives_seismicity


def is_deformation_seismicity_paradox(case: GIAContextCase) -> bool:
    """Whether a region shows the Grosset et al. (2023) paradox: real GIA deformation, no link.

    This is exactly the situation GIA_context is built to make explicit
    -- a common intuition error is to assume 'GIA explains deformation'
    implies 'GIA explains earthquakes here'. It does not, necessarily.
    """
    return case.explains_deformation and not case.drives_seismicity
