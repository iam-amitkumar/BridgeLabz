import sys


def monthly_payment(principal_loan, rate, year):
    n = 12 * year
    r = rate / (12*100)
    payment = (principal_loan * r)/(1 - (1+r) ** (-n))
    print("Monthly Payment is: ", float(payment))


principal = float(sys.argv[1])
rate1 = float(sys.argv[2])
year1 = float(sys.argv[3])
monthly_payment(principal, rate1, year1)
