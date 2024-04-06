from aiogram import Router, types
from aiogram.filters import Command

from bot.messages import INFO_MESSAGE

router = Router(name="info")


@router.message(Command(commands=["info", "help", "about", "start"]))
async def info_handler(message: types.Message) -> None:
    """Information about bot."""

    await message.answer(INFO_MESSAGE)
