import datetime as dt
from dataclasses import dataclass


@dataclass
class Event:
    date: str
    title: str
    notes: str = ""


def days_since(event: Event) -> int:
    date = dt.date.fromisoformat(event.date)
    date_today = dt.date.today()
    difference = date_today - date
    return difference.days
