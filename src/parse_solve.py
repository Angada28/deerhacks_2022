from sympy import Eq, Expr
from dataclasses import dataclass
from parse_sympy_expr import parse_sympy_expr
from typing import Any, List, Tuple

from parse_where_clause import parse_where


@ dataclass
class SolveArgs:
    var: str
    eqn: Eq
    where: List[Tuple[Expr, Expr]]


def parse_equation(eqn: str) -> Eq:
    if '=' in eqn:
        lhs, rhs = eqn.split('=')
        return Eq(parse_sympy_expr(lhs), parse_sympy_expr(rhs))
    # In lieu of an equal sign, we equate the expression to zero...
    return Eq(parse_sympy_expr(eqn), 0)

def parse_solve(args: str) -> Any:
    fragments = list(map(lambda s: s.strip().casefold(), args.split()))


    kw = None
    eqn_list = []
    for_list = []
    where_list = []
    for fragment in fragments:
        if fragment == "for".casefold():
            kw = "for"
        elif fragment == "where".casefold():
            kw = "where"
        else:
            if kw is None:
                eqn_list.append(fragment)
            elif kw == "for":
                for_list.append(fragment)
            elif kw == "where":
                where_list.append(fragment)
    
    eqn = ' '.join(eqn_list)
    for_clause = ' '.join(for_list) if for_list != [] else 'x'
    where_clause = ' '.join(where_list)
    
    return SolveArgs(for_clause, parse_equation(eqn), parse_where(where_clause))

