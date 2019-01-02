import utility.Utility
import util.Util

print("\nPlease enter your option: \n1. Press 1 to convert Celsius to Fahrenheit \n2. Press 2 to convert "
      "Fahrenheit to Celsius \n")
t = utility.Utility.get_float()
print("Temperature: ", util.Util.temperature_conversion(t))
