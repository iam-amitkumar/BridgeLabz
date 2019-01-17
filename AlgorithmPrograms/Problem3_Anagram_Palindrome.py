"""Anagram_Palindrome program checks whether the given prime number
is anagram as well as palindrome or not

@author Amit Kumar
@version 1.0
@since 02/01/2019
"""
# importing important modules
import utility.Utility
import util.Util

global num

try:
    num = utility.Utility.get_integer()
except Exception as e:
    print(e)

res = False
print("\nPrime number which are palindrome and anagram up to", num, ": ")
for i in range(2, num):
    if util.Util.is_prime(i) and util.Util.is_palindrome(i):
        print(i, end=" ")
print()
