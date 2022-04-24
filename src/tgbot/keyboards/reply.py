from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji

from settings.const import EMOJIES


def request_location_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(KeyboardButton(
        emoji.emojize(f"Отправить Локацию {EMOJIES['maps']}"), request_location=True))
    return keyboard
