"""Tests for paraglacial-hazard-utac."""

import pytest

from paraglacial_hazard_utac import (
    GLOBAL_EXPOSURE,
    HISTORIC_RECORD,
    PACKAGE_ID,
    WESTERN_ALPS,
    __version__,
    event_frequency_vs_exposure_mismatch_note,
    is_deformation_seismicity_paradox,
    is_gia_seismicity_driver,
    paraglacial_activity_decay,
    permafrost_overrepresentation_factor,
    recently_deglaciated_overrepresentation_factor,
    rockfall_overrepresentation_factor,
    top4_exposed_population_millions,
)


def test_version():
    assert __version__ == "1.0.1"


def test_package_id():
    assert PACKAGE_ID == 102


# --- gia_context.py ---------------------------------------------------------


def test_western_alps_case_values():
    assert WESTERN_ALPS.explains_deformation is True
    assert WESTERN_ALPS.drives_seismicity is False
    assert WESTERN_ALPS.citation


def test_is_gia_seismicity_driver_false_for_western_alps():
    assert is_gia_seismicity_driver(WESTERN_ALPS) is False


def test_is_deformation_seismicity_paradox_true_for_western_alps():
    assert is_deformation_seismicity_paradox(WESTERN_ALPS) is True


def test_is_deformation_seismicity_paradox_false_when_no_deformation():
    from paraglacial_hazard_utac import GIAContextCase

    no_deformation_case = GIAContextCase(
        region="test", explains_deformation=False, drives_seismicity=False, note="", citation=""
    )
    assert is_deformation_seismicity_paradox(no_deformation_case) is False


# --- slope_instability.py ---------------------------------------------------


def test_rockfall_overrepresentation_factor_basic():
    # 50% of events in a zone covering 25% of area -> factor 2.0
    assert rockfall_overrepresentation_factor(50.0, 25.0) == pytest.approx(2.0)


def test_rockfall_overrepresentation_factor_rejects_zero_area():
    with pytest.raises(ValueError, match="positive"):
        rockfall_overrepresentation_factor(50.0, 0.0)


def test_permafrost_overrepresentation_factor_real_numbers():
    # 76% of rockfalls in 22% of area -> ~3.45x over-represented
    factor = permafrost_overrepresentation_factor()
    assert factor == pytest.approx(76.0 / 22.0)
    assert factor > 3.0


def test_recently_deglaciated_overrepresentation_factor_real_numbers():
    # 40% of rockfalls in 4.7% of area -> ~8.5x over-represented
    factor = recently_deglaciated_overrepresentation_factor()
    assert factor == pytest.approx(40.0 / 4.7)
    assert factor > 8.0


def test_recently_deglaciated_more_overrepresented_than_permafrost():
    # The recently-deglaciated signal is stronger than the permafrost signal
    assert recently_deglaciated_overrepresentation_factor() > permafrost_overrepresentation_factor()


def test_paraglacial_activity_decay_at_zero_years():
    assert paraglacial_activity_decay(0.0) == pytest.approx(1.0)


def test_paraglacial_activity_decay_at_half_life():
    assert paraglacial_activity_decay(100.0, half_life_years=100.0) == pytest.approx(0.5)


def test_paraglacial_activity_decay_monotonically_decreasing():
    early = paraglacial_activity_decay(10.0)
    late = paraglacial_activity_decay(500.0)
    assert 1.0 > early > late > 0.0


def test_paraglacial_activity_decay_rejects_negative_years():
    with pytest.raises(ValueError, match="non-negative"):
        paraglacial_activity_decay(-1.0)


def test_paraglacial_activity_decay_rejects_bad_half_life():
    with pytest.raises(ValueError, match="positive"):
        paraglacial_activity_decay(10.0, half_life_years=0.0)


# --- glof.py -----------------------------------------------------------------


def test_global_exposure_values():
    assert GLOBAL_EXPOSURE.exposed_population_millions == pytest.approx(15.0)
    assert GLOBAL_EXPOSURE.top4_countries == ("India", "Pakistan", "Peru", "China")
    assert GLOBAL_EXPOSURE.citation


def test_historic_record_values():
    assert HISTORIC_RECORD.event_count == 3151
    assert HISTORIC_RECORD.country_count == 27
    assert HISTORIC_RECORD.year_range == (850, 2022)
    assert HISTORIC_RECORD.citation


def test_top4_exposed_population_millions():
    # >=50% of 15 million
    assert top4_exposed_population_millions() == pytest.approx(7.5)


def test_event_frequency_vs_exposure_mismatch_note_flags_the_mismatch():
    note = event_frequency_vs_exposure_mismatch_note()
    assert "NOT" in note
    assert "population" in note.lower() or "exposure" in note.lower()


def test_historic_hotspots_differ_from_exposure_hotspots():
    # NW North America + Iceland dominate historic EVENT counts...
    assert HISTORIC_RECORD.nw_north_america_share_pct > 20.0
    assert HISTORIC_RECORD.iceland_share_pct > 15.0
    # ...but neither is in the top-4 POPULATION-exposed countries
    assert "Iceland" not in GLOBAL_EXPOSURE.top4_countries
    assert "United States" not in GLOBAL_EXPOSURE.top4_countries
    assert "Canada" not in GLOBAL_EXPOSURE.top4_countries
