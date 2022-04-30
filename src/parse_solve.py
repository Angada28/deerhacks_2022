from sympy import Eq, parse_expr
from sympy.parsing.sympy_parser import standard_transformations, convert_xor, split_symbols, implicit_multiplication_application
from dataclasses import dataclass
from typing import Any


def parse_sympy_expr(e):
    return parse_expr(
        e,
        transformations=([t for t in standard_transformations] + [convert_xor, implicit_multiplication_application]))


@ dataclass
class SolveArgs:
    var: str
    eqn: str


def parse_equation(eqn: str) -> Eq:
    if '=' in eqn:
        lhs, rhs = eqn.split('=')
        return Eq(parse_sympy_expr(lhs), parse_sympy_expr(rhs))
    return Eq(parse_sympy_expr(eqn), 0)


def parse_solve(args: str) -> Any:
    fragments = list(map(lambda s: s.strip().casefold(), args.split()))

    # solve eqn for ...
    if "for".casefold() in fragments:
        idx = fragments.index("for".casefold())
        eqn = ' '.join(fragments[:idx])
        var = fragments[idx + 1]

        return SolveArgs(var, parse_equation(eqn))

    # solve eqn (assumes variable is x)
    return SolveArgs('x', parse_equation(' '.join(fragments)))
