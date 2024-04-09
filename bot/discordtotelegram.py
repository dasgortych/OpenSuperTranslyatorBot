import bot

client = bot.discord

@client.event
async def on_message (message):
  cof = bot.config()
  
  if message.channel.id not in cof['discord'] or message.author.bot:
    return
  
  text = f'**{message.author.display_name}**' + '\n' + message.content
  for a in cof['telegram']:
    await bot.telegram.send_message(a, text)
