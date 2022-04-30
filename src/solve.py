from parse_solve import SolveArgs
from sympy import solveset, symbols, Eq

def solve(args: SolveArgs):
    assert isinstance(args, SolveArgs)
    eqnl, eqnr = args.eqn.lhs, args.eqn.rhs
    for subst in args.where:
        eqnl = eqnl.subs(subst[0], subst[1])
        eqnr = eqnr.subs(subst[0], subst[1])
    return solveset(Eq(eqnl, eqnr), symbols(args.var))


if __name__ == "__main__":
    from parse import Parser
    from commands import dispatch_command
    print(dispatch_command(Parser().parse("$deermath solve x + y + z = 20 where x=2y, y = 3z for z")))
