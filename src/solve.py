from parse_solve import SolveArgs
from sympy import solveset, symbols, Eq
from sympy import solve as sympy_solve

def solve(args: SolveArgs, state):
    assert isinstance(args, SolveArgs)
    
    eq_tuples = [(e.lhs, e.rhs) for e in args.eqn]
    for i in range(len(eq_tuples)):
        for subst in args.where:
            eqnl, eqnr = eq_tuples[i]
            eqnl = eqnl.subs(subst[0], subst[1])
            eqnr = eqnr.subs(subst[0], subst[1])
            eq_tuples[i] = (eqnl, eqnr)

    if len(eq_tuples) == 1:
        el, er = eq_tuples[0]
        vars = args.var if args.var != "" else 'x'
        return solveset(Eq(el, er), symbols(vars))
    else:
        # Note solveset doesn't support systems of equations yet.
        return sympy_solve([Eq(el, er) for el, er in eq_tuples], symbols(args.var))

if __name__ == "__main__":
    from parse import Parser
    from commands import dispatch_command
    print(dispatch_command(Parser().parse("$deermath solve x + y + z = 20 where x=2y, y = 3z for z"), ()))
    print(dispatch_command(Parser().parse("$deermath solve x + y = 10, x - y = z, z=5 for x, y, z"), ()))
