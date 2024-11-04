from datetime import datetime, date
from datehelper.core import add_days , days_between #is_weekend, next_weekday

def test_add_days():
    initial_date = datetime.date(2023, 1, 1)
    days_to_add = 10
    new_date = add_days(initial_date, days_to_add)
    assert new_date == datetime.date(2023, 1, 11), "add_days function failed"

def test_days_between():
    assert days_between(date(2023, 1, 1), date(2023, 1, 10)) == 9

def test_days_between_same_date():
    assert days_between(date(2023, 1, 1), date(2023, 1, 1)) == 0

def test_days_between_reverse_order():
    assert days_between(date(2023, 1, 10), date(2023, 1, 1)) == 9

    