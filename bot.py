from pyrogram import Client
from configparser import ConfigParser
import tagger

config = ConfigParser()
config.read("config.ini")

app = Client(
    "usertaggerbot",
    api_id=int(config["bot"]["api_id"]),
    api_hash=config["bot"]["api_hash"],
    bot_token=config["bot"]["bot_token"]
)

app.run()
