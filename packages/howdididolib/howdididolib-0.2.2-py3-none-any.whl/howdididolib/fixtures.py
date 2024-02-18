"""Authentication for Howdidido integration."""

import logging
from datetime import datetime

import aiohttp
import bs4

from howdididolib.const import HOME_CLUB_URL, USER_AGENT, BASE_URL
from howdididolib.types import Fixture, Fixtures

logger = logging.getLogger(__name__)


class FixtureClient:
    def __init__(
        self,
        session: aiohttp.ClientSession,
        fixture_url: str = None
    ):
        self.session = session
        self.fixture_url = fixture_url

    async def get(self) -> Fixtures:
        """Get fixtures"""
        if not self.fixture_url:
            self.fixture_url = await self._get_fixture_url()

        async with self.session.get(
            f"{BASE_URL}{self.fixture_url}",
            headers={
                "user-agent": USER_AGENT,
            },
        ) as resp:
            resp.raise_for_status()
            soup = bs4.BeautifulSoup(await resp.text(), "html5lib")

        table = soup.find("table", attrs={"class": "table"})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')

        fixture_events = []

        for row in rows:
            cols = row.find_all('td')
            event_date, event_name, competition_type, event_description = cols

            fixture_events.append(
                Fixture(
                    event_date=datetime.strptime(event_date.text.strip(), "%d/%m/%Y").date(),
                    event_name=event_name.text.strip(),
                    competition_type=competition_type.text.strip(),
                    event_description=event_description.a["data-description"].strip()
                )
            )

        return fixture_events

    async def _get_fixture_url(self) -> str:
        """Get fixture URL"""

        async with self.session.get(
            HOME_CLUB_URL,
            headers={
                "user-agent": USER_AGENT,
            },
        ) as resp:
            resp.raise_for_status()
            soup = bs4.BeautifulSoup(await resp.text(), "html5lib")

        """
        Find fixture path

        <div class="panel-footer hidden-xs hidden-sm">
            <a href="/My/Fixtures?sectionId=9999">View upcoming Fixtures</a>
        </div>
        """
        # Search by text with the help of lambda function
        fixture_link = soup.find(lambda tag: tag.name == "a" and "View upcoming Fixtures" in tag.text)

        return fixture_link['href'] if fixture_link else None
