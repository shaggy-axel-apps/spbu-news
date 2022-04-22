from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from spbu_api import StudyDivisionsApi
from sut_scraper.scraper import Scraper
from tgbot.handlers.user import user_start
from tgbot.keyboards import InlineKeyboardPaginator
from tgbot.misc.pagination_functions import count_pages, fill_paginator


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
        query.from_user.id, f"Направления: {page}",
        reply_markup=paginator.markup
    )
    await query.bot.delete_message(
        query.message.chat.id, query.message.message_id
    )


async def programs_from_division(query: CallbackQuery):
    division_alias = query.data.split("#")[1]

    scraper = Scraper()
    groups = await scraper.get_all_groups(division_alias=division_alias)

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
        callback_data_prefix="group_pages", callback_data_field="group_id",
        previous_keyboard_callback="division_pages#1", paginator=paginator)

    await query.bot.send_message(
        query.from_user.id, f"Направление: {division_alias}\nГруппы: {page}",
        reply_markup=paginator.markup
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
        programs_from_division, lambda query: "group_pages" in query.data, state="*")
    dp.register_callback_query_handler(
        send_divisions, lambda query: "division_pages" in query.data, state="*")
