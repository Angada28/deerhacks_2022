from typing import Any
from parse import Command, Parser
from solve import solve

COMMANDS_TO_IMPL = {
    'solve'.casefold() : solve
}

def dispatch_command(cmd: Command) -> Any:
    return COMMANDS_TO_IMPL[cmd.command](cmd.args)


# print(dispatch_command(Parser().parse("$deermath solve y^2 - xy = 5 for y")))