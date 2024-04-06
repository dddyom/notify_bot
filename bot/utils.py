from aiogram import types

from bot.config import Config


def is_owner(message: types.Message) -> bool:
    user = message.from_user
    return bool(user and str(user.id) == Config.USER_ID)
