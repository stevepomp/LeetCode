'''
a + b + c = 0

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        m = len(nums)
        Nums = sorted(nums)
        for i in range(m-2):
            if (i == 0) or (Nums[i] != Nums[i-1]):
                j = i + 1
                k = m - 1
                while j < k:
                    sum = Nums[i] + Nums[j] + Nums[k]
                    if sum == 0:
                        result.append([Nums[i], Nums[j], Nums[k]])
                        while j+1 < k and Nums[j] == Nums[j+1]:
                            j += 1
                        while j+1 < k and Nums[k] == Nums[k-1]:
                            k -= 1
                        j += 1
                        k -= 1
                    if sum > 0:
                        k -= 1
                    if sum < 0:
                        j += 1
                        
        return result
