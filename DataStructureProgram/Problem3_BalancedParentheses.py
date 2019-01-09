"""Take an Arithmetic Expression where parentheses are used to order the
performance of operations. Ensure parentheses must appear in a balanced
fashion.

@author Amit Kumar
@version 1.0
@since 08/01/2019
"""

# importing important modules
from DataStructureProgram.Stack import *

s1 = Stack()  # creating object of Stack class


# this function checks whether the string given by the user has balanced parentheses or not, on that basis return
# boolean value
def check_bal(exp1):
    for i in range(0, len(exp1)):
        if exp1[i] == '(' or exp1[i] == '{' or exp1[i] == '[':  # pushing in stack if string contain open parentheses
            s1.push(exp1[i])
        try:
            if exp1[i] == ')':
                x = s1.pop()  # popping the stored open parentheses if any close parentheses found in the string
                if x != '(':
                    return False
            elif exp1[i] == '}':
                x = s1.pop()  # popping the stored curly braces if any close curly braces found in the string
                if x != '{':
                    return False
            elif exp1[i] == ']':
                x = s1.pop()  # popping the stored brackets if any close brackets found in the string
                if x != '[':
                    return False
        except Exception as e1:  # handling the exception of "Stack Underflow"
            print(e1)


global exp
try:
    exp = input("Please enter your expression")
except Exception as e:
    print(e)

check = check_bal(exp)

if s1.is_empty() and check:  # printing the result if function return True otherwise False
    print("\n>>> Your expression is balanced <<<")
# elif s1.is_empty():  # if the user-input string don't has any parentheses then print "Balanced"
#     print("\n>>> Your expression is balanced <<<")
else:
    print("\n>>> Your expression is not balanced <<<")
