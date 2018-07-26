'''
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = result = nums[0]
        for num in nums[1:]:
            sums = max(num, sums+num)
            result = max(result, sums)
        return result
