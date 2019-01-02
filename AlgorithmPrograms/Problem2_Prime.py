"""Prime program prints all the prime numbers up to a
user-input number.

@author Amit Kumar
@version 1.0
@since 02/01/2019
"""
# importing important modules
import utility.Utility
import util.Util

number = utility.Utility.get_integer()
print("\nPrime numbers up to ", number, ": ")
for i in range(2, number):  # checking the prime numbers from 2 to the user-input number
    res = util.Util.is_prime(i)  # passing each number of the range to get the boolean value
    if res is True:  # if the boolean value returned by th function is true then the current passed number is prime
        print(i, end=" ")
print()
