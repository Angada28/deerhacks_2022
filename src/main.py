import discord
import os
import sympy as sympy
from parse import Parser
from commands import dispatch_command
from out import sympy_expr_to_img, bytes_io_to_discord_file

client = discord.Client()
parser = Parser()
LATEX = True

try:
    with open('token') as tokenf:
        token = tokenf.readline().strip()
except FileNotFoundError as e:
    print("[ERROR] Must create a file named 'token' with the discord token.")
    raise e

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$deermath'):
        await message.channel.send('Thinking...')
        try:
            cmd = parser.parse(message.content)
            out = dispatch_command(cmd)
            
            if LATEX:
                await message.channel.send(
                    file=bytes_io_to_discord_file(sympy_expr_to_img(out)))
            else:
                await message.channel.send(f"`{str(out)}`")
        except Exception as e:
            await message.channel.send(f"Oops, there has been an issue:\n{str(e)}")


    if message.content.startswith('$math'):
        await message.channel.send('worked')
        sentenced = message.content.split(" ")
        sentence = ''
        for i in range(1,len(sentenced)):
            sentence += sentenced[i] + " "
        if sentence == '':
            return
        await message.channel.send(sentence)
        return
    
    if message.content.startswith('$test'):
        await message.channel.send(
            file=bytes_io_to_discord_file(
                sympy_expr_to_img(
                    # Note sympify is not safe to use on arbitrary input
                    sympy.sympify("x^2 - 3*y + 5"))
            )
        )

client.run(token)

