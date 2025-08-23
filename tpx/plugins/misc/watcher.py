from pyrogram import filters
from pyrogram.types import Message

from tpx import app
from tpx.core.call import toxic

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await toxic.stop_stream_force(message.chat.id)
