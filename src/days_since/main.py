from events import Event, days_since


EVENTS = [
    Event("2010-01-10", "Our doggo joined the lobby", ""),
    Event("2024-12-27", "New phone", "My friends gifted me a Fairphone"),
    Event("2024-07-25", "Last time I ate sushi", ""),
]


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
    print_events(EVENTS)
