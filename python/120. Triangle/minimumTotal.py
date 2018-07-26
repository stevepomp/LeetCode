'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        for i in range(1, n):
            row_ex = triangle[i-1]
            row = triangle[i]
            triangle[i] = [row[0]+row_ex[0]] + [row[x]+min(row_ex[x-1:x+1]) for x in range(1, i)] + [row[-1]+row_ex[-1]]
        return min(triangle[-1])
