from httpx import AsyncClient


class PlayApiService:
    def __init__(self, http: AsyncClient):
        self.http = http
