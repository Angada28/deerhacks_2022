from sympy import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, convert_xor, split_symbols, implicit_multiplication_application

def parse_sympy_expr(e):
    return parse_expr(
        e,
        transformations=([t for t in standard_transformations] + [convert_xor, implicit_multiplication_application]))
