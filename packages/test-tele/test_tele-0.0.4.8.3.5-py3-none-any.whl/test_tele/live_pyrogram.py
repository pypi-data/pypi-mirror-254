from test_tele.config import CONFIG

from pyrogram import Client
from telethon.sessions import StringSession

session_string_user = StringSession(CONFIG.login.SESSION_STRING)
api_id = CONFIG.login.API_ID
api_hash = CONFIG.login.API_HASH
bot_token = CONFIG.login.BOT_TOKEN


APP = Client("my_bot", api_id=api_id, api_hash=api_hash, in_memory=True, bot_token=bot_token)

