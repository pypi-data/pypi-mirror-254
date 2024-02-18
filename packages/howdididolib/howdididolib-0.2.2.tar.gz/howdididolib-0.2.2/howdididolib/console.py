"""Console for Howdidido library."""
import argparse
import asyncio
import logging
import sys
import types

import aiohttp.client_exceptions
from tabulate import tabulate

from howdididolib.authentication import AuthenticationClient
from howdididolib.bookings import BookingClient
from howdididolib.const import TIMEOUT
from howdididolib.exceptions import InvalidAuth
from howdididolib.fixtures import FixtureClient

logging.basicConfig(format='%(levelname)s:%(name)s:%(asctime)s:%(message)s', datefmt='%d/%m/%Y %H:%M:%S')

logger = logging.getLogger(__name__)


def validate_username_password(in_args):
    """Enforce the condition that either both username and password are provided or neither"""
    if ((in_args.username is None and in_args.password is not None) or
        (in_args.username is not None and in_args.password is None)):
        return "--username and --password must be provided together or not at all"
    else:
        return None


async def main() -> int:
    # create parser
    parser = argparse.ArgumentParser(
        description='Get golf booking information from How Did I Do website (https://www.howdidido.com)')
    parser.add_argument("--username", help="Provide username", required=False)
    parser.add_argument("--password", help="Provide password", required=False)
    parser.add_argument("--save_auth", help="Save authentication cookie", default=True, action="store_true")
    parser.add_argument("--bookings", help="Get bookings", action="store_true")
    parser.add_argument("--fixtures", help="Get fixtures", action="store_true")
    parser.add_argument("--debug", help="Enable debug logging", action="store_true")
    args = parser.parse_args()

    # Validate username and password
    validation_error = validate_username_password(args)
    if validation_error:
        parser.error(validation_error)

    logging.getLogger().setLevel(logging.DEBUG if args.debug else logging.INFO)

    trace_config = aiohttp.TraceConfig()
    trace_config.on_request_start.append(log_request)
    trace_config.on_request_chunk_sent.append(log_request_chunk_sent)
    trace_config.on_request_end.append(log_response)

    session = aiohttp.ClientSession(
        timeout=aiohttp.ClientTimeout(total=TIMEOUT),
        trace_configs=[trace_config],
    )

    async with session:
        auth_client = AuthenticationClient(session, username=args.username, password=args.password)
        try:
            if args.username:
                logger.info(f"Getting authentication cookie using username: {args.username}")
                # when username & password is provided, always get auth cookie and save
                await auth_client.login()
                if args.save_auth:
                    logger.info("Saving authentication cookie")
                    await auth_client.save_auth_cookie()
            else:
                logger.info("Restoring authentication cookie")
                await auth_client.restore_auth_cookie()

            if args.bookings:
                booking_client = BookingClient(session)
                bookings = await booking_client.get()

                if len(bookings.booked_events) > 0:
                    print("\nBooked Events:\n")
                    print(tabulate(bookings.booked_events, headers="keys"))

                if len(bookings.bookable_events) > 0:
                    print("\nBookable Events:\n")
                    print(tabulate(bookings.bookable_events, headers="keys"))

            if args.fixtures:
                fixture_client = FixtureClient(session)
                fixtures = await fixture_client.get()

                if len(fixtures) > 0:
                    print("\nFixtures:\n")
                    print(tabulate(fixtures, headers="keys"))
        except (aiohttp.client_exceptions.ClientError, InvalidAuth) as e:
            logger.error(e)
            return 1  # Exit with an error level of 1
        else:
            return 0


async def log_request(
    session: aiohttp.ClientSession,
    trace_config_ctx: types.SimpleNamespace,
    params: aiohttp.tracing.TraceRequestStartParams,
) -> None:
    # Log request information before sending
    method = params.method
    url = params.url
    logging.debug(f"> {method} {url}")
    for k, v in params.headers.items():
        logging.debug("> %s: %s", k, v)


async def log_request_chunk_sent(
    session: aiohttp.ClientSession,
    trace_config_ctx: types.SimpleNamespace,
    params: aiohttp.tracing.TraceRequestChunkSentParams,
) -> None:
    # Log request information being sent
    logging.debug(f"> {params.chunk}")


async def log_response(
    session: aiohttp.ClientSession,
    trace_config_ctx: types.SimpleNamespace,
    params: aiohttp.tracing.TraceRequestEndParams,
) -> None:
    # Log response information after receiving
    method = params.response.method
    url = params.response.url
    status = params.response.status
    reason = params.response.reason
    body = await params.response.read()
    logging.debug(f"< {method} {url} {status} {reason}")
    for k, v in params.response.headers.items():
        logging.debug("< %s: %s", k, v)
    logging.debug("< %s", body)


if __name__ == '__main__':
    sys.exit(asyncio.run(main()))
