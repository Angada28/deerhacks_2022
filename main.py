import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$math'):
        await message.channel.send('worked')
        sentenced = message.content.split(" ")
        sentence = ''
        for i in range(1,len(sentenced)):
            sentence += sentenced[i] + " "
        if sentence == '':
            return
        await message.channel.send(sentence);
        return
my_secret = os.environ['TOKEN']
client.run(my_secret)


