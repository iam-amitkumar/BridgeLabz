"""Vending_Machine is a Program to calculate the minimum number
of Notes as well as the Notes to be returned by the Vending Machine
as a Change using recursion.

@author Amit Kumar
@version 1.0
@since 02/01/2019
"""
# importing the important modules
import utility.Utility

print("Enter the amount of money you want to withdraw ")
amount1 = utility.Utility.get_integer()
print()


# this method print out minimum number of notes of given amount by the user
def vending_function(amount, notes, i):
        rupees = [1000, 500, 100, 50, 10, 5, 2, 1]
        if amount == 0 and i == len(rupees):
            print("\nTotal number of notes: ", int(notes))
        if i < len(rupees):  # assuring that the index is not incrementing more than the size of the list
            if int(amount / rupees[i]) > 0:  # finding whether current index amount of rupees will dispense or not
                print("note of", rupees[i], " is ", int(amount / rupees[i]))  # printing the total number of "current
                # index amount of rupees"
                notes = int(notes+amount / rupees[i])
                amount = int(amount % rupees[i])  # finding the left amount after printing current index amount
            vending_function(amount, notes, i+1)  # recurring the function while incrementing the index value of rupees


vending_function(amount1, 0, 0)
