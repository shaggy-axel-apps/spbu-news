from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards import start_keyboard


async def user_start(message: Message):
    keyboard = await start_keyboard()
    await message.answer("Hello, user!", reply_markup=keyboard)
    await message.bot.delete_message(message.chat.id, message.message_id)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
