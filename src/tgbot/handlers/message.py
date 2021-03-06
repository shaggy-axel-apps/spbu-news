from aiogram import types, Dispatcher
from tgbot.keyboards.inline import return_to_start_keyboard

from ya_rasp_api import YandexRaspisanieApi
from settings.const import GOOGLE_MAPS, YANDEX_MAPS


async def get_stations(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    yandex_api = YandexRaspisanieApi()
    stations = await yandex_api.get_nearest_stations(lat=lat, lon=lon)
    reply = f"Ближайших Станций: {len(stations)}\n\n" + "\n\n".join(
        (
            f"{station.station_type}: `{station.title}` \n"
            f"расстояние: {station.distance}м \n"
            f"[Google]({GOOGLE_MAPS}{station.lat},{station.lon}), "
            f"[Yandex]({YANDEX_MAPS}{station.lat},{station.lon})"
        )
        for station in stations
    )
    keyboard = return_to_start_keyboard()
    await message.answer(reply, parse_mode="Markdown", reply_markup=keyboard)
    await message.delete_reply_markup()
    await message.delete()


def register_messages(dp: Dispatcher):
    dp.register_message_handler(
        get_stations, state="*",
        content_types=['location']
    )
