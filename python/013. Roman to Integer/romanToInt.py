'''
Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s
        result = 0
        while l and l[0] == 'M':
            l = l[1:]
            result += 1000
        
        if l[:2] == 'CM':
            l = l[2:]
            result += 900
        elif l and l[0] == 'D':
            l = l[1:]
            result += 500
        elif l[:2] == 'CD':
            l = l[2:]
            result += 400
        
        while l and l[0] == 'C':
            l = l[1:]
            result += 100
        
        if l[:2] == 'XC':
            l = l[2:]
            result += 90
        elif l and l[0] == 'L':
            l = l[1:]
            result += 50
        elif l[:2] == 'XL':
            l = l[2:]
            result += 40
        
        while l and l[0] == 'X':
            l = l[1:]
            result += 10

        if l[:2] == 'IX':
            l = l[2:]
            result += 9
        elif l and l[0] == 'V':
            l = l[1:]
            result += 5
        elif l[:2] == 'IV':
            l = l[2:]
            result += 4
        
        while l and l[0] == 'I':
            l = l[1:]
            result += 1

        return result
