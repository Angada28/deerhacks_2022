from sympy import Eq
from dataclasses import dataclass
from parse_sympy_expr import parse_sympy_expr
from typing import Any




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
