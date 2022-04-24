from datetime import datetime

from ya_rasp_api.base import BaseYandexApi
from ya_rasp_api.models import Station, Schedule, StationTimeTable, IntervalSchedule


class YandexRaspisanieApi(BaseYandexApi):
    """ ... """
    async def get_nearest_stations(self, lat, lon) -> list[Station]:
        api = (
            "{base_api}/nearest_stations/"
            "?apikey={api_key}&lat={lat}&lng={lng}"
            "&distance=5&lang=ru_RU"
        )
        response: dict = await self.send_query(api, lat=lat, lng=lon)
        try:
            stations = response['stations']
        except KeyError:
            assert False, response['error']

        result_stations: list[Station] = []
        for station in stations:
            result_stations.append(Station(
                code=station["code"],
                title=station['popular_title'],
                station_type=station['station_type'],
                lat=station['lat'],
                lon=station['lng'],
                distance=round(station['distance'] * 1000, 2)
            ))
        return result_stations

    async def parse_station_schedule(self, station: Station) -> StationTimeTable:
        api = (
            "{base_api}?apikey={api_key}&station={code}"
            f"&date={datetime.today():%Y-%m-%d}"
        )
        response = await self.send_query(api, code=station.code)
        response = await response.response
        return StationTimeTable(
            station=station, date=f"{datetime.today():%Y-%m-%d}",
            schedule=[
                Schedule(
                    arrival=schedule["arrival"],
                    departure=schedule["departure"],
                    days=schedule["days"],
                    is_fuzzy=schedule["is_fuzzy"],
                    title=schedule["thread"]["title"],
                    number=schedule["thread"]["number"],
                    transport_type=schedule["thread"]["transport_type"]
                ) for schedule in response['schedule']
            ],
            interval_schedule=[
                IntervalSchedule(
                    title=schedule["thread"]["title"],
                    number=schedule["thread"]["number"],
                    transport_type=schedule["thread"]["transport_type"],
                    interval=schedule["thread"]["interval"]["density"],
                    end_time=schedule["thread"]["interval"]["end_time"],
                    begin_time=schedule["thread"]["interval"]["begin_time"],
                    days=schedule["days"],
                    is_fuzzy=schedule["is_fuzzy"]
                ) for schedule in response['interval_schedule']
            ]
        )
