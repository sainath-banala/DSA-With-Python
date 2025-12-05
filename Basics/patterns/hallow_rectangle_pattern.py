"""
Docstring for Basics.patterns.hallow_rectangle_pattern
--> n-1 rows, 
--> first and last rows of stars and 
--> first and last columns of stars
--> remaining spaces
n=4
* * * 
*   *
* * *
n=5
* * * * 
*     *
*     *
* * * *
"""

n = int(input("Enter the integer value: "))

for row in range(n-1):
    for col in range(n-1):
        # first and last rows of stars
        if row == 0 or row == n-2:
            print("* ", end="")
        # first and last columns of stars
        elif col == 0 or col == n-2:
            print("* ", end="")
        # since we are keeping spaces after stars we are inserting two spaces
        else:
            print("  ", end="")
    print("")

    

