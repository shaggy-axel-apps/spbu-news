from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards import start_keyboard


async def admin_start(message: Message):
    keyboard = await start_keyboard()
    await message.reply("Hello, admin!", reply_markup=keyboard)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(
        admin_start, commands=["start"],
        state="*", is_admin=True
    )
