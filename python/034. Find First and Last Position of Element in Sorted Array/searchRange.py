'''
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        if target in nums:
            result.append(nums.index(target))
            nums.reverse()
            result.append(len(nums)-nums.index(target)-1)
        else:
            return [-1, -1]
        return result
