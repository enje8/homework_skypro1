import requests

BASE_URL = "https://yougile.com/api-v2"
API_TOKEN = ""


class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json"
        }

    def post(self, endpoint, payload=None):
        return requests.post(self.base_url + endpoint, json=payload, headers=self.headers)

    def put(self, endpoint, payload=None):
        return requests.put(self.base_url + endpoint, json=payload, headers=self.headers)

    def get(self, endpoint):
        return requests.get(self.base_url + endpoint, headers=self.headers)