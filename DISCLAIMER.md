# DISCLAIMER — Real Science, No Framework Bridge

**Status: Real, independently verified science. NO UTAC/CREP/AFET bridge.**

## What this is

Every figure in this package was checked directly against the paper
(DOI lookup, publisher abstract, or press summary) on 2026-08-14.

- **Grosset, Mazzotti & Vernant (2023)**, *Solid Earth* 14, 1067-1081,
  DOI: 10.5194/se-14-1067-2023 — a real, contrasting GIA case for the
  Western Alps: GIA explains much of the observed geodetic strain rate
  but its stress perturbations tend to either inhibit fault slip or
  promote the wrong failure mechanism relative to observed seismicity.
  The authors conclude GIA does not drive or promote the Western Alps'
  current seismicity — even though seismic hazard studies there still
  need detailed GIA modeling for other reasons. This complements, not
  contradicts, P101's Alaska case (where GIA-induced stress plausibly
  did help promote the 1958 Fairweather Fault earthquake).
- **Ballantyne (2002)**, *Quaternary Science Reviews* 21(18-19),
  1935-2017, DOI: 10.1016/S0277-3791(02)00005-7 — the foundational,
  extremely widely cited paraglacial-geomorphology review. Real,
  documented rock-slope failures (e.g. Brecon Beacons, South Wales)
  attributed to glacial oversteepening/debuttressing/stress release.
- **Fey, Wichmann & Zangerl (2025)**, *Earth Surface Processes and
  Landforms* 50(5), e70063, DOI: 10.1002/esp.70063 — a real, recent
  (1,989-event) rockfall inventory for the Stubaier/Ötztaler Alps,
  Austria. The 76%-in-22%-of-area and 40%-in-4.7%-of-area
  over-representation figures are specific to this regional dataset,
  not universal constants — see `FEY_NOTE` in `constants.py`.
- **Gruber & Haeberli (2007)**, *JGR Earth Surface* 112, F02S18, DOI:
  10.1029/2006JF000547 — the mechanistic explanation (ice-filled joint
  strength loss + meltwater percolation raising water pressure) behind
  the Fey et al. pattern above.
- **Taylor, Robinson, Dunning et al. (2023)**, *Nature Communications*
  14, 487, DOI: 10.1038/s41467-023-36033-x — real, current (15 million
  people) global GLOF population-exposure estimate.
- **Lützow, Veh & Korup (2023)**, *Earth System Science Data* 15,
  2983-3000, DOI: 10.5194/essd-15-2983-2023 — the real historic GLOF
  event database (3,151 events, 850-2022 CE, 27 countries).

## What this is NOT

- **`paraglacial_activity_decay()` is illustrative, not fitted.** It is
  a simplified exponential stand-in for Ballantyne (2002)'s qualitative
  "activity highest right after deglaciation, declining over time"
  model — the paper proposes no single universal decay constant. Same
  honesty pattern as `glacier-buffer-utac`'s
  `buffer_sensitivity_multiplier()`.
- **The Fey et al. (2025) over-representation factors are regional**
  (Eastern Alps, Austria), not global constants — see `FEY_NOTE`.
- **GLOF event-frequency hotspots (NW North America, Iceland) and
  human-exposure hotspots (India, Pakistan, Peru, China) are
  deliberately kept separate** — conflating them would misrepresent
  which risk dimension matters for which purpose (geomorphological
  research vs. disaster-risk planning).
- **No UTAC/CREP/AFET bridge.** This is a real, standalone geohazard
  topic; the cited papers already provide the relevant quantitative
  structure without this ecosystem's cross-domain vocabulary.

## Real-world confirmation (observed, not predicted)

This package was released 2026-08-15, and the underlying literature
(Ballantyne 2002, Fey/Wichmann/Zangerl 2025, Taylor/Robinson/Dunning 2023)
was cited independently of any specific future event. On 2026-08-26, a
major glacier collapse at Langtang Lirung (Nepal-China border) sent a
large debris mass downslope causing severe flooding; National Geographic
Germany's coverage of high-mountain glacier-collapse risk (2026-08-29,
citing the Blatten/Birchgletscher, Switzerland collapse of May 2026 and
GLOF exposure concentrated in the Himalaya/Tibetan Plateau) describes
exactly the permafrost-driven rock-slope instability and GLOF-exposure
pattern this package's `paraglacial_activity_decay()` and GLOF-exposure
functions are built from.

This is **not** a prediction this package made — it did not forecast
Langtang Lirung, Blatten, or any specific event. What it documents is that
the general risk mechanism already established in the cited peer
literature (permafrost thaw destabilizing slopes; GLOF exposure
concentrated in exactly these regions) continues to manifest in real,
dated events after this package's release. Noted here as one more data
point, not as validation of any package-specific formula or constant.

## References

- Grosset, J., Mazzotti, S., Vernant, P. (2023). *Solid Earth*, 14,
  1067-1081. DOI: 10.5194/se-14-1067-2023.
- Ballantyne, C.K. (2002). *Quaternary Science Reviews*, 21(18-19),
  1935-2017. DOI: 10.1016/S0277-3791(02)00005-7.
- Fey, C., Wichmann, V., Zangerl, C. (2025). *ESPL*, 50(5), e70063.
  DOI: 10.1002/esp.70063.
- Gruber, S., Haeberli, W. (2007). *JGR Earth Surface*, 112, F02S18.
  DOI: 10.1029/2006JF000547.
- Taylor, C., Robinson, T.R., Dunning, S. et al. (2023). *Nature
  Communications*, 14, 487. DOI: 10.1038/s41467-023-36033-x.
- Lützow, N., Veh, G., Korup, O. (2023). *ESSD*, 15, 2983-3000. DOI:
  10.5194/essd-15-2983-2023.

All verified directly (2026-08-14) via WebSearch against the
publisher/journal record for each paper. Originating dialogue:
`P 102.txt` (Johann + Kimi) and `P102.md` (Kimi's own deep-research
audit and restructuring proposal, itself independently spot-checked
before this package was built).
