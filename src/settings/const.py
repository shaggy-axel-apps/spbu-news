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

# API
SPBU_API = "https://timetable.spbu.ru/api/v1/"
