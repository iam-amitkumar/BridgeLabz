"""Util module contains all the important or commonly
used functions which can be further used in the
programs by importing this module.

@author Amit Kumar
@version 1.0
@since 02/01/2019
"""
import utility.Utility

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
    for i in range(2, int(num/2)):  # propagating from  number 2 to the given number
        if num % i == 0:  # checking check whether any number is divisible by any other number except 1 or itself
            count += 1  # incrementing the value of count if the number is divisible by any other number
    if count == 0:  # returning true if the value of count is zero, i.e., number is not divisible by any other number
        return True


# this function returns boolean value depending on the result whether the given number is palindrome or not
def is_palindrome(num):
    temp = num  # storing the number into a temporary variable to compare it with the reversed number
    r = 0
    while num != 0:
        rev = int(num % 10)  # picking up the last number
        r = r * 10 + rev  # reversing the number
        num = int(num / 10)  # trimming the last number
    if temp == r:  # comparing the reversed number with the given number, if matches then return True
        return True


def temperature_conversion(option):
    if option == 1:
        print("\nEnter the temperature in Celcius: ")
        temp = utility.Utility.get_float()
        res = float((temp*9/5)+32)
        return res
    elif option == 2:
        print("\nEnter the temperature in Fahrenheit: ")
        temp = utility.Utility.get_float()
        res = float((temp-32)*5/9)
        return res
    else:
        print("Invalid input")


def to_binary(dec):
    binary = " "
    while dec != 0:
        rev = int(dec % 2)
        binary = str(rev) + binary
        dec = int(dec / 2)
    return binary


def to_decimal(binary):
    dec = 0
    count = 0
    while binary != 0:
        r = int(binary % 10)
        dec = dec + r * (2 ** count)
        count += 1
        binary = int(binary / 10)
    return int(dec)
