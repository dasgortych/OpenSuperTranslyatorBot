import yaml
import disnake
from disnake.ext import commands
import aiogram

def config ():
  with open('config.yml') as f:
    return yaml.safe_load(f)

discord = commands.Bot(command_prefix='!',intents=disnake.Intents.all())
telegram = aiogram.Bot(open('tokentelegram.txt').read())
dispatcher = aiogram.Dispatcher()
