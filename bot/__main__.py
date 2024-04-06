import asyncio
import logging
import sys

from bot.loader import bot, dp
from handlers import get_handlers_router


async def on_startup():
    dp.include_router(get_handlers_router())


async def main() -> None:
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
