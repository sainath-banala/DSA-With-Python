"""
Docstring for Basics.patterns.inverted_right_pyramid
pattern 3:
* * * * 
* * *
* *
*

1 2 3 4 
1 2 3
1 2
1
"""

n = int(input("Enter the integer value: "))

# for row in range(n):
#     for col in range(n-row):
#         print("*", end=" ")
#     # printing a new line
#     print("")

for row in range(n):
    for col in range(1, n-row+1):
        print(f"{col}", end=" ")
    # printing a new line
    print("")