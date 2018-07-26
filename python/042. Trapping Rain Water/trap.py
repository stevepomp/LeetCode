'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        left = right = 0
        miss = 0
        result = 0
        if len(height) < 3:
            return result
        
        while i < len(height) and height[i] == 0:
            i += 1
        
        if i == len(height):
            return result
        else:
            left = i
        
        while i < len(height)-1:
            i += 1
            if height[i] >= height[left]:
                result += (i-left-1) * height[left] - miss
                left = i
                miss = 0
            else:
                miss += height[i]
        if left < len(height)-2:
            i = left
            while i < len(height)-1:
                hi = height[i+1]
                right = i + 1
                while i < len(height)-1:
                    i += 1
                    if height[i] >= hi:
                        hi = height[i]
                        right = i
                result += hi * (right-left-1) - sum(height[left+1:right])
                if right > len(height)-3:
                    break
                i = left = right
        return result
