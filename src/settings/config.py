from sqlalchemy import create_engine

from settings.const import (
    BOT_TOKEN, ADMINS, USE_REDIS,
    POSTGRES_DB, POSTGRES_USER, POSTGRES_PASS,
    POSTGRES_HOST, POSTGRES_PORT,
    REDIS_HOST, REDIS_PORT, REDIS_PASSWORD,
)
from settings.data import CacheConfig, Config, TgBot, Miscellaneous


engine=create_engine(
    (f'postgresql://{POSTGRES_USER}:{POSTGRES_PASS}'
     f'@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'),
    client_encoding='utf8'
)


def load_config() -> Config:
    """ load config with telegram-bot, database and extra fields """
    return Config(
        tg_bot=TgBot(
            token=BOT_TOKEN, admin_ids=ADMINS,
            use_redis=USE_REDIS
        ),
        db=engine,
        cache=CacheConfig(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD
        ),
        misc=Miscellaneous()
    )
