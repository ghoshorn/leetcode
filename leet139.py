# encoding: utf8
'''
Word Break
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        l=len(s)
        if l==0:
            return True
        f=[False for i in range(l)]
        for i in range(-1,l-1):
            for j in range(i+1,l):
                if i>=0 and f[i] and s[i+1:j+1] in wordDict:
                    f[j]=True
                elif i==-1 and s[:j+1] in wordDict:
                    f[j]=True
        # print f
        return f[l-1]

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.wordBreak('leetcode',['leet','code']),True)

if __name__ == '__main__':
    unittest.main()