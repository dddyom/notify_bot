from typing import Any

from aiogram import Router, types

router = Router(name="message")


@router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


@router.callback_query()
async def channel_post_handler(channel_post: types.Message) -> Any:
    try:
        await channel_post.send_copy(chat_id=channel_post.chat.id)
    except TypeError:
        await channel_post.answer("Nice try!")
