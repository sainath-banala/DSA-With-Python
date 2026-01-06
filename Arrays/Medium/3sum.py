"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Solution: first we are sorting so the given array, and fixing one value and checking any other two values in the array with its sum with fixed_value returns to zero
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output_list = []
        n = len(nums)
        # sorting the list
        nums.sort()
        for i in range(n):
            # Skip duplicate fixed values
            if i > 0 and nums[i] == nums[i-1]:
                continue  # Skip this iteration
            # Early termination: if fixed value > 0, all remaining positive
            if nums[i]  > 0:
                break 
            cur_val = nums[i]
            left_index = i+1
            right_index = n - 1
            while left_index < right_index:
                cur_sum = nums[left_index] + nums[right_index] + cur_val
                if cur_sum < 0:
                    left_index += 1
                elif cur_sum > 0:
                    right_index -= 1
                else:                        
                    # when sum == 0:
                    output_list.append([cur_val, nums[left_index], nums[right_index]])

                    # Skip duplicate left values
                    while left_index < right_index and nums[left_index] == nums[left_index + 1]:
                        left_index += 1
                        
                    # Skip duplicate right values  
                    while left_index < right_index and nums[right_index] == nums[right_index - 1]:
                        right_index -= 1
                        
                    # Move both pointers as already both left_indexed and right_indexed value included in the triplet
                    left_index += 1
                    right_index -= 1
                    

if __name__ == '__main__':
    solution = Solution()
    input_list = list(map(int, input("Enter the list of integers separated by space: ").strip().split(" ")))
    triplets = solution.three_sum(input_list)
    print(triplets)