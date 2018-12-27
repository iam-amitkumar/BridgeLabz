""" HeadTail program gives the output of percentage of tails and heads
occured, on the basis of number of tails and heads occured the flips of
coin N times where N is an user input integer.

@author Amit Kumar
@version 1.0
@since 26/12/2018
"""
# Importing important package
import utility.Utility
import random

tail = 0
head = 0

# taking user input to determine that how many times coin will flip
number_of_flips = utility.Utility.get_integer()

for i in range(0, number_of_flips):
    rand = random.random()
    if rand < 0.5:
        tail += 1
    else:
        head += 1

tail_percent = tail/(tail+head)*100
head_percent = head/(head+tail)*100

print("\nNo. of Tails: ", tail, " out of ", number_of_flips)  # printing no. of tails occurred out of total flips
print("No. of Heads: ", head, " out of ", number_of_flips)  # printing no. of heads occurred out of total flips

print("\nPercentage of Tails: ", tail_percent, "%")  # printing percentage of tails
print("Percentage of Heads: ", head_percent, "%")  # printing percentage of heads
