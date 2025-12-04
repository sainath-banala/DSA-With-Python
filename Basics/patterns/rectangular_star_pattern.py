"""
Pattern 1:
* * * * 
* * * *
* * * *
* * * *
"""
n = int(input("Enter the integer value: "))

for row in range(n):
    for col in range(n):
        print("*", end=" ")
    # printing a new line
    print("")
