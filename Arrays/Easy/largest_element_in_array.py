"""
Docstring for Arrays.Easy.largest_element_in_array
Input: nums = [3, 3, 6, 1]

Output: 6

Explanation: The largest element in array is 6
"""
class Solution:
    def largestElement(self, nums):
        max_element = nums[0]
        for i in range(len(nums)):
            if nums[i] > max_element:
                max_element = nums[i]
        return max_element


if __name__ == '__main__':
    solution = Solution()
    input_list = list(map(int, input("Enter the list of integers separated by space: ").strip().split(" ")))
    solution.largestElement(input_list)
