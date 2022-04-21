from typing import Iterable

from aiogram.types import InlineKeyboardButton

from tgbot.keyboards.paginator import InlineKeyboardPaginator


def count_pages(data: Iterable) -> int:
    if len(data) % 10 == 0:
        return len(data) // 10
    return len(data) // 10 + 1


def fill_paginator(
    data: Iterable, data_fields: tuple[str],
    callback_data_prefix: str, callback_data_field: str,
    previous_keyboard_callback: str,
    paginator: InlineKeyboardPaginator
) -> InlineKeyboardPaginator:
    """ create keyboard with pages pagination """
    start = paginator.current_page * 10 - 10
    stop = paginator.current_page * 10

    if len(data) < stop:
        stop = len(data)

    for object_index in range(start, stop, 2):
        first_callback = (
            f"{callback_data_prefix}#"
            f"{getattr(data[object_index], callback_data_field)}#1"
        )
        if stop != object_index + 1:
            second_callback = (
                f"{callback_data_prefix}#"
                f"{getattr(data[object_index + 1], callback_data_field)}#1"
            )
            paginator.add_before(
                InlineKeyboardButton(
                    ":".join(
                        str(getattr(data[object_index], data_field))
                        for data_field in data_fields
                    ),
                    callback_data=first_callback
                ),
                InlineKeyboardButton(
                    ":".join(
                        str(getattr(data[object_index + 1], data_field))
                        for data_field in data_fields
                    ),
                    callback_data=second_callback
                )
            )
        else:
            paginator.add_before(
                InlineKeyboardButton(
                    ":".join(
                        str(getattr(data[object_index], data_field))
                        for data_field in data_fields
                    ),
                    callback_data=first_callback
                )
            )
    paginator.add_after(
        InlineKeyboardButton("Назад", callback_data=previous_keyboard_callback)
    )
    return paginator
