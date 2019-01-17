""" Coupon_Number program gives the output that how many times
random function generated the random number so than distinct N
random number is generated where N is a user-input number.

@author Amit Kumar
@version 1.0
@since 28/12/2018
"""
# importing important modules
import utility.Utility
import random

global number_of_coupons

try:
    number_of_coupons = utility.Utility.get_integer()  # getting input for Number of Coupons
except Exception as e:
    print(e)

list1 = []
count = 0
while len(list1) != number_of_coupons:
    rand = random.randint(1, 10)  # generating random coupons from 1 to 15
    count += 1  # counting the times the random coupons generated
    if rand not in list1:  # checking if the coupon just generated is distinct or not
        list1.append(rand)  # adding the random number to the list "list1" if the generated random number is distinct

# printing the total number of times random number generated
print("\n>>> Random number generated ", count, "times to generate", number_of_coupons, "coupons <<<")
