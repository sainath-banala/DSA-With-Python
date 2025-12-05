"""
Docstring for Basics.patterns.start_pyramid
patten 4(inverted right pyramid of spaces(total no. of lines - row number) + left angled triangle of stars(as many as the row number) + right angled of stars(row - 1 stars) ):
one more way is spaces + stars (in each row: (n - row) spaces + (2*(row - 1) + 1) stars  )

      * 
    * * *
  * * * * *
* * * * * * *
"""
n = int(input("Enter the integer value: "))

# for row in range(1, n+1):
#     # right pyramid of spaces
#     for col in range(n-row):
#         print(" ", end=" ")
    
#     # left angled triangle of stars
#     for col in range(row):
#         print("*", end=" ")
    
#     # right angled of stars
#     for col in range(row-1):
#         print("*", end=" ")

for row in range(1, n+1):
    # right pyramid of spaces
    for col in range(n-row):
        print(" ", end=" ")
    
    # (2*(row - 1) + 1) stars
    for col in range(2*(row - 1)+1):
        print("* ", end="")
    
    print("")
    