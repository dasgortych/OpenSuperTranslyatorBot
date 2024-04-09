# top of the file
# importing libraries
import disnake
from disnake.ext import commands
import aiogram
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
import asyncio
import yaml
from time import localtime

# support functions
# getting current local time as dictionary
def get_time ():
  lc = localtime()
  return {'year':lc[0],'month':lc[1],'day':lc[2],'hour':lc[3],'minute':lc[4],'second':lc[5]}


# logging messages into console with local time
def log (*args, category=''):
  if not category.isspace():
    categories = ''.join([f' [{a}]' for a in category.split()])
  for a in args:
    lc = get_time();
    h=lc['hour'];m=lc['minute'];s=lc['second']
    print(f'[{h}:{m}:{s}]{categories} > {a}')


# getting settings from config.yml
def get_settings ():
  with open('config.yml') as f:
    doc = yaml.safe_load(f)
  return doc

def get_tgs ():
  return get_settings()['telegram']
def get_dss ():
  return get_settings()['discord']



# getting bots
ds = commands.Bot(command_prefix='-', intents=disnake.Intents.all())
tgConnect = aiogram.Bot(token=open('tokentelegram.txt').read())
tg = aiogram.Dispatcher()


# discord client
@ds.event
async def on_connect ():
  log('Connected to Discord',category='DISCORD INFO')

@ds.event
async def on_message (message):
  if not message in get_dss()['chats']:
    return
  # here's continuation


# telegram client
@tg.message(CommandStart())
async def telegram_command_start (message: aiogram.types.Message):
  await message.answer(get_tgs()['messages']['start'])

@tg.message()
async def echo_handler (message: aiogram.types.Message):
  await message.answer(get_tgs()['messages']['echo'])


# running bots
async def dsGather ():
  await ds.start(open('tokendiscord.txt').read())

async def tgGather ():
  await tg.start_polling(tgConnect)

async def main ():
  await asyncio.gather(dsGather(), tgGather())

asyncio.run(main())