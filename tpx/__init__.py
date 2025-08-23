from tpx.core.bot import toxic
from tpx.core.dir import dirr
from tpx.core.git import git
from tpx.core.userbot import Userbot
from tpx.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = toxic()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
