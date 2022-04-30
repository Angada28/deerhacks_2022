
from sympy import Eq, Expr
from dataclasses import dataclass
from parse_sympy_expr import parse_sympy_expr
from typing import Any, List, Tuple

from parse_where_clause import parse_where

@dataclass
class SimplifyArgs:
    expr: Expr
    where: List[Tuple[Expr, Expr]]



def parse_simplify(args: str) -> Any:
    fragments = list(map(lambda s: s.strip().casefold(), args.split()))

    # simplify expr where A,B,C...
    if "where".casefold() in fragments:
        idx = fragments.index("where".casefold())
        expr = ' '.join(fragments[:idx])
        where = parse_where(' '.join(fragments[idx + 1:]))
    # simplify expr
    else:
        expr = ' '.join(fragments)
        where = []
    return SimplifyArgs(parse_sympy_expr(expr), where)
