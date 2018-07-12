'''
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
---------------------
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sum = sorted(nums1 + nums2)
        twolens = len(nums1) + len(nums2)
        val, part = divmod(twolens, 2)
        if val == 0:
            median = float(sum[0])
        elif part:
            x = int((twolens-1)/2)
            median = float(sum[x])
        else:
            x = int(twolens/2-1)
            median = (sum[x]+sum[x+1])/2
            
        return median
