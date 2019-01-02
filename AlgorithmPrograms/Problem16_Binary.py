import utility.Utility
import util.Util


def eight_bits(s):
    length_s = len(s)
    while length_s < 9:
        s = str(0)+s
        length_s = len(s)
    return s


number = utility.Utility.get_integer()
print("I.")
binary_converted = util.Util.to_binary(number)
eight_bit_converted = eight_bits(binary_converted)
print("8-bit representation of ", number, ": ", eight_bit_converted)

list1 = list(eight_bit_converted)
first_nibble = list1[0:4]
fir_nibble = ''.join(first_nibble)
print("\nFirst half Nibble: ", fir_nibble)
second_nibble = list1[4:8]
sec_nibble = ''.join(second_nibble)
print("Second half Nibble: ", sec_nibble)
reversed_nibble = second_nibble + first_nibble
rev_nibble = ''.join(reversed_nibble)
print("\nReversed Nibble: ", int(rev_nibble))
print("\nDecimal representation of", rev_nibble, ": ", util.Util.to_decimal(int(rev_nibble)))
print("II.")

