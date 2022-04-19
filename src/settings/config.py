from settings.const import (
    BOT_TOKEN, ADMINS, USE_REDIS,
    POSTGRES_DB, POSTGRES_USER, POSTGRES_PASS,
)
from settings.data import Config, TgBot, DbConfig, Miscellaneous


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
        misc=Miscellaneous()
    )
