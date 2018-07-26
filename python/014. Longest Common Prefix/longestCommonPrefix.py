'''
Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        if not strs:
            return ''
        
        for i, letter in enumerate(zip(*strs)):
            if len(set(letter)) > 1:
                return strs[0][:i]
        
        return min(strs)
