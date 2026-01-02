"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
[24,12,4,1]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

--> In the problem itself says, we should not use division operation, that is if we use division operation, we will reach to the solution
therefore: output_element[i] = total_list_product/nums[i]
from this we can get that output_element[i] = multiply(nums[0],nums[1],..nums[i-1]) * multiply(nums[i+1],...nums[n-1])
therefore we shall create two arrays left and right, 
where left will store the multiplication value till before that value
and right will store the multiplication value from after that value to end of the array
"""
class Solution:
    def productExceptSelf_myapproach(self, nums: list[int]) -> bool:
        # starting the left_array and right_array with 1, so that the final output will not change and for handling the base case
        left_array = []
        right_array = []
        final_array = []
        iterable_value = 1
        for i in range(len(nums)):
            if i != 0:
                iterable_value = iterable_value * nums[i-1]
            left_array.append(iterable_value)
            print(left_array)
        
        last_temp_value = 1
        for i in range(len(nums) - 1, -1, -1):
            if i != (len(nums) - 1):
                last_temp_value = last_temp_value * nums[i+1]
            right_array.append(last_temp_value)
            print(right_array)
        right_array.reverse()
        print(right_array)
        
        for i in range(len(nums)):
            print(i)
            final_array.append(left_array[i] * right_array[i])
        
        return final_array
    
    # optimal solution
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        
        # Build left products directly in result
        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]
        
        # Multiply by right products
        right = 1
        for i in range(n-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result


if __name__ == '__main__':
    solution = Solution()
    input_list = list(map(int, input("Enter the list of nums separated by space: ").strip().split(" ")))
    print(solution.productExceptSelf(input_list))