import argparse
import httpx
import string
import smtplib
from email.mime.text import MIMEText

class WebAPI:

    async def send_api_request(self, endpoint, headers=None, params=None):
        headers = headers or {}
        headers['Authorization'] = f'Bearer {self.api_key}'
        async with httpx.AsyncClient() as client:
            response = await client.get(f'{self.url}/{endpoint}', headers=headers, params=params)
            return response

def main():
    parser = argparse.ArgumentParser(description="Send API requests")
    parser.add_argument("url", help="API URL")
    parser.add_argument("--header", nargs="*", help="Custom headers in key=value format")
    parser.add_argument("--param", nargs="*", help="Query parameters in key=value format")

    args = parser.parse_args()

    headers = {}
    if args.header:
        for header in args.header:
            key, value = header.split("=")
            headers[key] = value

    params = {}
    if args.param:
        for param in args.param:
            key, value = param.split("=")
            params[key] = value

    response = send_api_request(args.url, headers=headers, params=params)

    if response.status_code == 200:
        print("Response:")
        print(response.text)
    else:
        print(f"API request failed with status code {response.status_code}")

if __name__ == "__main__":
    main()
