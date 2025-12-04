"""
Docstring for Basics.patterns.right_triangle
pattern 2:
* 
* *
* * *
* * * *

1 
1 2
1 2 3
1 2 3 4

1 
2 2
3 3 3
4 4 4 4

1 
2 3
4 5 6
7 8 9 10
"""
n = int(input("Enter the integer value: "))


# for row in range(1,n+1):
#     for col in range(row):
#         print("*", end=" ")
#     # printing a new line
#     print("")


# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print(f"{col}", end=" ")
#     # printing a new line
#     print("")

# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print(f"{row}", end=" ")
#     # printing a new line
#     print("")

init_var = 1
for row in range(1, n+1):
    for col in range(1, row+1):
        print(init_var, end=" ")
        init_var += 1
    print("")