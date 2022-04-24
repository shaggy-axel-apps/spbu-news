from typing import NamedTuple

from bs4 import BeautifulSoup


class ApiResponse(NamedTuple):
    code: int
    status: str
    soup: BeautifulSoup


class Group(NamedTuple):
    group_id: int
    name: str


class Division(NamedTuple):
    alias: str
    name: str


class Event(NamedTuple):
    subject: str
    educator: str
    classroom: str
    reason: str
    time: str


class EventDay(NamedTuple):
    events: list[Event]
    day: str
    week_day: int
    group_id: int
