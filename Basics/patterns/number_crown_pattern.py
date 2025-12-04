"""
Docstring for Basics.patterns.number_crown_pattern (integers + spaces(reducing 2 spaces for every row) + reverse integers )
1         1 
1 2     2 1
1 2 3 3 2 1
for n = 4, for first line spaces are coming as 2*n - 2*row - 2 (reducing 2 spaces for every row)
"""
n = int(input("Enter the integer value: "))

for row in range(1, n):
    # first numbers
    for col in range(1,row+1):
        print(col, end=" ")

    # spaces (got by calculating manually for one problem)
    for col in range(2*n- 2 - 2*row): 
        print(" ", end=" ")

    # last numbers (reverse printing the numbers)
    for col in range(row, 0, -1):
        print(col, end=" ")
    print("")
     