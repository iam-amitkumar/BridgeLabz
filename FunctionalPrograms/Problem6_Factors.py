"""Factors program compute the prime factorization of N using
brute force and print the prime factors of N.

@author Amit Kumar
@version 1.0
@since 28/12/2018
"""
# Importing important modules
import utility.Utility

num = utility.Utility.get_integer()  # getting user input through function call
print("\nPrime factors of", num, "are: ")
for i in range(2, num+1):
    while num % i == 0:  # checking whether the current value 'i' is divisible by num or not
        print(i)  # if the 'i' is divisible then it will print the value of 'i' because it is prime factor of num
        num = num/i  # getting the quotient after dividing for further modulo check
if num > 1:  # checking if last prime factor is greater than 1 or not, if yes then print it
    print(num)
