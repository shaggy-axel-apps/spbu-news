from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards import start_keyboard


async def user_start(message: Message):
    keyboard = await start_keyboard()
    await message.reply("Hello, user!", reply_markup=keyboard)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
