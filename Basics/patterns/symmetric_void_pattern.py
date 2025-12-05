"""
Docstring for Basics.patterns.symmetric_void_pattern
--> upper part - (inverted right angled pyramid of stars + spaces + inverted left angled pyramid of stars)
--> lower part - (right angled pyramid of stars + spaces + left angled pyramid of stars)

* * * * * * * * 
* * *     * * *
* *         * *
*             *
*             *
* *         * *
* * *     * * *
* * * * * * * *
"""
n = int(input("Enter the integer value: "))

for row in range(n):
    # inverted right angled pyramid of stars
    for col in range(n-row):
        print("* ", end="")
    
    # spaces(since we are maintaining spaces after stars, we are giving two spaces)
    for col in range(2*row):
        print("  ", end="")
    
    for col in range(n-row):
        print("* ", end="")
    
    print("")

for row in range(1, n+1):
    # first numbers
    for col in range(1,row+1):
        print("* ", end="")

    # spaces (got by calculating manually for one problem) -- (since we are maintaining spaces after stars, we are giving two spaces)
    for col in range(2*n - 2*row): 
        print("  ", end="")

    # last numbers (reverse printing the numbers)
    for col in range(row):
        print("* ", end="")
    print("")