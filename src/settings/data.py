from dataclasses import dataclass

from sqlalchemy.engine.base import Engine


@dataclass
class CacheConfig:
    host: str
    port: int
    password: str


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
    cache: CacheConfig
    db: Engine
    misc: Miscellaneous
