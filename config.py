import os


class Config(object):
    API_HASH = ("5a2e46d1e6deb1456c75aa743bc8e0e6")
    BOT_TOKEN = ("7399145318:AAFv1VMcDVwPkQNElgdBBH5YJ-A3iw5G_i0")
    TELEGRAM_API = 7931165
    OWNER = ("6274275394")
    OWNER_USERNAME = ("Devilharsha_2153")
    PASSWORD = ("TMR")
    DATABASE_URL = ("mongodb+srv://Filesstreambot:eHtqPEVohrO3YAS3@cluster0.hdxt929.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = ("-1002017090961")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
