import requests


class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get(self, endpoint: str, params: dict | None = None):
        return requests.get(f"{self.base_url}{endpoint}", params=params)

    def post(self, endpoint: str, data: dict):
        return requests.post(f"{self.base_url}{endpoint}", json=data)

    def put(self, endpoint: str, data: dict):
        return requests.put(f"{self.base_url}{endpoint}", json=data)

    def delete(self, endpoint: str):
        return requests.delete(f"{self.base_url}{endpoint}")
