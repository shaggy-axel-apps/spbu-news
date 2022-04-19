from typing import Generator, NamedTuple
from spbu_api import SpbuApi


class Division(NamedTuple):
    oid: int
    alias: str
    name: str


class StudyDivisionsApi(SpbuApi):
    def __init__(self):
        self.API = f"{self.API}study/divisions/"

    def get_all(self) -> Generator[Division, None, str]:
        response = self.send_query(self.API)
        if 200 < response.code and response.code < 400:
            for division in response.response:
                yield Division(
                    oid=division.get("Oid", None),
                    alias=division.get("Alias", None),
                    name=division.get("Name", None)
                )
        return response.status
