# Telegram-Bot-Template
## Stack
Python, Aiogram, Aiohttp, BeautifulSoup,
Docker, PostgreSQL, Redis
## Setup
```bash
# change values in `.env` after this command
cat env_sample > .env

# building bot service and run serivces
docker-compose build
docker-compose up -d

# database migrations
docker-compose exec bot bash
python src/bot.py migrate
```

## Get data from
 * [spbsut-timetable](https://www.sut.ru/studentu/raspisanie/raspisanie-zanyatiy-studentov-ochnoy-i-vecherney-form-obucheniya) - scrape data
 * [spbu-timetable](https://timetable.spbu.ru/) using [spbu-timetable-api](https://timetable.spbu.ru/api/v1/) - [docs-swagger](https://timetable.spbu.ru/docs/v1/swagger)
 * [yandex-raspisanie](https://api.rasp.yandex.net/v3.0/) - [docs](https://yandex.ru/dev/rasp/doc/reference/schedule-point-point.html)
