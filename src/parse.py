"""
Parsing of bot commands.
"""

from dataclasses import dataclass
from typing import Any, List
from parse_simplify import parse_simplify

from parse_solve import parse_solve

from parse_differentiate import parse_differentiate

COMMANDS_TO_ARG_PARSER = {
    'solve'.casefold(): parse_solve,
    'simplify'.casefold(): parse_simplify,
    'diff'.casefold(): parse_differentiate
}

@dataclass
class Command:
    command: str
    args: Any


class InvalidMessageError(Exception):
    pass


class Parser:
    def __init__(self):
        pass

    def parse(self, msg: str) -> Command:
        if not msg.casefold().startswith("$deermath".casefold()):
            raise InvalidMessageError("Command must start with '$deermath'")

        _, cmd, rest = msg.split(maxsplit=2)
        if cmd.strip().casefold() not in COMMANDS_TO_ARG_PARSER.keys():
            raise InvalidMessageError(f"Unknown command '{cmd.strip()}'")

        return Command(cmd, COMMANDS_TO_ARG_PARSER[cmd.strip().casefold()](rest))
