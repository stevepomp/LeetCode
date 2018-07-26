'''
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        s = sorted(nums)
        result = []
        for i in range(n-3):
            if i == 0 or s[i] != s[i-1]:
                for j in range(i+1, n-2):
                    if j == i+1 or s[j] != s[j-1]:
                        k = j + 1
                        l = n - 1
                        while k < l:
                            sums = s[i] + s[j] + s[k] + s[l]
                            if sums == target:
                                result.append([s[i], s[j], s[k], s[l]])
                                while k+1 < l and s[k] == s[k+1]:
                                    k += 1
                                while k+1 < l and s[l] == s[l-1]:
                                    l -= 1
                                k += 1
                                l -= 1

                            if sums < target:
                                k += 1

                            if sums > target:
                                l -= 1
        
        return result
