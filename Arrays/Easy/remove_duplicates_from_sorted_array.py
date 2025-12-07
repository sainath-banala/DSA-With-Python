"""
Docstring for Arrays.Easy.remove_duplicates_from_sorted_array
Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.
EX:
Input: arr[]=[1,1,2,2,2,3,3]
Output: [1,2,3,_,_,_,_]
Explanation: Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #your code goes here
        ## considering the first index is having unique value
        unique_index = 0
        # iterating the loop from index 1
        for i in range(1, len(nums)):
            # checking if the cur_val is different from the unique_indexed value
            if nums[unique_index] != nums[i]:
                # incrementing the unique_index value
                unique_index += 1
                # swapping the unique value to the same place and moving before the duplicate values if exists between the unique index and current value
                # [1,1,2,3,3] --> consider i = 3 and cur_val is 2, we will swap: [1, 2, 1, 3, 3]
                temp_var = nums[i]
                nums[i] = nums[unique_index]
                nums[unique_index] = temp_var
        
        print(nums)
        
        return unique_index + 1


if __name__ == '__main__':
    solution = Solution()
    input_list = list(map(int, input("Enter the list of integers separated by space: ").strip().split(" ")))
    unique_element_count = solution.removeDuplicates(input_list)
    print(unique_element_count)