'''
Given a collection of intervals, merge all overlapping intervals.

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
'''


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        i = 0
        intervals = sorted(intervals, key = lambda x: x.start)
        while i < len(intervals)-1:
            if intervals[i].end >= intervals[i+1].start:
                intervals[i:i+2] = [Interval(intervals[i].start, max(intervals[i].end, intervals[i+1].end))]
            else:
                i += 1
        return intervals
