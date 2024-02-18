import pytest

from tradinghours.market import Market, MarketHoliday, MicMapping
from tradinghours.currency import Currency, CurrencyHoliday
from tradinghours.schedule import Schedule
from tradinghours.season import SeasonDefinition
from tradinghours.util import snake_case


@pytest.mark.parametrize("model, columns", [
    (Market, ["Exchange Name",
                      "Market Name",
                      "Security Group",
                      "Timezone",
                      "Weekend Definition",
                      "FinID",
                      "MIC",
                      "Acronym",
                      "Asset Type",
                      "Memo",
                      "Permanently Closed",
                      "Replaced By"]
     ),
    (Currency, ["Currency Code",
                "Currency Name",
                "Country Code",
                "Central Bank", 
                "Financial Capital",
                "Financial Capital Timezone",
                "Weekend Definition"]
     ),
    (CurrencyHoliday, ["Currency Code",
                       "Date",
                       "Holiday Name",
                       "Settlement",
                       "Observed",
                       "Memo"]
     ),
    (MarketHoliday, ["FinID",
                     "Date",
                     "Holiday Name",
                     "Schedule",
                     "Settlement",
                     "Observed",
                     "Memo",
                     "Status"]
     ),
    (MicMapping, ["MIC",
                 "FinID"]
     ),
    (Schedule, ["FinID",
                "Schedule Group",
                "Schedule Group Memo",
                "Timezone",
                "Phase Type",
                "Phase Name",
                "Phase Memo",
                "Days",
                "Start",
                "End",
                "Offset Days",
                "Duration",
                "Min Start",
                "Max Start",
                "Min End",
                "Max End",
                "In Force Start Date",
                "In Force End Date",
                "Season Start",
                "Season End"]
     ),
    (SeasonDefinition, ["Season",
                        "Year",
                        "Date"]
     )
])
def test_model_fields(model, columns):

    column_snakes = sorted([snake_case(c) for c in columns])
    field_names = sorted([f.field_name for f in model.fields])
    assert field_names == column_snakes



def test_model_instance():

    aud = Currency.get("AUD")
    assert str(aud.weekend_definition) == "Sat-Sun"

    holidays = MarketHoliday.list_range("US.NYSE", "2007-11-20", "2007-11-23")
    assert len(holidays) == 2

    first, second = holidays

    assert first.holiday_name == "Thanksgiving Day"
    assert first.settlement == "No"
    assert first.status == "Closed"
    assert first.observed is None

    assert second.holiday_name == "Thanksgiving Day"
    assert second.settlement == "Yes"
    assert second.status == "Open"
    assert second.observed == "OBS"







