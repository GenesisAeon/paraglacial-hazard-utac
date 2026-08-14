"""Verified constants for paraglacial and geophysical hazard science.

Companion to glacial-seismicity-utac (P101, GIA/seismicity specifically)
and the P99/P100/P101 series generally. P102 covers the broader set of
hazards that emerge as a landscape transitions from glaciated to
deglaciated ("paraglacial" period, Ballantyne 2002): slope instability,
permafrost degradation, and glacial lake outburst floods (GLOFs) --
plus a direct extension of P101's GIA work with a contrasting case.

All citations independently verified via direct paper/DOI lookup on
2026-08-14.
"""

PACKAGE_ID = 102

# =====================================================================
# Foundational concept
# =====================================================================

BALLANTYNE_2002_CITATION = (
    "Ballantyne, C.K. (2002). Paraglacial geomorphology. Quaternary "
    "Science Reviews, 21(18-19), 1935-2017. "
    "DOI: 10.1016/S0277-3791(02)00005-7"
)
BALLANTYNE_2002_DOI = "10.1016/S0277-3791(02)00005-7"

PARAGLACIAL_CONCEPT_NOTE = (
    "Paraglacial geomorphology (Ballantyne 2002) is the study of "
    "earth-surface processes and landforms directly conditioned by "
    "former glaciation and deglaciation. Ice withdrawal exposes "
    "landscapes in an unstable/metastable state, liable to erosion and "
    "sediment release at rates far exceeding background (non-glacial) "
    "denudation rates. Ballantyne documents glacial oversteepening + "
    "debuttressing + stress release as an explanation for numerous "
    "post-deglaciation rock slope failures (e.g. Brecon Beacons, South "
    "Wales) and proposes a general model in which paraglacial activity "
    "is highest shortly after deglaciation and declines over time as "
    "the landscape re-stabilizes."
)

# =====================================================================
# GIA context -- direct extension of P101 (glacial-seismicity-utac)
# =====================================================================

GROSSET_2023_CITATION = (
    "Grosset, J., Mazzotti, S., Vernant, P. (2023). Glacial-isostatic-"
    "adjustment strain rate-stress paradox in the Western Alps and "
    "impact on active faults and seismicity. Solid Earth, 14, "
    "1067-1081. DOI: 10.5194/se-14-1067-2023"
)
GROSSET_2023_DOI = "10.5194/se-14-1067-2023"

GROSSET_NOTE = (
    "The 'strain-rate-stress paradox': GIA-induced stress perturbations "
    "in the Western Alps correlate with the OBSERVED geodetic strain "
    "rates (horizontal extension), but the GIA stress perturbations "
    "themselves tend to either inhibit fault slip or promote the WRONG "
    "failure mechanism relative to the actual seismicity deformation "
    "style. Grosset et al. (2023) therefore conclude GIA explains much "
    "of the region's deformation but does NOT drive or promote the "
    "observed seismicity -- a real, contrasting case to P101's Alaska "
    "example (where GIA-induced Coulomb stress plausibly did promote a "
    "specific large earthquake). Seismic hazard studies in the Western "
    "Alps still require detailed GIA modeling, just not as a seismicity "
    "driver."
)

# =====================================================================
# Permafrost degradation and rock-slope instability
# =====================================================================

FEY_2025_CITATION = (
    "Fey, C., Wichmann, V., Zangerl, C. (2025). Influence of permafrost "
    "degradation and glacier retreat on recent high mountain rockfall "
    "distribution in the eastern European Alps. Earth Surface Processes "
    "and Landforms, 50(5), e70063. DOI: 10.1002/esp.70063"
)
FEY_2025_DOI = "10.1002/esp.70063"

# Stubaier/Oetztaler Alps (Austria) rockfall inventory, 1989 events,
# 200-200,000 m^3 volume range
FEY_ROCKFALL_COUNT = 1989
# Share of rockfalls occurring in permafrost-affected terrain (mean
# annual ground surface temperature, MAGST, below 0C)
FEY_ROCKFALL_PCT_IN_PERMAFROST_AREA = 76.0
# That permafrost-affected terrain is only this share of the total
# potential rockfall area -- i.e. permafrost terrain is massively
# over-represented among rockfall sources
FEY_PERMAFROST_AREA_PCT_OF_TOTAL = 22.0
# Share of rockfall events in terrain deglaciated since 1969
FEY_ROCKFALL_PCT_IN_RECENTLY_DEGLACIATED_AREA = 40.0
# That recently-deglaciated terrain is only this share of the total area
FEY_RECENTLY_DEGLACIATED_AREA_PCT_OF_TOTAL = 4.7

FEY_NOTE = (
    "Both over-representation ratios are striking: permafrost terrain "
    "(22% of the study area) hosts 76% of rockfalls; terrain "
    "deglaciated since 1969 (4.7% of the area) hosts 40% of rockfalls. "
    "Study region: Stubaier/Oetztaler Alps, Austria -- a real, "
    "recent (2025) regional dataset, not a global constant."
)

GRUBER_HAEBERLI_2007_CITATION = (
    "Gruber, S., Haeberli, W. (2007). Permafrost in steep bedrock "
    "slopes and its temperature-related destabilization following "
    "climate change. Journal of Geophysical Research: Earth Surface, "
    "112, F02S18. DOI: 10.1029/2006JF000547"
)
GRUBER_HAEBERLI_2007_DOI = "10.1029/2006JF000547"

GRUBER_HAEBERLI_MECHANISM_NOTE = (
    "Mechanism (Gruber & Haeberli 2007): permafrost in steep bedrock "
    "mechanically stabilizes rock joints via ice infill; warming "
    "reduces ice strength and increases meltwater percolation into "
    "fractures, raising water pressure and destabilizing the rock mass "
    "-- the mechanistic explanation for the Fey et al. (2025) rockfall "
    "over-representation pattern above."
)

# =====================================================================
# Glacial Lake Outburst Floods (GLOFs)
# =====================================================================

TAYLOR_2023_CITATION = (
    "Taylor, C., Robinson, T.R., Dunning, S. et al. (2023). Glacial "
    "lake outburst floods threaten millions globally. Nature "
    "Communications, 14, 487. DOI: 10.1038/s41467-023-36033-x"
)
TAYLOR_2023_DOI = "10.1038/s41467-023-36033-x"

# Global population potentially exposed to GLOF impacts
GLOF_EXPOSED_POPULATION_MILLIONS = 15.0
# Share of the globally exposed population in just four countries
GLOF_EXPOSED_POPULATION_PCT_IN_TOP4_COUNTRIES = 50.0  # "more than half"
GLOF_TOP4_EXPOSED_COUNTRIES = ("India", "Pakistan", "Peru", "China")
# High Mountain Asia: population living within 10 km of a glacial lake
GLOF_HMA_POPULATION_WITHIN_10KM_MILLIONS = 1.0

LUTZOW_2023_CITATION = (
    "Lutzow, N., Veh, G., Korup, O. (2023). A global database of "
    "historic glacier lake outburst floods. Earth System Science Data, "
    "15, 2983-3000. DOI: 10.5194/essd-15-2983-2023"
)
LUTZOW_2023_DOI = "10.5194/essd-15-2983-2023"

# Historic GLOF database: 850-2022 CE, 27 countries
GLOF_HISTORIC_DATABASE_EVENT_COUNT = 3151
GLOF_HISTORIC_DATABASE_COUNTRY_COUNT = 27
GLOF_HISTORIC_DATABASE_YEAR_RANGE = (850, 2022)
# Regional share of reported historic GLOFs, percent
GLOF_PCT_IN_NW_NORTH_AMERICA = 26.0
GLOF_PCT_IN_ICELAND = 19.0

GLOF_NOTE = (
    "GLOF risk is NOT concentrated where most people assume: the "
    "largest historic event counts are in NW North America and Iceland "
    "(sparsely populated), while the largest POPULATION exposure is in "
    "High Mountain Asia (India, Pakistan, Peru, China together account "
    "for over half of the 15 million people globally exposed). Event "
    "frequency and human exposure are two different, only loosely "
    "correlated risk dimensions -- do not conflate them."
)
