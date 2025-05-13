from pyrogram.types import Message
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")
OWNER_ID = int(config["bot"]["owner_id"])

def is_admin(user_id: int, admins: list[int]):
    return user_id == OWNER_ID or user_id in admins

def get_flag():
    return "🚩"

def get_emoji():
    return "🌟"
