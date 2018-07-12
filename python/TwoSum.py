'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

#element in set,dict 通过hash查值,速度快
#i, element in enumerate(object) 枚举，获取角标和元素，角标默认从0开始，可指定
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, element in enumerate(nums):
            if target-element in d:
                return [d[target-element], i]
            d[element] = i
