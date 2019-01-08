"""this program creates Banking Cash Counter where people
come in to deposit Cash and withdraw Cash. It have an input panel to add people
to Queue to either deposit or withdraw money and de-queue the people maintaining
the Cash Balance.

@author Amit Kumar
@version 1.0
@since 08/01/2019
"""
# importing important modules
from DataStructureProgram.Queue import *
# creating the object of Queue class
q1 = Queue()
global opinion, amount, size_of_queue  # globalizing the variables
amt_of_money = 1000  # initializing the bank balance
print("\nYour cleared balance: ", amt_of_money)
try:  # handling the invalid user input for "size of the queue"
    size_of_queue = int(input("\nEnter the size of the queue: "))
except Exception as e:
    print(e)

# initialing the queue
try:
    for i in range(size_of_queue):
        q1.enqueue(i)
    q1.display()
except Exception as e:
    print(e)

# processing the steps until the queue even a single element
while q1.is_empty() is False:
    print("\nEnter your opinion: \n"
          "1. Press 1 to deposit\n"
          "2. Press 2 to withdraw\n")
    try:  # handling the invalid user input for "opinion of user"
        opinion = int(input("Enter your opinion: "))
    except Exception as e:
        print(e)
    try:
        if opinion == 1:  # checking for the input of the user, whether to deposit or withdraw
            try:  # handling the invalid user input for "amount to deposit"
                amount = int(input("Enter the amount you want to deposit in the account: "))
            except Exception as e:
                print(e)
            if amount < 0:
                print("Enter a valid amount")
            else:
                amt_of_money += amount  # adding the money to the account
                print("Remaining balance: ", amt_of_money)
                q1.de_queue()
        elif opinion == 2:  # checking for the input of the user, whether to deposit or withdraw
            try:  # handling the invalid user input for "amount to withdraw"
                amount = int(input("Enter the amount you want to withdraw from the account: "))
            except Exception as e:
                print(e)
            if amount < 0:
                print("!!! Enter a valid amount !!!")
                print("Remaining balance: ", amt_of_money)
            else:
                if (amt_of_money - amount) < 0:
                    print("\n>>> Don't have sufficient balance, reenter withdraw amount or Deposit first. <<<")
                    print("Remaining balance: ", amt_of_money)
                else:
                    amt_of_money -= amount  # deducting the amount of money from the account
                    print("Remaining balance: ", amt_of_money)
                    q1.de_queue()
        else:
            print("Invalid Input !!!")
    except Exception as e:
        print(e)

# printing final available balance present in the account
print("\n>>> Available Balance :", amt_of_money, " <<<")
