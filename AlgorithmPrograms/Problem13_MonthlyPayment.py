"""This program calculate monthlyPayment that reads in three
command-line arguments P, Y, and R and calculates the monthly payments you
would have to make over Y years to pay off a P principal loan amount at R per cent
interest compounded monthly.

@author Amit Kumar
@version 1.0
@since 03/01/2019
"""
# importing important modules
import sys

global principal, rate1, year1


# function which calculates the monthly payment contains @param principal loan, @param rate and @param year
def monthly_payment(principal_loan, rate, year):
    n = 12 * year
    r = rate / (12*100)
    payment = (principal_loan * r)/(1 - (1+r) ** (-n))
    print("Monthly Payment is: ", float(payment))


# taking values principal, rate and year as through command-line argument and storing them into the variables
try:
    principal = float(sys.argv[1])
    rate1 = float(sys.argv[2])
    year1 = float(sys.argv[3])
except Exception as e:
    print(e)

# calling the function to calculate the monthly payment
monthly_payment(principal, rate1, year1)
