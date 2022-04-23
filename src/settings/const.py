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
SPBU_API = "https://timetable.spbu.ru/api/v1/"
SUT_URL = (
    "https://www.sut.ru/studentu/raspisanie/"
    "raspisanie-zanyatiy-studentov-ochnoy-i-vecherney-form-obucheniya"
)
SUT_HEADERS = {
    'User-Agent': os.environ.get("HEADERS"),
    'Referer': 'https://www.sut.ru/'
}

# OTHER
WEEKDAYS_NAMES = {
    1: "Пн.",
    2: "Вт.",
    3: "Ср.",
    4: "Чт.",
    5: "Пт.",
    6: "Сб.",
    7: "Вс."
}

EMOJIES = {
    'timetable': ':five_o’clock:',         # 🕔
    'date': ':tear-off_calendar:',         # 📆
    'classroom': ':school:',               # 🏫
    'educator': ':man_teacher:',           # 👨‍🏫
    'group': ':busts_in_silhouette:',      # 👥
    'division': ':card_index_dividers:',   # 🗂
    'prev_week': ':fast_reverse_button:',  # ⏪
    'next_week': ':fast-forward_button:',  # ⏩
    'prev_day': ':left_arrow:',            # ⬅️
    'next_day': ':right_arrow:'            # ➡️
}
