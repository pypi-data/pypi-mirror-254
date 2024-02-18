"""Constants for Howdidido library."""

BASE_URL = "https://www.howdidido.com"
LOGIN_URL = f"{BASE_URL}/Account/Login"
BOOKING_URL = f"{BASE_URL}/Booking"
HOME_CLUB_URL = f"{BASE_URL}/My/Club"
FIXTURES_PATH = "/My/Fixtures"

AUTH_COOKIE_NAME = ".ASPXAUTH"
DEFAULT_AUTH_COOKIE_FILE = "howdidido_auth_cookie.dat"

# Windows 10-based PC using Edge browser
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'

TIMEOUT = 30
