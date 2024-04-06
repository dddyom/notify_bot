from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN = getenv("BOT_TOKEN") or ""
    USER_ID = getenv("USER_ID") or ""
