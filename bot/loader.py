from aiogram import Bot, Dispatcher

from bot.config import Config

dp = Dispatcher()
bot = Bot(token=Config.BOT_TOKEN)
