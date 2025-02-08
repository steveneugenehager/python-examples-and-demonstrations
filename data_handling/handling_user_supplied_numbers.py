# 2025-02-08 Steve
#    This is just a musing about the precision of numbers and
#  how to handle them at the edge cases where a float would
#  round up to an integer.
#    Also I looked out how to handle user input where any 
#  decimal representation of zero wouldn't be allowed.

#import math
import re

def is_non_zero_number(s):
    print(f"The input to the function is '{s}'")
    trimmed_trailing_zeros = s.rstrip('0')
    print(f"After trimming trailing zeroes ... '{trimmed_trailing_zeros}'")
    trimmed_trailing_decimals = trimmed_trailing_zeros.rstrip('.')
    print(f"After trimming trailing decimal point(s) ... '{trimmed_trailing_decimals}'")
    # Matches non-zero,positive integers and floats
    pattern = r"^([1-9]\d*|[1-9]\d*\.\d+|\d+\.\d+)$"  
    return bool(re.match(pattern, trimmed_trailing_decimals))

input_age = input("How old are you? ")
print(f"input_age = '{input_age}'")

if ( is_non_zero_number(input_age) ):
    massaged_input = input_age.split('.')[0]
    print(f"massaged_input = '{massaged_input}'")
    age=int(massaged_input)
    print(f"age={age}")

    if ( age >= 18 ):
        print("You are old enough to vote!",end=' ')
        print("Have you registered to vote yet?")
    else:    
        print("You are too young enough to vote!")
else:
    print("ERROR enter a valid positive number.")
exit

# Negative Test cases (not a postive input)
# -0.1
# -0.0000000000000000000000000000000001
# 0
# 00+
# 0.0+

# Negative Test cases (positive but less than 18)
# 0.000000000000000000000000000000000001
# 1..17
# 17.999+

# Positive Test cases
# 18.00000000000000000000000000000001
# 18..[inf]
