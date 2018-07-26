'''
Input: "()[]{}"
Output: true

Input: "([)]"
Output: false
'''


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {')': '(', '}': '{', ']': '['}
        stack = []
        for x in s:
            if x in d.values():
                stack.append(x)
            elif x in d.keys():
                if stack == [] or d[x] != stack.pop():
                    return False
        return stack == []
