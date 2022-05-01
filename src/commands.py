from typing import Any
from parse import Command, Parser
from solve import solve
from simplify import simplify
from differentiate import differentiate

COMMANDS_TO_IMPL = {
    'solve'.casefold() : solve,
    'simplify'.casefold(): simplify,
    'diff'.casefold(): differentiate
}

def dispatch_command(cmd: Command, state) -> Any:
    return COMMANDS_TO_IMPL[cmd.command](cmd.args, state)


# print(dispatch_command(Parser().parse("$deermath solve y^2 - xy = 5 for y")))