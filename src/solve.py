from parse_solve import SolveArgs
from sympy import solveset, symbols

def solve(args: SolveArgs):
    assert isinstance(args, SolveArgs)
    return solveset(args.eqn, symbols(args.var))


