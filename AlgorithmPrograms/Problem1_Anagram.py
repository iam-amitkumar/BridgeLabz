"""Anagram program checks whether the given user-input
strings are anagram or not.

@author Amit Kumar
@version 1.0
@since 02/01/2019
"""
# importing important modules
import utility.Utility
import util.Util

global s1, s2

try:
    s1 = utility.Utility.get_string()
    s2 = utility.Utility.get_string()
except Exception as e:
    print(e)

res = util.Util.is_anagram(s1, s2)
if res is True:  # checking whether the function returns true or not, of true then both the strings are anagram
    print("\n", s1, "and ", s2, " are anagram string")
else:
    print("\n", s1, "and ", s2, " are not anagram string")
