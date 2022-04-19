from typing import NamedTuple, Optional, Union

import requests as req
from requests.models import Response
from requests.status_codes import codes
from requests.structures import LookupDict

from settings.const import SPBU_API


codes: LookupDict


class ApiResponse(NamedTuple):
    code: int
    status: str
    response: Optional[Union[Response, list[dict], dict, str]]


class SpbuApi:
    def __init__(self):
        self.API = SPBU_API

    def send_query(self, api: str, **params) -> ApiResponse:
        response = req.get(api.format(**params))
        return ApiResponse(
            code=response.status_code,
            status=codes.get(response.status_code, ("unknown",))[0],
            response=response.json()
        )
