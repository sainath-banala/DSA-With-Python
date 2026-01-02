"""
Docstring for Arrays.Easy.valid_parantheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false
# from the examples go to know that, 
# if a open paratheses came, after that the same closing parantheses should come, or a new open parantheses should come, not any other closing parantheses 
after ( --> [ or ) != ] or }
"""
class Solution:
    def isValid(self, s: str) -> bool:
        open_parantheses = ["(", "[", "{"]
        close_parantheses = [")", "]", "}"]
        # considering ( as 1, ) as -1, [ as 2, ] as -2, { as 3, } as -3
        current_stack = []
        for character in s:
            if character in open_parantheses: 
                current_stack.append(character)
            elif character in close_parantheses and len(current_stack) !=0 and current_stack[-1] == open_parantheses[close_parantheses.index(character)]:
                current_stack.pop(-1)
            elif character in close_parantheses:
                return False
        
        if len(current_stack) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    input_string = input("Enter the chars")
    print(solution.isValid(input_string))