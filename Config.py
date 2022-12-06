import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID", "10300036"))
    API_HASH = os.environ.get("API_HASH", "79c295e05c970ddd724f0762ba275104")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5806444106:AAG2eBRSOsfKbcZvlf0wA_6lG73qJ1zgqPI")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "DevolopTaggerbot")
    BOT_NAME = os.environ.get("BOT_NAME", "DevolopTag")
    BOT_ID = int(os.environ.get("BOT_ID", "5806444106"))
    SUDO_USERS = os.environ.get("SUDO_USERS", "2124305832").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "Rahid_Support")
    OWNER_ID = int(os.environ.get("OWNER_ID", "2124305832"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Rahid_2003")
