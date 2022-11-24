# (©)Codexbotz
# Recife By #Mafia_Tobatz
# Recode by @RYUUSHINNI
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5863064719:AAE0T-ZEv4N5-JO9LvkyC6LqtsU1xbcB5_c")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "13663693"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "1f93516405fced4f28ada0f2e1496d40")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001615531278"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5029255799"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "Tytydaj")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://ygugoklo:GuavWOBSVwe7M527C5zZ1Oh1Wj5qJJC_@peanut.db.elephantsql.com/ygugoklo")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "")
GROUP = os.environ.get("GROUP", "")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001666792521"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001530272301"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "5029255799 2013745499").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nᴊɪᴋᴀ ʟᴀᴍᴀ ᴍᴜɴᴄᴜʟ ᴛᴜɴɢɢᴜ 5 ᴍᴇɴɪᴛ ᴍᴜɴɢᴋɪɴ ʙᴏᴛ ᴋᴏɴᴅɪsɪ ʙᴀɴʏᴀᴋ ʏᴀɴɢ ᴘᴀᴋᴀɪ ᴛᴏʟᴏɴɢ ᴊᴀɴɢᴀɴ ᴅɪ sᴘᴀᴍ ᴀɢᴀʀ ᴛɪᴅᴀᴋ ᴅᴇʟᴀʏ.\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", True) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(1540632666)
ADMINS.append(5041138056)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
