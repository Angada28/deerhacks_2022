
from sympy import Eq, Expr
from dataclasses import dataclass
from parse_sympy_expr import parse_sympy_expr
from typing import Any, List, Tuple

@dataclass
class SimplifyArgs:
    expr: Expr
    where: List[Tuple[Any, Any]]

def parse_where(where_clauses):
    out = []
    clauses = where_clauses.split(',')
    for c in clauses:
        if '=' in c:
            lhs, rhs = c.split('=')
            out.append((parse_sympy_expr(lhs), parse_sympy_expr(rhs)))
    return out

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
