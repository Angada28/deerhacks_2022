from sympy.parsing.sympy_parser import standard_transformations, convert_xor, \
    split_symbols, implicit_multiplication_application
from dataclasses import dataclass
from typing import Any
from sympy import parse_expr


@dataclass
class DiffArgs:
    var: str
    fn: Any


def parse_differentiate(args: str) -> Any:
    fragments = list(map(lambda s: s.strip().casefold(), args.split()))

    if "for".casefold() in fragments:
        idx = fragments.index("for".casefold())
        eqn = ' '.join(fragments[:idx])
        var = fragments[idx + 1]

        return DiffArgs(var, parse_expr(eqn,transformations=(
                [t for t in standard_transformations] + [convert_xor,
                                                         implicit_multiplication_application])))

    # solve eqn (assumes variable is x)
    return DiffArgs('x', parse_expr(' '.join(fragments),transformations=(
            [t for t in standard_transformations] + [convert_xor,
                                                     implicit_multiplication_application])))
