# importing important modules
import utility.Utility

num = utility.Utility.get_integer()
NthSum = 0.0
for i in range(1, num+1):  # iterating the value of i from 1 to N
    NthSum = NthSum + (1/i)  # adding all the inverted natural number up to N
print("\n", num, "Harmonic Number: ", NthSum)
