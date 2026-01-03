"""
Docstring for Arrays.Medium.merge_intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

pattern: sorting + merging based on the ending time of current interval and starting time of next interval
"""
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # sorting the list of lists based on the first index value
        intervals.sort(key=lambda x: x[0])
        final_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            # if the current interval starting time is less than or equal to the previous interval ending time -- merging intervals
            if intervals[i][0] <= final_intervals[-1][1]:
                # merging only the end time of the current interval greater than the previous interval's ending time
                if intervals[i][1] > final_intervals[-1][1]:
                    final_intervals[-1][1] = intervals[i][1]
            else:
                final_intervals.append(intervals[i])
        
        return final_intervals


if __name__ == '__main__':
    solution = Solution()
    input_string = [[1,4],[2,3]]
    print(solution.merge(input_string))

