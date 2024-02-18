import requests

class APIWrapper:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        response = requests.get(self.base_url + endpoint)
        return response.json()

    def post(self, endpoint, data):
        response = requests.post(self.base_url + endpoint, data=data)
        return response.json()