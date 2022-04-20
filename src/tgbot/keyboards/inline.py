from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from spbu_api import StudyDivisionsApi


async def start_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    division_api = StudyDivisionsApi()
    for division in await division_api.get_all():
        keyboard.add(InlineKeyboardButton(
            division.name, callback_data=f"division:{division.alias}"))
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
