#!/usr/bin/env python3
"""Execute AWS SSO auth tasks."""
import boto3
import json
import os.path
import glob
import webbrowser
import argparse
import time


__version__ = '2024.1.0.0'


class FailedToGetFileException(Exception):
    """Raise when the JSON cache fails file check."""

    pass


class InvalidTimeoutException(Exception):
    """Raise when the timeout value is not a positive integer."""

    pass


def createclient(
    client_name: str,
    client_type: str = 'public',
    region: str = 'us-east-1'
) -> dict:
    """
    Create SSO client for authorization.

    return dict
    """
    # Create client.
    sso_oidc = boto3.client(
        'sso-oidc',
        region_name=region
    )

    # Register client.
    response = sso_oidc.register_client(
        clientName=client_name,
        clientType=client_type
        # scopes=[
        #     'string',
        # ]
    )

    return response


def startauth(
    client_id: str,
    client_secret: str,
    start_url: str,
    region: str = 'us-east-1'
) -> dict:
    """
    Start SSO authorization process.

    return dict
    """
    # Create client.
    sso_oidc = boto3.client(
        'sso-oidc',
        region_name=region
    )

    # Start authentication process.
    return sso_oidc.start_device_authorization(
        clientId=client_id,
        clientSecret=client_secret,
        startUrl=start_url
    )


def getclienttoken(
    client_id: str,
    client_secret: str,
    device_code: str,
    grant_type: str = 'urn:ietf:params:oauth:grant-type:device_code',
    region: str = 'us-east-1'
) -> dict:
    """
    Get SSO Access Token from client authorization (recommended).

    Supports grant types for authorization code,
    refresh token, and device code requests.

    return dict
    """
    # Create client.
    sso_oidc = boto3.client(
        'sso-oidc',
        region_name=region
    )

    # Get tokens.
    return sso_oidc.create_token(
        clientId=client_id,
        clientSecret=client_secret,
        grantType=grant_type,
        deviceCode=device_code
    )


def getjsontoken(
    json_cache: str = None
) -> dict:
    """
    Get SSO Access Token from SSO JSON cache.

    If an SSO JSON cache file is specified, use it. Otherwise, use the
    newest ".json" file in "~/.aws/sso/cache/".

    Login to SSO using AWSCLI if token doesn't exist or has expired.
    Command: aws sso login [--profile <your-SSO-profile-if-not-default>]

    return dict
    """
    # Expand home directory if specified witha tilde.
    home = os.path.expanduser("~")

    # Get JSON cache file from argument or from default location.
    try:
        assert json_cache is not None
        if json_cache.startswith('~'):
            json_cache = json_cache.replace('~', home)
    except Exception as e:
        list_of_files = glob.glob(f'{home}/.aws/sso/cache/*.json')
        json_cache = max(list_of_files, key=os.path.getctime)

    # Raise exception if specified JSON cache file
    # is not a file or does not exist.
    if not os.path.isfile(json_cache):
        raise FailedToGetFileException(
            'Failed to get JSON cache file.'
        )

    # Get Access Token and expiry from JSON cache.
    with open(json_cache, 'r') as f:
        response = json.load(f)

    return response


def gettoken(
    start_url: str,
    client_name: str = 'ssoclient',
    region: str = 'us-east-1',
    timeout: int = 30
) -> dict:
    """
    Get SSO Access Token using getclienttoken.

    Run the full process:
    1. createclient
    2. startauth
    3. getclienttoken

    return dict
    """
    # Check timeout data type and value.
    if not isinstance(timeout, int) or timeout < 0:
        raise InvalidTimeoutException(
            'Expecting a positive integer for timeout.'
        )

    # Create authorization client.
    response_create = createclient(
        client_name,
        region=region
    )

    # Start client authorization process.
    response_start = startauth(
        response_create['clientId'],
        response_create['clientSecret'],
        start_url,
        region=region
    )

    print(
        f'Verification URI: {response_start["verificationUriComplete"]}'
    )

    # Open web browser for authentication.
    response_web = webbrowser.open(
        response_start['verificationUriComplete'],
        new=2,
        autoraise=True
    )

    # Try and retry to get Access Token
    # while browser authentication is running.
    # Fail after 10 tries.
    get_counter = 0
    while True:
        try:
            assert get_counter <= timeout
            response = getclienttoken(
                response_create['clientId'],
                response_create['clientSecret'],
                response_start['deviceCode'],
                region=region
            )
            break
        except Exception as e:
            time.sleep(1)
            get_counter += 1
            if get_counter > timeout:
                break

    try:
        response
        print('Access Token retrieval successful.')
        return response
    except Exception as e:
        print('Request failed.')
        return {
            'message': (
                f'Failed to get Access Token after {timeout} tries.'
            )
        }


def get_params():
    """Get parameters from script inputs."""
    myparser = argparse.ArgumentParser(
        add_help=True,
        allow_abbrev=False,
        description="Execute AWS SSO auth tasks.",
        usage="%(prog)s [options]",
    )
    myparser.add_argument(
        "-v", "--version", action="version", version="%(prog)s 2024.1.0.0"
    )
    myparser.add_argument(
        "-u",
        "--sso_url",
        action="store",
        help="AWS SSO login URL.",
        required=True,
        type=str,
    )
    myparser.add_argument(
        "-c",
        "--client_name",
        action="store",
        help="AWS SSO client name.",
        nargs="?",
        default="ssoclielnt",
        required=False,
        type=str,
    )
    myparser.add_argument(
        "-r",
        "--region",
        action="store",
        help="AWS SSO region.",
        nargs="?",
        default="us-east-1",
        required=False,
        type=str,
    )
    myparser.add_argument(
        "-t",
        "--timeout",
        action="store",
        help="Login attempt timeout duration in seconds.",
        nargs="?",
        default=30,
        required=False,
        type=str,
    )
    return myparser.parse_args()


def main():
    """Execute module as a script for testing purposes."""
    response = gettoken(get_params().sso_url)
    print({"access_token": response['accessToken']})
