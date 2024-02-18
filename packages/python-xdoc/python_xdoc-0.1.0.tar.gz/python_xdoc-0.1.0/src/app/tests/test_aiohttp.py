import pytest
import aiohttp
import asyncio
import json

pytestmark = pytest.mark.asyncio

class API:
    def __init__(self, base_url, api_key=None, auth_user=None):
        self.base_url = base_url
        self.api_key = api_key
        self.auth_user = auth_user

    async def get(self, endpoint):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url + endpoint) as response:
                if response.status != 200:
                    raise Exception(f"Request failed with status {response.status}")
                return await response.json()

    async def post(self, endpoint, data, custom_headers=None):
        all_headers = {'Authorization': 'Bearer ' + self.api_key} if self.api_key else {}
        if custom_headers:
            all_headers.update(custom_headers)

        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url + endpoint, headers=all_headers, data=json.dumps(data)) as response:
                if response.status != 200:
                    raise Exception(f"Request failed with status {response.status}")
                return await response.json()

class Email:
    def __init__(self, url, api_key, auth_user):
        self.api = API(url, api_key, auth_user)

    async def send_email(self, endpoint, data):
        headers = {'Authorization': 'Bearer ' + self.api.api_key} if self.api.api_key else {}
        data.update({"apiKey": self.api.api_key, "authUser": self.api.auth_user})
        response = await self.api.post(endpoint, data, custom_headers=headers)
        return response

@pytest.mark.asyncio
async def test_send_email():
    endpoint = 'https://service.5ymail.com/api'
    email = Email(endpoint, 'your_api_key', 'your_auth_user')
    data = {
        'toEmail': 'test@example.com',
        'subject': 'Test Email',
        'content': 'This is a test email.',
        'lang': 'en',
        'html_content': True,
        'fromEmail': 'sender@example.com',
        'ccEmail': 'cc@example.com',
        'bccEmail': 'bcc@example.com',
        'fromName': 'Sender Name',
        'replyEmail': 'reply@example.com',
        'replyName': 'Reply Name',
        'xMailer': 'Custom X-Mailer',
        'header1': 'Custom Header 1',
        'header2': 'Custom Header 2',
        'serverLocation': 'asia'
    }
    response = await email.send_email('/http', data)
    assert response['status'] == 'success'
