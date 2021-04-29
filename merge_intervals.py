"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
Input: intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
Output: [[1,10]]
Explanation: Interval [1,10] covers all other intervals.
"""

def merge(intervals):
    def merge_two_intervals(l, r):
        intervals[l][0] = min(intervals[r][0], intervals[l][0])
        intervals[l][1] = max(intervals[r][1], intervals[l][1])
        intervals.pop(r)
    l, r = 0, 1
    intervals = sorted(intervals)
    while r < len(intervals):
        if intervals[r][0] <= intervals[l][0] <= intervals[r][1]:
            merge_two_intervals(l, r)
        elif intervals[r][0] <= intervals[l][1] <= intervals[r][1]:
            merge_two_intervals(l, r)
        elif intervals[l][0] <= intervals[r][1] <= intervals[l][1]:
            merge_two_intervals(l, r)
        else:
            r += 1
            l += 1
    return intervals
