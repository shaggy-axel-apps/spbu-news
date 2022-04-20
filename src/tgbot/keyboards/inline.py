from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from spbu_api import StudyDivisionsApi


async def start_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(
        "Расписание", callback_data=f"division_pages#1"))
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
