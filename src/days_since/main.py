from typing import Literal

from events import (
    Event,
    days_since,
    delta_since,
    load_json
)


EVENTS_FILE = "./data/events.json"


def print_events(events: list[Event], mode: Literal["days", "delta"]):
    if not events:
        print("No events to print")
        return

    # Find the length of the longest title to use it later for alignment
    max_len = -1
    for event in events:
        if len(event.title) > max_len:
            max_len = len(event.title)

    # The alignment line will always be at least this long
    minimum_dashes_count = 2
    for event in events:
        try:
            elapsed = days_since(event)
        except ValueError:
            print(f"Error in event: '{event.title}'. Invalid date")
            continue
        if elapsed < 0:
            print(f"Error in event: '{event.title}'. Date is in the future!")
            continue
        dashes_count = (max_len - len(event.title)) + minimum_dashes_count
        line = "-" * dashes_count
        if mode == "days":
            print(f"{event.title} {line} {elapsed} days ago")
        elif mode == "delta":
            print(f"{event.title} {line} " + delta_since(event))
        else:
            raise ValueError(f"unexpected 'mode' value: {mode}")


if __name__ == "__main__":
    events = load_json(EVENTS_FILE)
    print_events(events, "delta")
