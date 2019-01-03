"""Program to compute the square root of a non-negative number c
given in the input using Newton's method.

@author Amit Kumar
@version 1.0
@since 03/01/2019
"""


# function to calculate the square root of a user-input number contains @param number, @param t and @param epsilon
# which @return value t which is square root of the given number.
def sqrt(no, t, epsilon):
    while abs(t-no/t) > epsilon * t:
        t = (no / t + t) / 2.0
    return t


epsilon1 = 1e-15  # declaring the constant value of epsilon
c = int(input("\nEnter the Number: "))
t1 = c  # assigning the value of user-input value c to t1 for further calculation
res = sqrt(c, t1, epsilon1)  # calling the function
print("\nSquare root of ", c, ": ", res)
