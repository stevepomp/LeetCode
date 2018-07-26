'''
Input: 121
Output: true

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = 0
        n = x
        if 0 <= x <= 9:
            return True
        elif x < 0:
            return False
        else:
            while n > 0:
                _, i = divmod(n, 10)
                temp = temp*10 + i
                n = (n - i)/10
            if temp == x:
                return True
            else:
                return False
