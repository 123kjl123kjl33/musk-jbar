from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("17698861"))
API_HASH = getenv("b69aecfce02173110b437f4206f57306")

BOT_TOKEN = getenv("6434739473:AAENphC-GP6rS4MaWvBExnPAb9kmEVEwcOQ", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "3500"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "http://t.me/BBSI8")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "http://t.me/BBSI8")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5587153836").split()))


FAILED = "https://te.legra.ph/file/f7e1acf9338cc453a87ad.jpg"
