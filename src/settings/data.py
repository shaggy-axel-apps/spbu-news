from dataclasses import dataclass


@dataclass
class DbConfig:
    database: str
    user: str
    password: str
    host: str
    port: int


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous
