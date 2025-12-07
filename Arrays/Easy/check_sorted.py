"""
Docstring for Arrays.Easy.check_sorted
Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.
Input : nums = [1, 2, 3, 4, 5]

Output : true

Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.
"""

class Solution:
    def isSorted(self, nums):
        #your code goes here
        sorted_flg = True
        ## initalising the temporary value with the first value
        prev_val = nums[0]

        for num in nums:
            # checking whether the cur_value is less than the previous value
            if num < prev_val:
                sorted_flg = False
                break
            # assigning the current val as prev_value
            prev_val = num
        
        return sorted_flg


if __name__ == '__main__':
    solution = Solution()
    input_list = list(map(int, input("Enter the list of integers separated by space: ").strip().split(" ")))
    is_sorted = solution.isSorted(input_list)
    print(is_sorted)