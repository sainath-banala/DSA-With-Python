"""
Docstring for Arrays.Easy.merge_sorted_array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""
class Solution:
    def swap_till_end(self, second_list_val, nums1, first_list_index):
        # storing the value of the current index in the first_list
        temp = nums1[first_list_index]
        # replacing the current index in the first_list with the value from the second list
        nums1[first_list_index] = second_list_val
        for i in range(first_list_index+1, len(nums1)):
            temp_1 = nums1[i]
            nums1[i] = temp
            temp = temp_1

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # my approach
        second_list_index = 0
        # doing the modification only if the second list is having some elements
        if n != 0:
            for i in range(m+n):
                # print(nums1[i], i, second_list_index)
                if nums1[i] >= nums2[second_list_index] or (nums1[i] == 0 and i >= second_list_index + m):
                    self.swap_till_end(nums2[second_list_index], nums1, i)
                    if second_list_index < n-1:
                        second_list_index += 1
                    else:
                        break

        # print(nums1)
        
if __name__ == '__main__':
    solution = Solution()
    first_input_list = list(map(int, input("Enter the first list of nums separated by space without zeros: ").strip().split(" ")))
    second_input_list = list(map(int, input("Enter the second list of nums separated by space: ").strip().split(" ")))
    
    # adding n no. of zeros to the end of the first_list where n is the length of second input list provided
    first_input_list.extend(list(0 for _ in range(len(second_input_list))))
    # print(first_input_list)
    # print(second_input_list)
    print(solution.merge(first_input_list, len(first_input_list)-len(second_input_list), second_input_list, len(second_input_list)))




# -1 -1 -1 0 0 0 3 0 0 0

