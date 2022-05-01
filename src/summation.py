from parse_summation import SumArgs
from typing import Union
from sympy.abc import i, k, m, n, x
from sympy import Sum, factorial, oo, IndexedBase, Function, symbols, pretty_print


def summation(args: Union[SumArgs, None], state):
    if args is None:
        return 0
    else:
        return Sum(args.exp, (args.var, args.lower, args.upper)).doit()


