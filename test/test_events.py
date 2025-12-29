import datetime as dt
from days_since.events import Event, days_since


def test_days_since():
    today = dt.date.today()
    assert days_since(Event(today.isoformat(), "today")) == 0
    yesterday = today - dt.timedelta(days=1)
    assert days_since(Event(yesterday.isoformat(), "yesterday")) == 1
    one_year_ago = today - dt.timedelta(days=365)
    assert days_since(Event(one_year_ago.isoformat(), "1 year ago")) == 365
    tomorrow = today + dt.timedelta(days=1)
    assert days_since(Event(tomorrow.isoformat(), "tomorrow")) == -1
