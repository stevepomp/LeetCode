'''
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        left = -1
        result = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    left = i
                else:
                    stack.pop()
                    if not stack:
                        result = max(result, i-left)
                    else:
                        result = max(result, i-stack[-1])
        return result
