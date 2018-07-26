'''
Given an unsorted integer array, find the smallest missing positive integer.

Input: [1,2,0]
Output: 3

Input: [3,4,-1,1]
Output: 2

Input: [7,8,9,11,12]
Output: 1
'''


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        nums = list(set(nums))
        nums.sort()
        result = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                break
        while i < len(nums):
            if nums[i] > result:
                return result
            else:
                result += 1
                i += 1
        if i == len(nums):
            return nums[-1]+1
                
