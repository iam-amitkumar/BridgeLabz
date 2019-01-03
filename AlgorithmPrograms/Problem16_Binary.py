"""Binary is a program to read an integer as an Input, convert to Binary using toBinary
function and perform the following functions:
i. Swap nibbles and find the new number.
ii. Find the resultant number is the number is a power of 2.

@author Amit Kumar
@version 1.0
@since 03/01/2019
"""
# importing important modules
import utility.Utility
import util.Util


# function to convert any bit binary value to the 8-bit binary value with @param string and @return string of 8-bit
def eight_bits(s):
    length_s = len(s)
    while length_s < 9:
        s = str(0)+s  # concatenating string type zero until the binary value converted into 8-bit
        length_s = len(s)  # assigning the current length of string to again check it in while loop
    return s  # returning 8-bit binary value


# function to check whether the @param num is a power of 2 or not with @return boolean value
def is_power_of_two(num):
    for i in range(1, int(num/2)):
        if 2 ** i == num:
            return True  # return True if the @param is power of 2
    return False  # # return False if the @param is not power of 2


number = utility.Utility.get_integer()

# solution of first bit of the question
print("\nI.")
# converting the user-input number to the binary value
binary_converted = util.Util.to_binary(number)
# converted binary value to the 8-bit binary value to swap the nibbles
eight_bit_converted = eight_bits(binary_converted)
print("8-bit representation of ", number, ": ", eight_bit_converted)
# converting the 8-bit binary value into list to divide it into two 4-bits
list1 = list(eight_bit_converted)

first_nibble = list1[0:4]  # slicing the list to get first nibble(4-bits) and storing it into a variable first_nibble
fir_nibble = ''.join(first_nibble)  # converting sliced list into string
print("\nFirst half Nibble: ", fir_nibble)
second_nibble = list1[4:8]  # slicing the list to get second nibble(4-bits) and storing it into a variable second_nibble
sec_nibble = ''.join(second_nibble)  # converting sliced list into string
print("Second half Nibble: ", sec_nibble)

reversed_nibble = second_nibble + first_nibble  # reversing the nibbles by swapping both the sliced list(nibbles)
rev_nibble = ''.join(reversed_nibble)  # converting the reversed list into list
print("\nReversed Nibble: ", int(rev_nibble))
dec_value = util.Util.to_decimal(int(rev_nibble))
print("\nDecimal representation of", rev_nibble, ": ",dec_value)  # converting reversed
# nibbles of binary value again into decimal

# solution of second bit of the question
print("\nII.")
if is_power_of_two(dec_value):
    print("Yes, the resultant number is power of 2.")
else:
    print("No, the resultant number is not power of 2.")

