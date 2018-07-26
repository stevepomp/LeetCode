'''
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        s = sorted(nums)
        result = s[0] + s[1] + s[2]
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                sums = s[i] + s[j] + s[k]
                if sums == target:
                    return sums
                
                if abs(sums-target) < abs(result-target):
                    result = sums
                
                if sums < target:
                    j += 1
                
                if sums > target:
                    k -= 1
        
        return result
