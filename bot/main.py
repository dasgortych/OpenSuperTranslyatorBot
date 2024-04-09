import asyncio
from discordtotelegram import client as discord
from telegramtodiscord import client as telegram
from telegramtodiscord import dispatcher

async def ds ():
  tkn = open('tokendiscord.txt').read()
  await discord.start(tkn)

async def tg ():
  await dispatcher.start_polling(telegram)

async def main ():
  await asyncio.gather(ds(), tg())

asyncio.run(main())