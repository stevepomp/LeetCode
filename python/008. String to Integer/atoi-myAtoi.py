'''
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
'''


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        result = 0
        sign = 1
        if len(str) == 0:
            return 0
        while str[i] == ' ':
            i += 1
            if i > len(str)-1:
                return 0
        
        if ord(str[i]) < 48 or ord(str[i]) > 57:
            if ord(str[i]) == 45:
                sign = -1
            elif ord(str[i]) == 43:
                sign = 1
            else:
                return 0
            i += 1
        if i > len(str)-1:
            return 0
        
        if str[i] == ' ':
            return 0
        
        while str[i] != ' ':
            if 48 <= ord(str[i]) <= 57:
                result = result*10 + int(str[i])
                i += 1
            else:
                break
            if i > len(str)-1:
                break
        
        result = result * sign
        if result > 2**31-1:
            return 2**31-1
        if result < -2**31:
            return -2**31
        
        return result
