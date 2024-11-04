from datehelper import days_between, add_days, is_weekend, next_weekday
import pytest
from datetime import date, datetime
from datehelper.core import next_weekday

# define test cases for next_weekday function
def test_next_weekday_later_same_week():
    # checks to find the next Thursday from a Monday
    assert next_weekday(date(2024, 11, 4), 3) == date(2024, 11, 7), "Should be the next Thursday in the same week"

def test_next_weekday_early_next_week():
    # checks to find the next Monday from a Friday
    assert next_weekday(date(2024, 11, 8), 0) == date(2024, 11, 11), "Should be the next Monday in the following week"

def test_next_weekday_already_that_day():
    # checks to skip to next week if it's already on the given weekday
    assert next_weekday(date(2024, 11, 6), 2) == date(2024, 11, 13), "Should be the next Wednesday in the following week, not the current one"

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
