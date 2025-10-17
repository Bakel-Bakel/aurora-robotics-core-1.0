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
theta1,theta2,theta4,do,a1,a2,d3,L_1,L_2 = symbols ("theta1,theta2,theta4,do,a1,a2,d3,L_1,L_2")

#Define all the transformation matrix
TO_A = Matrix([[cos(theta1),-sin(theta1), L_1*cos(theta1)],
               [sin(theta1), cos(theta1), L_1*sin(theta1)],  
               [     0     ,     0      , 1 ]])

TA_E = Matrix([[cos(theta2),-sin(theta2), L_2*cos(theta2)],
               [sin(theta2), cos(theta2), L_2*sin(theta2)],
               [     0     ,     0      , 1 ]])



#Multiplying all the transformation matrix to get the final matrix
TO_E = TO_A * TA_E

# Simplifying each component of the resulting transformation matrix
TO_E_simplified = simplify(TO_E)

# Displaying the simplified transformation matrix
print("  \n\n")
#pprint(TO_E_simplified)

#pprint(simplify(TO_A * TA_E))
pprint(simplify(TO_A * TA_E))

