from aiogram import Bot, Dispatcher
from aiogram.types import CallbackQuery

from settings import load_config
from tgbot.keyboards import get_programs_keyboard


CONFIG = load_config()


async def programs_from_division(query: CallbackQuery):
    bot = Bot(token=CONFIG.tg_bot.token, parse_mode='MarkdownV2')
    _, division_alias = query.data.split(":")
    keyboard = await get_programs_keyboard(division_alias)
    await bot.send_message(query.from_user.id, division_alias, reply_markup=keyboard)
    await bot.delete_message(query.message.chat.id, query.message.message_id)


def register_callbacks(dp: Dispatcher):
    dp.register_callback_query_handler(
        programs_from_division, lambda callback_query: True,
        state="*"
    )
