"""
Docstring for Basics.basic_math.count_digits
Example 1:
Input:N = 12345
Output:5
Explanation:  The number 12345 has 5 digits.
"""
import math

num = int(input("Enter the integer N: "))

temp = num
count = 0

################################# brute force #################
# while temp > 0:
#     temp = temp // 10
#     print(temp)
#     count += 1

################## optimal approach #########################
# Initialize a variable 'count' to
# store the count of digits.
count = int(math.log10(num) + 1) ## this will work only if the integer is greater than 0

# The expression int(math.log10(n) + 1)
# calculates the number of digits in 'n'
# and casts it to an integer.

# Adding 1 to the result accounts
# for the case when 'n' is a power of 10,
# ensuring that the count is correct.

# Finally, the result is cast
# to an integer to ensure it is rounded
# down to the nearest whole number.

print(f"count of integers: {count}")