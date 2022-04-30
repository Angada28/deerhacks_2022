import discord
import os
import sympy as sympy
from history import History
from parse import Parser
from commands import dispatch_command
from out import sympy_expr_to_img, bytes_io_to_discord_file
from state import BotState

client = discord.Client()
state = BotState()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$deermath latex on'):
        state.cfg_latex = True
        await message.channel.send('Ok...')
    
    elif message.content.startswith('$deermath latex off'):
        state.cfg_latex = False
        await message.channel.send('Ok...')

    elif message.content.startswith('$deermath'):
        await message.channel.send('Thinking...')
        try:
            cmd = state.parser.parse(message.content)
            out = dispatch_command(cmd, state)
            
            if state.cfg_latex:
                await message.channel.send(
                    file=bytes_io_to_discord_file(sympy_expr_to_img(out)))
            else:
                await message.channel.send(f"`{str(out)}`")
        except Exception as e:
            await message.channel.send(f"Oops, there has been an issue:\n{str(e)}")
            out = "ERROR"
        state.global_history.register_command(message.channel, message.content, out)

    elif message.content.startswith('$repeat'):
        try:
            try:
                idx = -abs(int(message.content.split()[1].strip()))
            except IndexError:
                idx = -1

            cmd, out = state.global_history.last(message.channel, idx)
            await message.channel.send(f"> {cmd}")

            if state.cfg_latex and not isinstance(out, str):
                await message.channel.send(
                    file=bytes_io_to_discord_file(sympy_expr_to_img(out)))
            else:
                await message.channel.send(f"`{str(out)}`")
        except Exception as e:
            await message.channel.send(f"Oops, there has been an issue:\n{str(e)}")
            
    
    elif message.content.startswith('$test'):
        await message.channel.send(
            file=bytes_io_to_discord_file(
                sympy_expr_to_img(
                    # Note sympify is not safe to use on arbitrary input
                    sympy.sympify("x^2 - 3*y + 5"))
            )
        )


if __name__ == "__main__":
    try:
        with open('token') as tokenf:
            token = tokenf.readline().strip()
    except FileNotFoundError as e:
        print("[ERROR] Must create a file named 'token' with the discord token.")
        raise e

    client.run(token)


