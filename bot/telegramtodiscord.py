import bot

client = bot.telegram
dispatcher = bot.dispatcher

@dispatcher.message()
async def on_message (message):
  cof = bot.config()
  
  if message.chat.id not in cof['telegram']:
    await message.answer(cof['messages']['notwhitelisted'])
    return
  
  name = message.from_user.full_name
  for a in cof['discord']:
    try:
      ch = bot.discord.get_channel(a)
      wh = await ch.create_webhook(name=name)
      await wh.send(message.text)
      await wh.delete()
    except AttributeError:
      pass