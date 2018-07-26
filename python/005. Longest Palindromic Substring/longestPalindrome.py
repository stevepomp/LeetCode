'''
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        result = ''
        if n == 0:
            result = None
        elif n == 1:
            result = s
        else:
            for i in range(n):
                for j in range(i+1):
                    temp = s[j:n-i+j]
                    a = 0
                    b = n-i-1
                    while a < b:
                        if temp[a] == temp[b]:
                            a += 1
                            b -= 1
                        else:
                            break
                    
                    if a >= b:
                        result = s[j:n-i+j]
                        break
                if result:
                    break
        
        return result
