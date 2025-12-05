"""
Docstring for Basics.patterns.symmetric_butterfly_pattern
--> upper part: (right angled pyramid of stars + spaces + left angled pyramid of stars)
--> lower part: (inverted right angled pyramid of stars + spaces + left angled pyramid of stars)
*             * 
* *         * *
* * *     * * *
* * * * * * * *
* * *     * * *
* *         * *
*             *
"""

n = int(input("Enter the integer value: "))

## upper part
for row in range(1, n+1):
    # right angled pyramid of stars
    for col in range(row):
        print("* ", end="")

    # spaces(since we are maintaining spaces after stars, we are giving two spaces)
    for col in range(2*n - 2*row):
        print("  ", end="")
    
    # left angled pyramid of stars
    for col in range(row):
        print("* ", end="")
    
    print("")


# lower part (n-1 lines as in the middle we are having only straight line that we covered in the upper part)
for row in range(n-1, 0, -1):
    # inverted right angled pyramid
    for col in range(row):
        print("* ", end="")
    
    # spaces (2(n-row))
    for col in range(2*n - 2*row):
        print("  ", end="")
    
    # inverted left angled pyramid
    for col in range(row):
        print("* ", end="") 
    
    print("")