

from pyrogram import Client
from ..vars import Var

StreamBot = Client(
    session_name= 'hr-file-stream',
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)
