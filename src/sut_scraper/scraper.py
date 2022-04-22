from sut_scraper import BaseScraper
from sut_scraper.models import Division, Group


class Scraper(BaseScraper):
    def __init__(self):
        super().__init__()

    async def get_all_divisions(self):
        soup = await self.get_soup(self.BASE_URL)

        divisions = []
        for row in soup.find_all('div', class_="vt252"):
            alias = row.find('div', class_="vt253").text.strip()
            name = row.find('div', class_="vt254").text.strip()
            divisions.append(Division(alias=alias, name=name))
        return divisions

    async def get_all_groups(self, division_alias: str):
        soup = await self.get_soup(self.BASE_URL)

        groups = []
        for row in soup.find_all('div', class_='vt252'):
            if row.find('div', class_="vt253").text.strip() == division_alias:
                groups = [
                    Group(group_id=int(group.get('data-i')), name=group.get('data-nm'))
                    for group in row.find('div', class_="vt255").find_all('a')
                ]
                break
        return groups

