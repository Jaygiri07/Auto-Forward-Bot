from os import getenv

class Config(object):
      API_HASH = getenv("ba25181c01b50d945748801b6c8b6ecc")
      API_ID = int(getenv("26162072", 0))
      AS_COPY = True if getenv("AS_COPY", False) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "7592820871:AAFVmhILYzWQbBlv_Mk6PlD10Sn052DoDfM")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002264789489").replace("\n", " ").split(' '))
