"""Authentication for Howdidido integration."""

import logging
from datetime import datetime, timedelta

import aiohttp
import bs4

from howdididolib.const import BOOKING_URL, USER_AGENT
from howdididolib.types import BookedEvent, BookableEvent, Bookings

logger = logging.getLogger(__name__)


class BookingClient:
    def __init__(
        self,
        session: aiohttp.ClientSession,
    ):
        self.session = session

    async def get(self) -> Bookings:
        """Get bookings"""

        async with self.session.get(
            BOOKING_URL,
            headers={
                "user-agent": USER_AGENT,
            },
        ) as resp:
            resp.raise_for_status()
            soup = bs4.BeautifulSoup(await resp.text(), "html5lib")

        booked_events = []
        bookable_events = []

        # find booking div
        upcoming_booking_div = soup.find(name="div", id="upcoming-bookings-container")
        if upcoming_booking_div:
            bookings = upcoming_booking_div.find_all(name="div", class_="cb")
            for booking in bookings:
                """
                Extract booking details

                <div class="cb">
                    <div class="date-time theme_bg">
                        <div class="wday">Sun</div>
                        <div class="date">21 Jan</div>
                        <div class="time">09:16</div>
                    </div>
                    <div class="info">
                        <div class="name">
                            <a href="..." target="_blank" class="theme_hover_text">Men's January Stableford 2</a>
                        </div>
                        <div class="players">
                            <div class="player col-xs-12 col-sm-6">
                                <span class="pos">P1</span>
                                <span>JOHN SMITH</span>
                            </div>
                            <div class="player col-xs-12 col-sm-6">
                                <span class="pos">P2</span>
                                <span>JOHNNY WALKER</span>
                            </div>
                            <div class="player col-xs-12 col-sm-6">
                                <span class="pos">P3</span>
                                <span>DAVID PALMER</span>
                            </div>
                        </div>
                        <!-- other elements omitted for brevity -->
                    </div>
                </div>
                """
                event_date_str = booking.find('div', class_='date').text
                event_time_str = booking.find('div', class_='time').text

                # Convert date string to Python date object
                event_date_str = _format_date_string(event_date_str)
                event_datetime = datetime.strptime(
                    f'{event_date_str} {datetime.today().year} {event_time_str}',
                    "%d %m %Y %H:%M"
                )

                # Check if the input_date is in the past
                if event_datetime < datetime.now():
                    # Add a year to the input_date
                    event_datetime += timedelta(days=365)

                # Extract the name of the booking
                event_name = booking.find('div', class_='name').a.text.strip()

                # Extract a list of player names
                players = booking.find_all('div', class_='player')
                players_names = [player.find_all('span')[1].text.strip() for player in players]

                logger.debug("booked_event: event_datetime: %s, event_name: %s, players: %s", event_datetime,
                             event_name,
                             players_names)

                booked_events.append(BookedEvent(event_datetime, event_name, players_names))

        # find booking div
        comp_booking_div = soup.find(name="div", id="comp-booking-selector")
        if comp_booking_div:
            bookings = comp_booking_div.find_all(name="div", class_="cb")
            for booking in bookings:
                """
                Extract booking details

                <div class="cb" >
                    <div class="date-time theme_bg">
                        <div class="wday">Sun</div>
                        <div class="date">21 Jan</div>
                        <div class="time"></div>
                    </div>
                    <div class="info">
                        <div class="name">
                            <a href="..." class="theme_hover_text">
                                <i class="fa fa-trophy"></i><span>Men's January Stableford 2</span>
                            </a>
                        </div>
                        <div class="comp-info">
                            <div class="book-from-until">
                                <div class="from">
                                    <span class="lbl-from">Book From</span>
                                    <span class="val">25th Dec 2023 07:00</span>
                                </div>
                                <div class="to">
                                    <span class="lbl-to">To</span>
                                    <span class="val">19th Jan 2024 18:00</span>
                                </div>
                            </div>
                        </div>
                        <!-- other elements omitted for brevity -->
                        </div>
                    </div>
                </div>
                """
                event_date_str = booking.find('div', class_='date').text

                # Convert date string to Python date object
                event_date_str = _format_date_string(event_date_str)
                event_date = datetime.strptime(f'{event_date_str} {datetime.today().year}', "%d %m %Y").date()

                # Check if the input_date is in the past
                if event_date < datetime.now().date():
                    # Add a year to the input_date
                    event_date += timedelta(days=365)

                # Extract the name of the booking
                event_name = booking.find('div', class_='name').a.text.strip()

                book_from_div = booking.find('div', class_='book-from-until')

                book_from_datetime_str = book_from_div.find('div', class_='from').find("span", class_="val").text
                book_to_datetime_str = book_from_div.find('div', class_='to').find("span", class_="val").text

                book_from_datetime_str = _format_date_string(book_from_datetime_str)
                book_to_datetime_str = _format_date_string(book_to_datetime_str)

                book_from_datetime = datetime.strptime(book_from_datetime_str, "%d %m %Y %H:%M")
                book_to_datetime = datetime.strptime(book_to_datetime_str, "%d %m %Y %H:%M")

                logger.debug(
                    "bookable_events: event_date: %s, event_name: %s, book_from_datetime: %s, book_to_datetime: %s",
                    event_date, event_name, book_from_datetime, book_to_datetime)

                bookable_events.append(BookableEvent(event_date, event_name, book_from_datetime, book_to_datetime))

        return Bookings(booked_events, bookable_events)


def _format_date_string(s: str) -> str:
    """Reformat hdid bookings string date format, to make string conversion to python datetime easier"""
    replacements = [['Jan', '01'], ['Feb', '02'], ['Mar', '03'], ['Apr', '04'], ['May', '05'], ['Jun', '06'],
                    ['Jul', '07'], ['Aug', '08'], ['Sep', '09'], ['Oct', '10'], ['Nov', '11'], ['Dec', '12'],
                    ['st', ''], ['nd', ''], ['rd', ''], ['th', '']]

    for elem in replacements:
        s = s.replace(elem[0], elem[1])

    return s
