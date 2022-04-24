from datetime import datetime

from aiogram import Dispatcher
from aiogram.types import CallbackQuery
import emoji

from settings.const import EMOJIES, WEEKDAYS_NAMES, GOOGLE_MAPS, YANDEX_MAPS
from sut_scraper.scraper import Scraper
from tgbot.handlers.user import user_start
from tgbot.keyboards import InlineKeyboardPaginator, get_timetable_keyboard
from tgbot.keyboards.reply import request_location_keyboard
from tgbot.misc.pagination_functions import count_pages, fill_paginator
from ya_rasp_api.worker import YandexRaspisanieApi


async def send_divisions(query: CallbackQuery):
    page = int(query.data.split("#")[1])

    scraper = Scraper()
    divisions = await scraper.get_all_divisions()

    page_count = count_pages(divisions, page_size=5)

    paginator = InlineKeyboardPaginator(
        page_count=page_count, current_page=page,
        data_pattern='division_pages#{page}'
    )

    paginator = fill_paginator(
        data=divisions, data_fields=("name",),
        callback_data_prefix="group_pages", callback_data_field="alias",
        previous_keyboard_callback="start", paginator=paginator, row_size=1, page_size=5)

    await query.bot.send_message(
        query.from_user.id, emoji.emojize(EMOJIES["division"]) + f" Направления: {page}",
        reply_markup=paginator.markup
    )
    await query.bot.delete_message(
        query.message.chat.id, query.message.message_id
    )


async def send_groups(query: CallbackQuery):
    division_alias = query.data.split("#")[1]

    scraper = Scraper()
    groups = await scraper.get_groups(division_alias=division_alias)

    page = int(query.data.split("#")[2])
    page_count = count_pages(groups)

    paginator = InlineKeyboardPaginator(
        page_count=page_count, current_page=page,
        data_pattern=(
            f'group_pages#{division_alias}'
            '#{page}'
        )
    )

    paginator = fill_paginator(
        data=groups, data_fields=("name",),
        callback_data_prefix="timetable#today", callback_data_field="group_id",
        previous_keyboard_callback="division_pages#1",
        paginator=paginator, without_page_in_callback=True)

    await query.bot.send_message(
        query.from_user.id, (
            emoji.emojize(EMOJIES["division"]) + f" Направление: {division_alias}\n" +
            emoji.emojize(EMOJIES["group"]) + f" Группы: {page}"
        ),
        reply_markup=paginator.markup
    )
    await query.bot.delete_message(
        query.message.chat.id, query.message.message_id
    )


async def send_timetable(query: CallbackQuery):
    day = query.data.split('#')[1]
    group_id = query.data.split('#')[2]
    if day == 'today':
        day = str(datetime.today()).split()[0]

    scraper = Scraper()
    event_day = await scraper.get_timetable(group_id=int(group_id), day=day)
    keyboard = get_timetable_keyboard(event_day)

    week_day = WEEKDAYS_NAMES[datetime.weekday(datetime.strptime(day, "%Y-%m-%d"))]
    message = emoji.emojize(f"{EMOJIES['date']}  `{week_day} {event_day.day}`\n\n")
    for event in event_day.events:
        message += emoji.emojize(
            f"*{event.subject}*\n*{event.reason}*\n"
            f"{EMOJIES['educator']} _Преподователь: {event.educator}_\n"
            f"{EMOJIES['classroom']} _Аудитория:_ `{event.classroom}`\n\n"
        )

    await query.bot.send_message(
        query.from_user.id, text=message,
        reply_markup=keyboard, parse_mode="Markdown"
    )
    await query.bot.delete_message(
        query.message.chat.id, query.message.message_id
    )


async def request_location(query: CallbackQuery):
    message = (
        emoji.emojize(f"{EMOJIES['smile']} __Нажмите на кнопку ниже, ") +
        emoji.emojize(f"чтобы поделиться локацией__ {EMOJIES['maps']}")
    )
    keyboard = request_location_keyboard()
    await query.bot.send_message(
        query.from_user.id, text=message,
        reply_markup=keyboard, parse_mode="Markdown"
    )
    await query.bot.delete_message(
        query.message.chat.id, query.message.message_id
    )


async def start_with_callback(query: CallbackQuery):
    await user_start(query.message)


def register_callbacks(dp: Dispatcher):
    dp.register_callback_query_handler(
        start_with_callback, lambda query: "start" in query.data, state="*")
    dp.register_callback_query_handler(
        send_groups, lambda query: "group_pages" in query.data, state="*")
    dp.register_callback_query_handler(
        send_divisions, lambda query: "division_pages" in query.data, state="*")
    dp.register_callback_query_handler(
        send_timetable, lambda query: "timetable" in query.data, state="*")
    dp.register_callback_query_handler(
        request_location, lambda query: "bus" == query.data, state="*")
