"""Authentication for Howdidido integration."""

import logging
from typing import cast

import aiohttp
import bs4

from howdididolib.const import DEFAULT_AUTH_COOKIE_FILE
from howdididolib.const import LOGIN_URL, BASE_URL, AUTH_COOKIE_NAME
from howdididolib.const import USER_AGENT
from howdididolib.exceptions import InvalidAuth

logger = logging.getLogger(__name__)


class AuthenticationClient:
    def __init__(
        self,
        session: aiohttp.ClientSession,
        username: str = None,
        password: str = None,
        auth_cookie_filename: str = DEFAULT_AUTH_COOKIE_FILE,
    ):
        self.session = session
        self.username = username
        self.password = password
        self.auth_cookie_filename = auth_cookie_filename

    async def login(self, persistent: bool = True):
        """Login using _username and _password via form to obtain authentication cookie"""

        async with self.session.get(
            LOGIN_URL,
            headers={
                "user-agent": USER_AGENT,
            },
        ) as resp:
            resp.raise_for_status()
            soup = bs4.BeautifulSoup(await resp.text(), "html5lib")

        # find login form
        login_div = soup.find(name="div", id="login-control")
        login_form = login_div.find(name="form")
        login_form_action = login_form.get("action")

        # Create a dictionary to store form data
        form_data = {}

        # Iterate over input elements within the form
        for input_element in login_form.find_all('input'):
            # Get the name and value attributes
            input_name = input_element.get('name')
            input_value = input_element.get('value')

            # Skip elements without a name attribute
            if input_name is not None:
                # Use a case statement to set different values for specific input names
                if input_name.lower() == 'username':
                    input_value = f'{self.username}'
                elif input_name.lower() == 'password':
                    input_value = f'{self.password}'
                elif input_name.lower() == 'rememberme':
                    if persistent:
                        input_value = ["true", "false"]
                    else:
                        input_value = "false"

                # Add the name and value to the form_data dictionary
                form_data[input_name] = input_value

        logger.debug("login form data: %s", form_data)

        async with self.session.post(
            f"{BASE_URL}{login_form_action}",
            headers={
                "user-agent": USER_AGENT,
                "Origin": BASE_URL,
                "Referer": login_form_action
            },
            data=form_data,
            allow_redirects=False,
        ) as resp:
            resp.raise_for_status()

        # check for authentication cookie
        filtered = self.session.cookie_jar.filter_cookies(BASE_URL)
        auth_cookie = filtered.get(AUTH_COOKIE_NAME)
        if not auth_cookie:
            raise InvalidAuth("Authentication failed: check username and password")

    async def save_auth_cookie(self):
        """save session auth cookie to file"""
        # only store the auth cookie
        cast(aiohttp.CookieJar, self.session.cookie_jar).save(file_path=self.auth_cookie_filename)

    async def restore_auth_cookie(self):
        """restore session auth cookie from file"""
        try:
            # Load existing cookie from the file (if any)
            cast(aiohttp.CookieJar, self.session.cookie_jar).load(file_path=self.auth_cookie_filename)

            # check for authentication cookie
            filtered = self.session.cookie_jar.filter_cookies(BASE_URL)
            auth_cookie = filtered.get(AUTH_COOKIE_NAME)
            if not auth_cookie:
                raise InvalidAuth("Authentication cookie not found: userpass authentication is required")

            return True
        except FileNotFoundError:
            raise InvalidAuth("Authentication cookie file not found")
