"""
Docstring for Arrays.Easy.contains_duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_mapper = {}
        for num in nums:
            if nums_mapper.get(num) == "exist":
                # indicates that the element already existed appeared twice
                return True
            else:
                nums_mapper[num] = "exist"
        # indicates no duplicates 
        return False

if __name__ == '__main__':
    solution = Solution()
    input_list = list(map(int, input("Enter the list of nums separated by space: ").strip().split(" ")))
    print(solution.containsDuplicate(input_list))
    