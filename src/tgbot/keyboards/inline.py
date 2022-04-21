from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from spbu_api import StudyDivisionsApi


async def start_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            "Расписание автобусов", callback_data="autobus_pages#1"),
        InlineKeyboardButton(
            "Расписание занятий", callback_data="division_pages#1"))
    keyboard.add(
        InlineKeyboardButton(
            "События", callback_data="event_pages#1"),
        InlineKeyboardButton(
            "Info List", callback_data="spbu_info")
        )
    keyboard.add(InlineKeyboardButton(
        "Аккаунт", callback_data="account_info"))
    return keyboard


async def get_programs_keyboard(division_alias: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    division_api = StudyDivisionsApi()
    for program in await division_api.get_programs(division_alias):
        keyboard.add(InlineKeyboardButton(
            f"{program.year}{program.name}",
            callback_data=f"program:{program.program_id}"
        ))
    return keyboard
