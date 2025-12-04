"""
Diamond
star_pyramid + inverted_star_pyramid
      * 
    * * * 
  * * * * * 
* * * * * * * 
* * * * * * * 
  * * * * * 
    * * * 
      * 
"""

n = int(input("Enter the integer value: "))

for row in range(1, n+1):
    # right pyramid of spaces
    for col in range(n-row):
        print(" ", end=" ")
    
    # left angled triangle of stars
    for col in range(row):
        print("*", end=" ")
    
    # right angled of stars
    for col in range(row-1):
        print("*", end=" ")
    
    print("")

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