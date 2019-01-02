"""Util module contains all the important or commonly
used functions which can be further used in the
programs by importing this module.

@author Amit Kumar
@version 1.0
@since 02/01/2019
"""


# this function determine whether the given strings are anagram or not, it gives boolean result depending on result
# contains @param string1 and @param string2 and @returns boolean value
def is_anagram(s1, s2):
    if len(s1) == len(s2):  # checking the length of both strings, if equals then returns True
        return True

    ''.join(sorted(s1))  # sorting both the strings to compare further
    ''.join(sorted(s2))
    for i in range(0, len(s1)):  # comparing both the strings letter by letter, if matches returns True else False
        if s1[i] == s1[i]:
            return True
        else:
            return False


# this function returns True if the number is a Prime Number having @param num and @return boolean value
def is_prime(num):
    count = 0
    for i in range(2, int(num/2)):
        if num % i == 0:
            count += 1
    if count == 0:
        return True







