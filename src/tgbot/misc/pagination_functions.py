from typing import Iterable

from aiogram.types import InlineKeyboardButton

from tgbot.keyboards.paginator import InlineKeyboardPaginator


def count_pages(data: Iterable, page_size: int = 10) -> int:
    if len(data) % page_size == 0:
        return len(data) // page_size
    return len(data) // page_size + 1


def fill_paginator(
    data: Iterable, data_fields: tuple[str],
    callback_data_prefix: str, callback_data_field: str,
    previous_keyboard_callback: str,
    paginator: InlineKeyboardPaginator,
    row_size: int = 2, page_size: int = 10
) -> InlineKeyboardPaginator:
    """ create keyboard with pages pagination """
    start = paginator.current_page * page_size - page_size
    stop = paginator.current_page * page_size

    if row_size > 2:
        row_size = 2

    if len(data) < stop:
        stop = len(data)

    for object_index in range(start, stop, row_size):
        first_callback = (
            f"{callback_data_prefix}#"
            f"{getattr(data[object_index], callback_data_field)}#1"
        )
        if stop != object_index + 1 and row_size != 1:
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
