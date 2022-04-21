import aiohttp

from settings.const import SPBU_API
from spbu_api.models import ApiResponse


class SpbuApi:
    def __init__(self):
        self.API = SPBU_API

    async def send_query(self, api: str, **params) -> ApiResponse:
        async with aiohttp.ClientSession() as session:
            response = await session.get(api.format(**params))
            return ApiResponse(
                code=response.status,
                status=response.reason,
                response=response.json()
            )
