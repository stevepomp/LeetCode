'''
Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        part = num
        if part >=1000:
            n, part = divmod(part, 1000)
            result += 'M' * n
        
        if part >= 900:
            result += 'CM'
            part -= 900
        elif part >= 500:
            result += 'D'
            part -= 500
        elif part >= 400:
            result += 'CD'
            part -= 400
        
        if part >=100:
            n, part = divmod(part, 100)
            result += 'C' * n
        
        if part >= 90:
            result += 'XC'
            part -= 90
        elif part >= 50:
            result += 'L'
            part -=50
        elif part >=40:
            result += 'XL'
            part -= 40
        
        if part >= 10:
            n, part = divmod(part, 10)
            result += 'X' * n
        
        if part >= 9:
            result += 'IX'
            part -= 9
        elif part >= 5:
            result += 'V'
            part -= 5
        elif part >= 4:
            result += 'IV'
            part -= 4
        
        if part > 0:
            result += 'I' * part
        
        return result
