from parse_differentiate import DiffArgs
import sympy


def differentiate(args: DiffArgs):
    assert (args, DiffArgs)
    return sympy.diff(args.fn, sympy.symbols(args.var))
