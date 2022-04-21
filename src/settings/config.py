from settings.const import (
    BOT_TOKEN, ADMINS, USE_REDIS,
    POSTGRES_DB, POSTGRES_USER, POSTGRES_PASS,
    REDIS_HOST, REDIS_PORT, REDIS_PASSWORD,
)
from settings.data import CacheConfig, Config, TgBot, DbConfig, Miscellaneous


def load_config() -> Config:
    """ load config with telegram-bot, database and extra fields """
    return Config(
        tg_bot=TgBot(
            token=BOT_TOKEN, admin_ids=ADMINS,
            use_redis=USE_REDIS
        ),
        db=DbConfig(
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASS,
            host="db",
            port=5432,
        ),
        cache=CacheConfig(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD
        ),
        misc=Miscellaneous()
    )
