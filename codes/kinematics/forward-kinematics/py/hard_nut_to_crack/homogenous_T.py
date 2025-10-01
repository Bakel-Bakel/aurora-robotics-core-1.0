from sympy import *

x, y, z = symbols('x y z')

init_printing(use_unicode=True)

print(simplify(sin(x)**2 + cos(x)**2))
c, d, e = symbols("c, d, e")

T1_2 = Matrix([[cos("\u03F4\u2081"),-sin("\u03F4\u2081"), 0, 0],
               [sin("\u03F4\u2081"), cos("\u03F4\u2081"), 0, 0],
               [0,0,1,"L\u2081"],
               [0,0,0,1]])

B = Matrix([[c,d],
            [1, -e]])

C = T1_2 * T1_2
latex_code = latex(C)

print(latex_code)
print(C)