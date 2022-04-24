import os


# TELEGRAM BOT
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMINS = tuple(map(int, os.environ.get("ADMINS").split(',')))
USE_REDIS = bool(os.environ.get("USE_REDIS"))

# DATABASE
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASS = os.environ.get('POSTGRES_PASS')

# REDIS
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = int(os.environ.get('REDIS_PORT'))
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')

# API, URLs, Headers
YANDEX_API = "https://api.rasp.yandex.net/v3.0"
YANDEX_API_KEY = os.environ.get("YANDEX_API")

SPBU_API = "https://timetable.spbu.ru/api/v1/"

SUT_URL = (
    "https://www.sut.ru/studentu/raspisanie/"
    "raspisanie-zanyatiy-studentov-ochnoy-i-vecherney-form-obucheniya")
SUT_HEADERS = {
    'User-Agent': os.environ.get("HEADERS"),
    'Referer': 'https://www.sut.ru/'}

GOOGLE_MAPS = "http://www.google.com/maps/place/"
YANDEX_MAPS = "http://yandex.ru/maps/?rtext="

# OTHER
WEEKDAYS_NAMES = {
    0: "Пн.",
    1: "Вт.",
    2: "Ср.",
    3: "Чт.",
    4: "Пт.",
    5: "Сб.",
    6: "Вс."
}

EMOJIES = {
    'timetable': ':five_o’clock:',                # 🕔
    'date': ':tear-off_calendar:',                # 📆
    'classroom': ':school:',                      # 🏫
    'educator': ':man_teacher:',                  # 👨‍🏫
    'group': ':busts_in_silhouette:',             # 👥
    'division': ':card_index_dividers:',          # 🗂
    'prev_week': ':fast_reverse_button:',         # ⏪
    'next_week': ':fast-forward_button:',         # ⏩
    'prev_day': ':left_arrow:',                   # ⬅️
    'next_day': ':right_arrow:',                  # ➡️
    'bus': ':bus:',                               # 🚌
    'smile': ':smiling_face_with_smiling_eyes:',  # 😊
    'maps': ':world_map:'                         # 🗺
}
