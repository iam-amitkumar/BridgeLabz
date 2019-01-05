"""this program takes a command­line argument N, asks you
to think of a number between 0 and N­1, where N = 2^n, and
always guesses the answer with n questions uses Binary Search
to find the number.

@author Amit Kumar
@version 1.0
@since 04/01/2019
"""
# importing important modules
import math


def question(low, high):
    if (high - low) == 1:  # if range is equal
        return low
    mid = int(high + low) / 2  # find middle value
    print('Is your number less than', mid, '?. press 1 to YES or 0 to NO:')
    a = int(input())
    if a == 1:
        return question(low, mid)  # recursive call for left half
    elif a == 0:
        return question(mid, high)  # recursive call for right half
    else:
        print("Invalid input.. ")
        return 0


noOfTimes = int(input("\nHow much time you want to ask the question:"))
low1 = 0  # assigning low value for further search of the number on the principal of binary search
high1 = int(math.pow(2, noOfTimes))  # assigning high as user-input value on the power of 2
print()
print("Think a number between ", low1, " to ", high1-1, " in range")  # asking the user that their value lies in which
# part of the range, whether in first part or second part and continue this process until we got the number
print()
res = question(low1, high1)  # calling the function
print("\nSurprise!!! Surprise!!! We got it, You guessed :", res)  # printing the result
