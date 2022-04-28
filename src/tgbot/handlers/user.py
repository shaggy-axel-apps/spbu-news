from aiogram import Dispatcher
from aiogram.types import Message
from db.queries import save_user

from tgbot.keyboards.inline import new_user_keyboard, saved_user_keyboard


async def user_start(message: Message):
    text = "Menu"
    created = save_user(message.from_user.id)
    if created:
        text = f"Welcome {message.from_user.full_name}\n{text}"
        keyboard = new_user_keyboard()
    else:
        keyboard = saved_user_keyboard(message.from_user.id)

    await message.answer(text, reply_markup=keyboard)
    await message.bot.delete_message(message.chat.id, message.message_id)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
