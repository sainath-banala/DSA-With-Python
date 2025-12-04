"""
Docstring for Basics.patterns.right_triangle with binary_numbers
1 
0 1
0 1 0
1 0 1 0

"""
n = int(input("Enter the integer value: "))
## since the number changes between 0 and 1, we can create one boolean, where not 0 becomes 1 and not 1 becomes 0
initial_bool_val = 1

for row in range(1,n+1):
    for col in range(row):
        print(initial_bool_val, end=" ")
        # converting the False to 0 and True to 1
        initial_bool_val = int(not(initial_bool_val))
    # printing a new line
    print("")