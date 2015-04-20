# encoding: utf8
'''
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
需要注意的特殊情况：输入是个空列表
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        prefix=""
        for i in strs[0]:
            prefix+=i
            iscommon=True
            for s in strs:
                if not s.startswith(prefix):
                    iscommon=False
                    break
            if not iscommon:
                return prefix[:-1]
        return prefix

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.longestCommonPrefix(["abccc","abdee","abcde"]),"ab")
        self.assertEqual(self.a.longestCommonPrefix([]),"")
        self.assertEqual(self.a.longestCommonPrefix([""]),"")


if __name__ == '__main__':
    unittest.main()