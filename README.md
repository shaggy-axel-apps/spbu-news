# Telegram-Bot-Template
## Stack
Python, Aiogram, Aiohttp,
Docker, PostgreSQL, Redis
## Setup
```bash
cat env_sample > .env
# change values in .env

docker-compose build
docker-compose up -d
```

## Get data from
 * [spbu-timetable](https://timetable.spbu.ru/) using [spbu-timetable-api](https://timetable.spbu.ru/api/v1/) - [docs-swagger](https://timetable.spbu.ru/docs/v1/swagger)
 * [yandex-raspisanie](https://api.rasp.yandex.net/v3.0/) - [docs](https://yandex.ru/dev/rasp/doc/reference/schedule-point-point.html)
