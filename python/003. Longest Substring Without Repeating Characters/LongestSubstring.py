'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 1
        if len(s) <= 1:
            result = len(s)
        while len(s) > 1:
            substring = ''
            for i in range(len(s)):
                if s[i] in substring:
                    break
                else:
                    substring += s[i]
            j = s.index(s[i])
            s = s[j+1:]
            temp = len(substring)
            if result < temp:
                result = temp
    
        return result
