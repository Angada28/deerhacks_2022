from parse_simplify import SimplifyArgs
from sympy import simplify as sympy_simplify

def simplify(args: SimplifyArgs, state):
    assert isinstance(args, SimplifyArgs)
    expr = args.expr
    for subst in args.where:
        expr = expr.subs(subst[0], subst[1])
    return sympy_simplify(expr)

if __name__ == "__main__":
    from parse import Parser
    from commands import dispatch_command
    print(dispatch_command(Parser().parse("$deermath simplify x + y + z where x=2y, y = 3z")))
