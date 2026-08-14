# paraglacial-hazard-utac

GenesisAeon Package 102 — paraglacial and geophysical hazard science.
Companion to [glacial-seismicity-utac](https://github.com/GenesisAeon/glacial-seismicity-utac)
(P101): extends GIA/seismicity with a real contrasting case, and adds
two more real paraglacial hazard domains. **Deliberately has no
UTAC/CREP/AFET bridge** — see [DISCLAIMER.md](DISCLAIMER.md).

## What's real here

- **GIA context** (`gia_context.py`): Grosset, Mazzotti & Vernant
  (2023, *Solid Earth*) — in the Western Alps, GIA explains much of
  the observed geodetic deformation but does **not** drive the
  observed seismicity. A real contrast to P101's Alaska/Fairweather
  case, where GIA-induced stress plausibly did help promote a specific
  large earthquake. GIA "explains deformation" and "drives seismicity"
  are two independent questions — this module makes that explicit.
- **Permafrost & rock-slope instability** (`slope_instability.py`):
  Ballantyne (2002)'s foundational paraglacial-geomorphology concept
  (post-deglaciation landscapes are unstable, activity declines over
  time) plus a real, recent dataset — Fey, Wichmann & Zangerl (2025,
  *ESPL*) found permafrost terrain (22% of their Eastern Alps study
  area) hosts 76% of rockfalls, and terrain deglaciated since 1969
  (4.7% of the area) hosts 40% of rockfalls. Mechanism: Gruber &
  Haeberli (2007, *JGR*).
- **GLOF exposure** (`glof.py`): Taylor, Robinson, Dunning et al.
  (2023, *Nature Communications*) — 15 million people globally exposed
  to glacial lake outburst flood risk, over half in India, Pakistan,
  Peru and China. Lützow, Veh & Korup (2023, *ESSD*) — the historic
  event record (3,151 events, 850–2022 CE, 27 countries) is dominated
  by NW North America and Iceland instead — **event frequency and
  human exposure are different, weakly correlated risk axes.**

## Quickstart

```bash
pip install paraglacial-hazard-utac
```

```python
from paraglacial_hazard_utac import (
    WESTERN_ALPS,
    is_deformation_seismicity_paradox,
    permafrost_overrepresentation_factor,
    recently_deglaciated_overrepresentation_factor,
    GLOBAL_EXPOSURE,
    HISTORIC_RECORD,
)

print(is_deformation_seismicity_paradox(WESTERN_ALPS))  # True
print(permafrost_overrepresentation_factor())            # ~3.45
print(recently_deglaciated_overrepresentation_factor())  # ~8.5
print(GLOBAL_EXPOSURE.exposed_population_millions)        # 15.0
print(HISTORIC_RECORD.nw_north_america_share_pct)         # 26.0
```

## Development

```bash
pip install -e ".[dev]"
pre-commit install
ruff check src tests
mypy src
pytest
```

## Citation

See [CITATION.cff](CITATION.cff) and [.zenodo.json](.zenodo.json).
