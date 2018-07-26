'''
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        i = 0
        x = 0
        temp = ['' for n in range(len(s))]
        while i < numRows-1 and x < len(s):
            temp[i] += s[x]
            x += 1
            i += 1
            if x > len(s)-1:
                break
            if i == numRows-1:
                while i > 0:
                    temp[i] += s[x]
                    x += 1
                    i -= 1
                    if x > len(s)-1:
                        break


        if len(s) <= 1 or numRows <= 1:
            result = s
        else:
            result = ''.join(temp)
        return result
