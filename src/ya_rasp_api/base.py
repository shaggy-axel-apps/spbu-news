import aiohttp

from settings.const import YANDEX_API_KEY, YANDEX_API
from ya_rasp_api.models import ApiResponse


class BaseYandexApi:
    def __init__(self):
        self.API = YANDEX_API
        self.KEY = YANDEX_API_KEY

    async def send_query(self, api: str, **params) -> ApiResponse:
        async with aiohttp.ClientSession() as session:
            response = await session.get(api.format(
                **params, base_api=self.API, api_key=self.KEY
            ))
        response = await response.json()
        return response
