from aiogram import Router, types
from aiogram.filters import Command

from bot.loader import bot
from bot.messages import INFO_MESSAGE

router = Router(name="info")


@router.message(Command(commands=["info", "help", "about", "start"]))
async def info_handler(message: types.Message) -> None:
    """Information about bot."""

    await bot.delete_message(message.chat.id, message.message_id)

    await message.answer(INFO_MESSAGE)
