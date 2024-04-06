from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN = getenv("BOT_TOKEN") or ""
    CHANNEL_ID = getenv("CHANNEL_ID") or ""
