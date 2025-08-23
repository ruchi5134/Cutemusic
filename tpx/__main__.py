import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from tpx import LOGGER, app, userbot
from tpx.core.call import toxic
from tpx.misc import sudo
from tpx.plugins import ALL_MODULES
from tpx.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("tpx.plugins" + all_module)
    LOGGER("tpx.plugins").info("Successfully Imported Modules For tpx system")
    await userbot.start()
    await toxic.start()
    try:
        await toxic.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("tpx").error(
            "Bsdk turn on the videochat of your log group\channel. 🤬\n\nStopping tpx..."
        )
        exit()
    except:
        pass
    await toxic.decorators()
    LOGGER("tpx").info("Tpx System Started Successfully \n\n Yaha App ko nahi aana hai aapni hf jo bhej sakte hai @xscnox ")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("tpx").info("Stopping Tpx.......")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
