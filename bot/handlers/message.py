from aiogram import Router, types

from bot.loader import bot
from bot.utils import is_owner

router = Router(name="message")


@router.message()
async def handler(message: types.Message) -> None:
    """Information about bot."""
    if not is_owner(message):
        return

    if message.text:
        await bot.delete_message(message.chat.id, message.message_id)
        await message.answer(message.text)
