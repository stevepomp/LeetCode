'''
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.

Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
Note that the order of those five elements can be arbitrary.
It doesn't matter what values are set beyond the returned length.
'''


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lo = hi = 0
        n = len(nums)
        while hi < len(nums):
            if nums[hi] != val:
                nums[lo] = nums[hi]
                hi += 1
                lo += 1
            while hi < len(nums) and nums[hi] == val:
                hi += 1
                n -= 1
        nums = nums[:n]
        return n
