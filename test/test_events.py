import os
import datetime as dt
from days_since.events import Event, days_since, save_json, load_json


def test_days_since():
    today = dt.date.today()
    assert days_since(Event(today.isoformat(), "today")) == 0
    yesterday = today - dt.timedelta(days=1)
    assert days_since(Event(yesterday.isoformat(), "yesterday")) == 1
    one_year_ago = today - dt.timedelta(days=365)
    assert days_since(Event(one_year_ago.isoformat(), "1 year ago")) == 365
    tomorrow = today + dt.timedelta(days=1)
    assert days_since(Event(tomorrow.isoformat(), "tomorrow")) == -1


def test_save_load_json():
    filename = "./__events_test__.json"
    events_original = [
        Event("2010-01-10", "A normal title", ""),
        Event("2024-12-27", "àèìòùÈÉËÌÎÏÐÑÛþ", "Non-ASCII characters"),
        Event("2024-07-25", "    ", "    "),
    ]

    save_json(filename, events_original)
    events_loaded = load_json(filename)
    assert events_original == events_loaded

    os.remove(filename)
