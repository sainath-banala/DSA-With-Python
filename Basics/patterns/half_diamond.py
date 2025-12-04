"""
right angled triangle + inverted right angled triangle
* 
* *
* * *
* * * *
* * *
* *
*
"""
n = int(input("Enter the integer value: "))

for row in range(1,n+1):
    for col in range(row):
        print("*", end=" ")
    # printing a new line
    print("")

# since there is only one centre line(from the first row we will print integer - row - 1 stars)
for row in range(n):
    for col in range(n-row-1):
        print("*", end=" ")
    # printing a new line
    print("")