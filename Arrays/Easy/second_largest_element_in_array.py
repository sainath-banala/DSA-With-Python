"""
Docstring for Arrays.Easy.second_largest_element_in_array
Input: nums = [8, 8, 7, 6, 5]

Output: 7

Explanation:

The largest value in nums is 8, the second largest is 7
"""
class Solution:
    def secondLargestElement(self, nums):
        max_1 = nums[0]
        
        # fetch the max value from the list
        for i in range(len(nums)):
            if nums[i] > max_1:
                max_1 = nums[i]

        temp_list = []
        # remove the max value from the list
        for num in nums:
            if num != max_1:
                temp_list.append(num)
        
        max_2=temp_list[0] if len(temp_list) > 0 else -1
        for i in range(len(temp_list)):
            if temp_list[i] > max_2:
                max_2 = temp_list[i]
            
        return max_2
                

if __name__ == '__main__':
    solution = Solution()
    input_list = list(map(int, input("Enter the list of integers separated by space: ").strip().split(" ")))
    second_largest = solution.secondLargestElement(input_list)
    print(second_largest)