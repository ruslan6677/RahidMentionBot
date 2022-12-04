import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID", "19485442"))
    API_HASH = os.environ.get("API_HASH", "a03fcb372b3ec4e406b5d52f84b02e53")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5394785524:AAGiGd4Xth_0Fa4oe32FYWEAfbTVbeD_W4M")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Rahid_Tag_Bot")
    BOT_NAME = os.environ.get("BOT_NAME", "𝑅𝐴𝐻𝐼𝐷 𝑇𝐴𝐺 🇦🇿")
    BOT_ID = int(os.environ.get("BOT_ID", "5394785524"))
    SUDO_USERS = os.environ.get("SUDO_USERS", "571698989").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "Rahid_Support")
    OWNER_ID = int(os.environ.get("OWNER_ID", "571698989"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Rahid_2003")
