from datetime import datetime, timedelta

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji

from settings.const import EMOJIES, WEEKDAYS_NAMES
from sut_scraper.models import EventDay


async def start_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            emoji.emojize(f"{EMOJIES['bus']} Расписание автобусов"),
            callback_data="bus"),
        InlineKeyboardButton(
            emoji.emojize(f"{EMOJIES['timetable']} Расписание занятий"),
            callback_data="division_pages#1"))
    return keyboard


def return_to_start_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            "Назад",
            callback_data="start"))
    return keyboard


def get_timetable_keyboard(event_day: EventDay) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    day = datetime.strptime(event_day.day, "%Y-%m-%d")
    next_day = day + timedelta(days=1)
    previous_day = day - timedelta(days=1)
    previous_day.day
    next_week = day + timedelta(days=7)
    previous_week = day - timedelta(days=7)

    keyboard.row(
        InlineKeyboardButton(
            emoji.emojize(EMOJIES["prev_day"]) + (
                f" {previous_day.day}.{previous_day.month} "
                f"{WEEKDAYS_NAMES[datetime.weekday(previous_day)]}"
            ),
            callback_data=(
                f"timetable#{datetime.strftime(previous_day, '%Y-%m-%d')}"
                f"#{event_day.group_id}"
            )
        ),
        InlineKeyboardButton(
            (
                f"{next_day.day}.{next_day.month} "
                f"{WEEKDAYS_NAMES[datetime.weekday(next_day)]} "
            ) + emoji.emojize(EMOJIES["next_day"]),
            callback_data=(
                f"timetable#{datetime.strftime(next_day, '%Y-%m-%d')}"
                f"#{event_day.group_id}"
            )
        )
    )

    keyboard.row(
        InlineKeyboardButton(
            emoji.emojize(EMOJIES["prev_week"]) + (
                f" {previous_week.day}.{previous_week.month} "
                f"{WEEKDAYS_NAMES[datetime.weekday(previous_week)]}"
            ),
            callback_data=(
                f"timetable#{datetime.strftime(previous_week, '%Y-%m-%d')}"
                f"#{event_day.group_id}"
            )
        ),
        InlineKeyboardButton(
            (
                f"{next_week.day}.{next_week.month} "
                f"{WEEKDAYS_NAMES[datetime.weekday(next_week)]} "
            ) + emoji.emojize(EMOJIES["next_week"]),
            callback_data=(
                f"timetable#{datetime.strftime(next_week, '%Y-%m-%d')}"
                f"#{event_day.group_id}"
            )
        )
    )

    keyboard.row(InlineKeyboardButton('Назад', callback_data="division_pages#1"))

    return keyboard
