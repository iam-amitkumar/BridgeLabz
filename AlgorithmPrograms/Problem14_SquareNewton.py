

def sqrt(no, t, epsilon):
    while abs(t-no/t) > epsilon * t:
        t = (no / t + t) / 2.0
    return t


epsilon1 = 1e-15
number = int(input("\nEnter the Number: "))
t1 = number
res = sqrt(number, t1, epsilon1)
print("\nSquare root of ", number, ": ", res)
