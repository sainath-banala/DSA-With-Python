"""
Docstring for Basics.patterns.number_pattern
--> 2n - 1 rows and 2n -1 columns
--> row = 0 or row = 2n-1 and col = 0 or col = 2n - 1 ---> print(n)
--> row = 1 and  
"""

"""
basic problem:
consider n * n matrix
--> After seeing n*n matrix on paper, found that min of row, col is the subtracted from the integer to get the value
n = int(input("Enter the integer value: "))
for row in range(n):
    for col in range(n):
        print(n-min(row, col), end="")
    print("")
"""

n = int(input("Enter the integer value: "))

for row in range(2*n - 1):

    for col in range(2*n - 1):
        temp_row = 2*n - 2 - row if row >= n else row
        temp_col =  2*n - 2 - col if col >= n else col
        # if col <= n:
        print(n-min(temp_row, temp_col), end="")

    print("")