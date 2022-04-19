# docs: https://yandex.ru/dev/rasp/doc/reference/schedule-point-point.html

QUERY = """
https://api.rasp.yandex.net/v3.0/search/?
from={FROM}
&to={TO}
&[format={FORMAT}]
&[lang={LANG}]
&[apikey={API_KEY}]
&[date={DATE}]
&[transport_types={TRANSPORT_TYPES}]
&[system={SYSTEM}]
&[show_systems={SHOW_SYSTEMS}]
&[offset={OFFSET}]
&[limit={LIMIT}]
&[add_days_mask={ADD_DAYS_MASK}]
&[result_timezone={TIMEZONE}]
&[transfers={TRANSFERS}]
"""

# REQUIRED PARAMETRS
FROM = ""             # <код станции отправления>
TO = ""               # <код станции прибытия>
API_KEY = ""          # <ключ>

# NOT-REQUIRED PARAMETRS
FORMAT = ""           # <формат — XML или JSON>
LANG = ""             # <язык>
DATE = ""             # <дата>
TRANSPORT_TYPES = ""  # <тип транспорта>
SYSTEM = ""           # <система кодирования параметров to и from>
SHOW_SYSTEMS = ""     # <система кодирования для ответа>
OFFSET = ""           # <сдвиг относительно первого рейса в ответе>
LIMIT = ""            # <ограничение на количество рейсов в ответе>
ADD_DAYS_MASK = ""    # <запрос календаря хождения рейсов>
TIMEZONE = ""         # <часовой пояс>
TRANSFERS = ""        # <признак запроса маршрутов с пересадками>
