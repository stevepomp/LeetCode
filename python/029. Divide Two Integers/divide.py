'''
Input: dividend = 10, divisor = 3
Output: 3

Input: dividend = 7, divisor = -3
Output: -2
'''


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend * divisor > 0:
            sign = 1
        else:
            sign = -1
        result, _ = divmod(abs(dividend), abs(divisor))
        if sign > 0:
            return min(2**31-1, result)
        if sign < 0:
            return max(-2**31, result*sign)
