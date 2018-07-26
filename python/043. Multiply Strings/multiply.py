'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Input: num1 = "2", num2 = "3"
Output: "6"

Input: num1 = "123", num2 = "456"
Output: "56088"
'''


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        int1 = 0
        int2 = 0
        d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for i in range(len(num1)):
            int1 = int1 * 10 + d[num1[i]]
        for j in range(len(num2)):
            int2 = int2 * 10 + d[num2[j]]
        return str(int1*int2)
