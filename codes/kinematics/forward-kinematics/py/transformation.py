# Importing the init_printing function from the sympy library
# This is used to enable better printing of symbolic expressions, making them easier to read.
from sympy import init_printing

# Initializing pretty printing with Unicode characters for enhanced readability
# This ensures that the symbolic matrix equations and expressions appear in a clean,
# mathematical format.
init_printing(use_unicode=True)
from IPython.display import display

# Importing the symbols function from sympy
# The symbols function allows the creation of symbolic variables that can be used in equations.
# The cos and sin functions are used for symbolic trigonometric calculations.
from sympy import symbols,cos, sin, pprint, simplify

# Importing the Matrix class from sympy's matrices module
# This class is used to create and manipulate matrices
from sympy.matrices import Matrix
import math

#Define all the symbols needed
theta1,theta2,theta4,do,a1,a2,d3 = symbols ("theta1,theta2,theta4,do,a1,a2,d3")

#Define all the transformation matrix
Tb_1 = Matrix([[cos(theta1),-sin(theta1), 0 , 0 ],
               [sin(theta1), cos(theta1), 0 , 0 ],
               [     0     ,     0      , 1 , do],
               [     0     ,     0      , 0 , 1 ]])

T1_2 = Matrix([[cos(theta2),-sin(theta2), 0 , 0 ],
               [sin(theta2), cos(theta2), 0 , a1],
               [     0     ,     0      , 1 , 0 ],
               [     0     ,     0      , 0 , 1 ]])

T2_3 = Matrix([[     1     ,     0      , 0 , 0 ],
               [     0     ,     1      , 0 , a2],
               [     0     ,     0      , 1 , d3],
               [     0     ,     0      , 0 , 1 ]])

T3_e = Matrix([[cos(theta4),-sin(theta4), 0 , 0 ],
               [sin(theta4), cos(theta4), 0 , 0 ],
               [     0     ,     0      , -1 , 0 ],
               [     0     ,     0      , 0 , 1 ]])

#Multiplying all the transformation matrix to get the final matrix
Tb_e = Tb_1 * T1_2 * T2_3 * T3_e

# Simplifying each component of the resulting transformation matrix
Tb_e_simplified = simplify(Tb_e)

# Displaying the simplified transformation matrix
print("  \n\n")
#pprint(Tb_e_simplified)

#pprint(simplify(Tb_1 * T1_2))
pprint(simplify(Tb_1 * T1_2* T2_3))
pprint(simplify(Tb_1 * T1_2* T2_3* T3_e))
