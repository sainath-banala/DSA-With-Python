"""
Docstring for Basics.patterns.start_pyramid
patten 5(right pyramid of spaces(row number - 1) + inverted left angled triangle of stars(total no. of lines - row number + 1) + inverted right angled of stars(total no. of lines - row number) ):
* * * * * * * 
  * * * * *
    * * *
      *
"""
n = int(input("Enter the integer value: "))

for row in range(1, n+1):
    # right pyramid of spaces
    for col in range(row-1):
        print(" ", end=" ")
    
    # inverted left angled triangle of stars
    for col in range(n - row + 1):
        print("*", end=" ")
    
    # inverted right angled of stars
    for col in range(n - row):
        print("*", end=" ")
    
    print("")
    