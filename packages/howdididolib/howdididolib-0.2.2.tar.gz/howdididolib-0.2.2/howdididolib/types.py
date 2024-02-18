"""Types for Howdidido integration."""
from dataclasses import dataclass
from datetime import date, datetime
from typing import TypeAlias, List


class Iterable:
    def __iter__(self):
        for attr in dir(self):
            if not attr.startswith("__"):
                yield attr


@dataclass
class BookedEvent(Iterable):
    event_datetime: datetime
    event_name: str
    players: list[str]


@dataclass
class BookableEvent(Iterable):
    event_date: date
    event_name: str
    book_from_datetime: datetime
    book_to_datetime: datetime


@dataclass
class Bookings:
    booked_events: list[BookedEvent]
    bookable_events: list[BookableEvent]


@dataclass
class Fixture(Iterable):
    event_date: date
    event_name: str
    competition_type: str
    event_description: str


Fixtures: TypeAlias = List[Fixture]
