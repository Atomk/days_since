from events import (
    Event,
    days_since,
    load_json
)


EVENTS_FILE = "./data/events_sample.json"


def print_events(events: list[Event]):
    for event in events:
        try:
            elapsed = days_since(event)
        except ValueError:
            print(f"Error in event: '{event.title}'. Invalid date")
            continue
        if elapsed < 0:
            print(f"Error in event: '{event.title}'. Date is in the future!")
            continue
        print(f"{event.title} -- {elapsed} days ago")


if __name__ == "__main__":
    events = load_json(EVENTS_FILE)
    print_events(events)
