'''
Input: 123
Output: 321

Input: -123
Output: -321

Input: 120
Output: 21
'''

# Given a 32-bit signed integer, reverse digits of an integer.


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        if x < -2**31 or x > 2**31-1:
            return 0
        else:
            y = abs(x)
            if y == x:
                sign = 1
            else:
                sign = -1
            while y > 0:
                i, j = divmod(y, 10)
                result = result*10 + j
                y = (y - j)/10
            result = int(result*sign)
            if result < -2**31 or result > 2**31-1:
                return 0
            else:
                return result
