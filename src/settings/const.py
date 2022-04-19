import os


# Environ Variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMINS = tuple(map(int, os.environ.get("ADMINS").split(',')))
USE_REDIS = bool(os.environ.get("USE_REDIS"))

POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASS = os.environ.get('POSTGRES_PASS')

PROGRAMS_ID_FROM = 10_000
PROGRAMS_ID_TO = 10_263

SPBU_API = "https://timetable.spbu.ru/api/v1/"
