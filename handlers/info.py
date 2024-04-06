from aiogram import Router, types
from aiogram.filters import Command

from bot.config import Config
from bot.loader import bot

router = Router(name="info")


@router.message(Command(commands=["info", "help", "about"]))
async def info_handler(message: types.Message) -> None:
    """Information about bot."""

    # await bot.send_message(Config.CHANNEL_ID, "Bot started!")
    await message.answer("sdf")
