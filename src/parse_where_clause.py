from parse_sympy_expr import parse_sympy_expr


def parse_where(where_clauses):
    out = []
    clauses = where_clauses.split(',')
    for c in clauses:
        if '=' in c:
            lhs, rhs = c.split('=')
            out.append((parse_sympy_expr(lhs), parse_sympy_expr(rhs)))
    return out