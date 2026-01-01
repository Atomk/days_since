"""
Entry point for the program when run in a terminal.

This script is intended to handle only the CLI, so it's not subject to
PyScript or MicroPython limitations.
"""

import argparse
from enum import StrEnum

from events import (
    Event,
    days_since,
    delta_since,
    load_json
)


class PrintMode(StrEnum):
    date = "date"
    days = "days"
    delta = "delta"


def print_events(events: list[Event], mode: PrintMode):
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
        if mode == PrintMode.days:
            print(f"{event.title} {line} {elapsed} days ago")
        elif mode == PrintMode.delta:
            print(f"{event.title} {line} " + delta_since(event))
        elif mode == PrintMode.date:
            print(f"{event.title} {line} {event.date}")
        else:
            raise ValueError(f"unexpected 'mode' value: {mode}")


def parse_arguments():
    # TODO use package name and description from the TOML file
    parser = argparse.ArgumentParser(
        prog="Days Since",
        description="A simple program to show time elapsed since past events.",
    )
    parser.add_argument(
        "--mode",
        type=PrintMode,
        choices=list(PrintMode),
        default=PrintMode.delta,
        help="change how to display the date of each event",
    )

    args = parser.parse_args()
    return args.mode


if __name__ == "__main__":
    print_mode = parse_arguments()

    try:
        events = load_json("./data/events.json")
    except FileNotFoundError:
        print("ERROR: no `events.json` found")
        print("Falling back to the sample file")
        events = load_json("./data/events_sample.json")
    print_events(events, print_mode)
