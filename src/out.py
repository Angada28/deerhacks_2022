from sympy import simplify, latex, preview, Expr, sympify
from io import BytesIO
from discord import File as DFile

LATEX_PREAMBLE = """
\\documentclass[varwidth]{standalone}
\\usepackage{amsmath,amsfonts}
\\begin{document}\\Huge
"""

def sympy_expr_to_img(expr: Expr) -> BytesIO:
    b = BytesIO()
    preview(expr, output='png', viewer='BytesIO', outputbuffer=b, preamble=LATEX_PREAMBLE)
    b.seek(0, 0)
    return b


def bytes_io_to_discord_file(b: BytesIO) -> DFile:
    return DFile(b, filename="img.png")
