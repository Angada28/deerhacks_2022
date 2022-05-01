import discord
import os
import sympy as sympy
from history import History
from parse import Parser
from commands import dispatch_command
from out import sympy_expr_to_img, bytes_io_to_discord_file
from state import BotState
from sympy import symbols
from sympy.plotting import plot
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, \
    implicit_multiplication_application

client = discord.Client()
state = BotState()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$deermath') and not message.content.startswith('$deermath '):
        instructions = '''Enter any of the following commands for:

SOLVE:
    DESCRIPTION:
        Solves a system of equations.
    COMMAND:
        $deermath solve {set of equation} for {variable}
    COMMAND:
        $deermath solve {set of equation} for {variable} where ...
        ... {...set of variable assignments...}
    EXAMPLE:
        $deermath solve x + y + z = 20 for z where x=2y, y=3z


DERIVATIVES:
    DESCRIPTION:
        Finds the derivative.
    COMMAND:
        $deermath diff {expression}
    EXAMPLE: 
        $deermath diff 5x^2
    
    For a multivariable expression please add
    the variable to differentiate with respect to:
    
        EXAMPLE:
            $deermath diff 2x + y for y


SUMMATIONS:
    DESCRIPTION:
        Finds the Riemann sum of an expression.
    COMMAND:
        $deermath summation {expression} where {variable} between ...
        ... {lower bound} and {upper bound}
    EXAMPLE: 
        $deermath summation 2k where k between 1 and n


SIMPLIFY:
    DESCRIPTION:
        Simplifies an expression.
    COMMAND:
        $deermath simplify {expression}
    COMMAND:
        $deermath simplify {expression} where {...set of variable assignments...}
    EXAMPLE:
        $deermath simplify x + 100^2y where x=a, y=2


PLOT GRAPH:
    DESCRIPTION:
        Plots a graph with the given expression
        with respect to x.
    COMMAND:
        $deermath plot {expression}
    EXAMPLE:
        $deermath plot x^3 + 5


REPEAT (repeats the last command):
    DESCRIPTION:
        Repeats the previous command.
    COMMAND:
        $repeat
    NOTE:
        Only the following commands can be repeated:
        solve, summation, diff, simplify
        '''
        await message.channel.send(f"```{instructions}```")

    elif message.content.startswith('$deermath latex on'):
        state.cfg_latex = True
        await message.channel.send('Ok...')

    elif message.content.startswith('$deermath latex off'):
        state.cfg_latex = False
        await message.channel.send('Ok...')

    elif message.content.startswith('$deermath plot'):
        try:
            arr = message.content.split(' ')
            exp = '0'
            if len(arr) > 2:
                exp = arr[2]
            exp = str(parse_expr(exp, transformations='all'))
            plt = plot(exp, show=False)
            plt.save('graph.png')
            with open('graph.png', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)
        except Exception as e:
            await message.channel.send(f"Oops, there has been an issue:\n{'Improper Expression was entered'}")

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


