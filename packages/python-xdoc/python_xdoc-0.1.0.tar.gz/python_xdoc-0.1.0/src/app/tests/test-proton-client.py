import os
import httpx
import argparse
import sys

from proton.api import Session, ProtonError

class ProtonMailClient:
    def __init__(self, endpoint, username, password, headers=None, params=None):
        self.session = Session(
            api_url=self.endpoint,
            appversion=None,
            user_agent=None,
            TLSPinning=False
            )

        try:
            self.session.authenticate(username, password)
        except ProtonError as error:
            print(f"Authentication failed: {error}")

    async def authenticate(self, username, password):
        error_message = {
            8002: "Provided password is incorrect",
            10002: "Account is deleted",
            10003: "Account is disabled",
        }
        try:
            self['session'].authenticate(username, password)
        except ProtonError as e:
            print(error_message.get(e.code, "Unknown error"))

    async def send_email(self, to, subject, body, endpoint):
        error_message = {
            401: "Invalid access token, client should refresh tokens",
            403: "Missing scopes, client should re-authenticate",
            429: "Too many requests, client needs to retry after specified in headers",
            503: "API is unreacheable",
            10013: "Refresh token is invalid. Client should re-authenticate (logout and login)",
        }

        params = {
            'endpoint': endpoint,
            'method': 'post',
            'data': {'to': to, 'subject': subject, 'body': body}
        }

        try:
            response = await self.session.api_request(**params)
            return response

        except ProtonError as e:
            print(error_message.get(e.code, "Unknown error"))

    async def receive_email(self, endpoint):
        error_message = {
            401: "Invalid access token, client should refresh tokens",
            403: "Missing scopes, client should re-authenticate",
            429: "Too many requests, client needs to retry after specified in headers",
            503: "API is unreacheable",
            10013: "Refresh token is invalid. Client should re-authenticate (logout and login)",
        }

        params = {
            'endpoint': endpoint,
            'method': 'get',
            'data': {'to': to, 'subject': subject, 'body': body}
        }

        try:
            response = await self.session.api_request(**params)
            return response

        except ProtonError as e:
            print(error_message.get(e.code, "Unknown error"))

    async def save_session(self):
        session_dump = self['session'].dump()
        print(session_dump)

    async def load_session(self, session_dump):
        with open(self['session'], "r") as f:
            session_in_json_format = json.loads(f.read())

            self['session'] = Session.load(
                dump=session_in_json_format
            )

    async def refresh_session(self):
        try:
            self['session'].refresh()
        except ProtonError as e:
            if e.code == 401:
                proton_session.refresh()
                print("Now we can retry making another API call since tokens have been refreshed")

def main():
    '''
    Example usage:
    set -x PROTON_API_KEY "..."
    set -x PROTON_USERNAME "..."
    set -x PROTON_PASS "..."
    python test-proton-client.py
    '''

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "ProtonMail API Python Client"
    }

    params = {
        "limit": 10,
    }

    parser = argparse.ArgumentParser(description="Send API requests")
    parser.add_argument("--endpoint", default="https://api.protonmail.ch/api/v1/messages",  help="API endpoint URL")
    parser.add_argument("--api_key", defaut=os.getenv('PROTON_USERNAME', None), help="API Key")
    parser.add_argument("--username", defaut=os.getenv('PROTON_USERNAME', None), help="username")
    parser.add_argument("--password", defaut=os.getenv('PROTON_PASS', None), help="password")
    parser.add_argument("--header", nargs="*", help="Custom headers in key=value format")
    parser.add_argument("--param", nargs="*", help="Query parameters in key=value format")

    args = parser.parse_args()

    if args.header:
        for header in args.header:
            key, value = header.split("=")
            headers[key] = value

    if args.param:
        for param in args.param:
            key, value = param.split("=")
            params[key] = value

    if args.api_key or (args.username and args.password):
        auth_info = args.api_key if args.api_key else Tuple(args.username, args.password)

        api = ProtonMailClient(args.endpoint, auth_info, headers=headers, params=params)

        response = client.send_email('recipient@example.com', 'Hello', 'This is a test email.', 'custom_api_endpoint')

        if response.status_code == 200:
            print("Response:")
            print(response.text)
            with open('response.txt', 'w') as f:
                f.write(response.text)
        else:
            print(f"API request failed with status code {response.status_code}")
    else:
        print("API key or username and password are required")


if __name__ == "__main__":
    main()
