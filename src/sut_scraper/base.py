import aiohttp
from bs4 import BeautifulSoup as BS

from settings.const import SUT_URL, SUT_HEADERS
from sut_scraper.models import ApiResponse


class BaseScraper:
    def __init__(self):
        self.BASE_URL = SUT_URL
        self.HEADERS = SUT_HEADERS

    async def get_soup(self, url: str, **params) -> ApiResponse:
        """ Get html page using response from request to `url` """
        async with aiohttp.ClientSession() as session:
            response = await session.get(url.format(**params), headers=self.HEADERS)
            text = await response.text()
            soup = BS(text, 'lxml')
        return soup
