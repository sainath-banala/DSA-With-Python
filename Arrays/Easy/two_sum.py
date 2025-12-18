"""
Docstring for Arrays.Easy.two_sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            if target - nums[i] in nums[i+1:]:
                return [i, nums[i+1:].index(target - nums[i])+i+1]


if __name__ == '__main__':
    solution = Solution()
    input_list = list(map(int, input("Enter the list of integers separated by space: ").strip().split(" ")))
    list_of_two_indeces = solution.two(input_list)
    print(list_of_two_indeces)