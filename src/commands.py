from typing import Any
from parse import Command, Parser
from solve import solve
from simplify import simplify

COMMANDS_TO_IMPL = {
    'solve'.casefold() : solve,
    'simplify'.casefold(): simplify
}

def dispatch_command(cmd: Command) -> Any:
    return COMMANDS_TO_IMPL[cmd.command](cmd.args)


# print(dispatch_command(Parser().parse("$deermath solve y^2 - xy = 5 for y")))