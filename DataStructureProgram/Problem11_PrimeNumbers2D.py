"""This program take a range of 0 ­ 1000 Numbers and find
the Prime numbers in that range. Store the prime numbers
in a 2D Array, the first dimension represents the range
0­100, 100­200, and so on. While the second dimension
represents the prime numbers in that range.

@author Amit Kumar
@version 1.0
@since 09/01/2019
"""


# this function having @param: num, determine whether the given number is prime or not and on this basis returns
# True or False
def prime_or_not(num):
    for k in range(2, int(num/2)+1):
        if num % k == 0:  # checking for divisibility of any number between 2 and given number
            return False
    else:
        return True


print()
# creating list "prime" of ranges of each rows
prime = [["0-100    :"], ["100-200  :"], ["200-300  :"], ["300-400  :"], ["400-500  :"], ["500-600  :"], ["600-700  :"],
         ["700-800  :"], ["800-900  :"], ["900-1000 :"]]

# appending all the prime numbers in the list
for i in range(2, 1000+1):
    if prime_or_not(i):
        prime[int(i/100)].append(str(i))

# organising all the prime numbers in their respective row according to the value
for i in range(len(prime)):
    for j in range(len(prime[i])):
        print(prime[i][j], end=" ")
    print()
