from datetime import datetime

from bs4 import BeautifulSoup
from sut_scraper import BaseScraper
from sut_scraper.models import Division, Event, EventDay, Group


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

    async def get_groups(self, division_alias: str):
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

    async def get_timetable(self, group_id: int, day: str):
        soup: BeautifulSoup = await self.get_soup(f"{self.BASE_URL}?group={group_id}&date={day}")
        week_day = datetime.weekday(datetime.strptime(day, "%Y-%m-%d")) + 1

        events = []
        for event in soup.find_all('div', class_=f"rasp-day{week_day}"):
            if not event.text:
                continue
            subject = event.find('div', class_="vt240").text.strip()
            educator = event.find('div', class_="vt241").text.strip()
            time = event.find_previous('div', class_="vt244").find('div', class_="vt239")
            time = time.text.removeprefix(time.find('div', class_="vt283").text).strip()
            time = f"{time[:5]} - {time[5:]}"

            try:
                classroom = event.find('div', class_="vt242").text.strip()
            except AttributeError:
                classroom = "Unknown :("
            reason = event.find('div', class_="vt243").text.strip()

            events.append(Event(
                subject=subject, educator=educator,
                classroom=classroom, reason=reason,
                time=time
            ))

        return EventDay(events=events, group_id=group_id, day=day, week_day=week_day)
