"""TemperatureConversion program converts user-input temperature
from Celcius to Fahrenheit and vice-versa after asking from the user.

@author Amit Kumar
@version 1.0
@since 03/01/2019
"""
# importing important modules
import utility.Utility
import util.Util

global t

# asking from the user whether he/she want to convert from Celcius to Fahrenheit aor vice-versa
print("\nPlease enter your option: \n1. Press 1 to convert Celsius to Fahrenheit \n2. Press 2 to convert "
      "Fahrenheit to Celsius \n")

try:
    t = utility.Utility.get_float()
except Exception as e:
    print(e)

print("Temperature: ", util.Util.temperature_conversion(t))  # printing temperature after passing the user-input
# to the function
