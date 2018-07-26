'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        
        d = {'2': 'abc', '3': 'def', '4': 'ghi', "5": 'jkl', '6': "mno", '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 1:
            return list(d[digits[0]])
        
        part = self.letterCombinations(digits[:-1])
        result = [i + j for i in part for j in d[digits[-1]]]
        
        return result
