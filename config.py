from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/c06dc13db7690b96a0c13.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/e43dfce32aa093c6f511b.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tmm_support_chat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tmm_heroku_world")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6481884068").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
