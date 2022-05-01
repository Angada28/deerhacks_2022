from sympy import Eq
from dataclasses import dataclass
from parse_sympy_expr import parse_sympy_expr
from typing import Any

class SumArgs:
    exp: str
    upper: str
    lower: str
    var: str

    def __init__(self, e, u, l, v):
        self.exp = e
        self.upper = u
        self.lower = l
        self.var = v

def parse_summation(args: str) -> Any:
    try:
        _args = args.split("where", maxsplit=1)
        exp = _args[0]
        _args2 = _args[1].split("between", maxsplit=1)
        var = _args2[0]
        bounds = _args2[1].split("and", maxsplit=1)
        lower = bounds[0]
        upper = bounds[1]
        exp = exp.strip()
        upper = upper.strip()
        lower = lower.strip()
        var = var.strip()
    except IndexError:
        return None

    return SumArgs(exp, upper, lower, var)

