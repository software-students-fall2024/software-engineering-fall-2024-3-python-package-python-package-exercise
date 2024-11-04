from datetime import timedelta

def days_between(date1, date2):
    return abs((date2 - date1).days)

def add_days(date, days):
     return date + timedelta(days=days)