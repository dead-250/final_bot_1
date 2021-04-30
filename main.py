import discord
import os

client=discord.Client()
@client.event
async def on_ready():
	print('we have logged in as {0.user}'
.format(client))


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	dark_commands = [
	    "cookie", "az", "ceo", "CEO", "cookies", "we offer cookies"
	]
	the_cookie = ["🍪"]
	msg = message.content
	if message.content.startsWith('hello there'):
		await message.channel.send('general kenobi!')
	if any(word in msg for word in darsk_commands):
		await message.channel.send(the_cookie)	

client.run(os.environ['TOKEN'])
