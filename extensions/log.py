import os
from datetime import datetime
from discord_webhook import DiscordWebhook

from dotenv import load_dotenv
from os.path import join, dirname
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


DISCORD_WEBHOOK = os.getenv('DISCORD_WEBHOOK')

def l(str):
    print("%s : %s" % (datetime.now().strftime("%Y/%m/%d %H:%M:%S"), str))

async def bot_say(text: str):
    DiscordWebhook(url=DISCORD_WEBHOOK, content=text).execute()