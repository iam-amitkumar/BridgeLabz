""" Quadratic equation is used to find the roots of the equation a*x*x + b*x + c.
Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
can be found using a formula

@author Amit Kumar
@version 1.0
@since 01/01/2019
"""
# import important modules
import utility.Utility
print("Please enter the value of a(a should not be 0): ")
a = utility.Utility.get_float()
print("Please enter the value of b: ")
b = utility.Utility.get_float()
print("Please enter the value of c: ")
c = utility.Utility.get_float()
print(utility.Utility.quad_equation(a, b, c))
