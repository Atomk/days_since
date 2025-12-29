import json
import datetime as dt
from dataclasses import dataclass, asdict


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


def save_json(filename, events: list[Event]):
    """Save a list of event objects to a JSON file.

    `filename` is the path to the JSON file.
    If the specified file already exists, it will be overwritten.
    """
    export = []
    if not events:
        print("No events to export")
        return
    for event in events:
        export.append(asdict(event))
    # By default non-ASCII characters are converted to their respective
    # codepoint representation, but if would make the JSON unreadable for
    # non-English languages
    string = json.dumps(export, ensure_ascii=False)
    with open(filename, "w", encoding="utf-8") as fhl:
        fhl.write(string)
    print(f"{len(export)} events saved to file '{filename}'")


def load_json(filename) -> list[Event]:
    with open(filename, encoding="utf-8") as fhl:
        imported = json.load(fhl)
    events = []
    for event_dict in imported:
        events.append(Event(**event_dict))
    print(f"{len(events)} events imported from file '{filename}'")
    return events
