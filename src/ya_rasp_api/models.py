from typing import NamedTuple

from spbu_api.models import ApiResponse


class Station(NamedTuple):
    code: str
    title: str
    station_type: str
    lat: str
    lon: str
    distance: float


class Schedule(NamedTuple):
    arrival: str     # "2022-04-23T20:03:00+03:00" взять время
    departure: str     # "2022-04-23T20:03:00+03:00" взять время
    days: str
    is_fuzzy: bool
    title: str
    number: str
    transport_type: str


class IntervalSchedule(NamedTuple):
    title: str
    number: str
    transport_type: str
    interval: str
    end_time: str    # "2022-04-23T00:15:00" взять время
    begin_time: str  # "2022-04-23T06:15:00" взять время
    is_fuzzy: bool
    days: str


class StationTimeTable(NamedTuple):
    station: Station
    date: str        # "%Y-%m-%d"
    schedule: list[Schedule]
    interval_schedule: list[IntervalSchedule]


__all__ = [
    "ApiResponse", "Schedule", "IntervalSchedule",
    "StationTimeTable", "Station"
]
