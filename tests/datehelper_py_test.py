import datetime
from datehelper.add_days import add_days #days_between, is_weekend, next_weekday

def test_add_days():
    initial_date = datetime.date(2023, 1, 1)
    days_to_add = 10
    new_date = add_days(initial_date, days_to_add)
    assert new_date == datetime.date(2023, 1, 11), "add_days function failed"

    