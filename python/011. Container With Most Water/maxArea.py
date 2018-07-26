'''
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(height) - 1
        i = len(height) - 1
        result = 0
        while lo < hi:
            result = max(min(height[lo], height[hi]) * i, result)
            if height[lo] < height[hi]:
                lo += 1
                i -= 1
            else:
                hi -= 1
                i -= 1
        return result
