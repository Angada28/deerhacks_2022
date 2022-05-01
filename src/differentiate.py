from parse_differentiate import DiffArgs
import sympy


def differentiate(args: DiffArgs,temp):
    return sympy.diff(args.fn, sympy.symbols(args.var))
