# encoding: utf8
'''
Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character but a character 
may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

从头到尾计算两个字符串中，对应字母的差。如果某个字母对应的差有多个，则返回False。
为了应对No two characters may map to the same character，需要计算s->t和t->s.
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        dic1={}
        dic2={}
        for x,y in zip(s,t):
            dif=ord(x)-ord(y)
            if x not in dic1:
                dic1[x]=dif
            elif dic1[x]!=dif:
                return False
            if y not in dic2:
                dic2[y]=dif
            elif dic2[y]!=dif:
                return False
        return True

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.isIsomorphic("aa", "ab"), False)
        self.assertEqual(self.a.isIsomorphic("ab", "aa"), False)
        self.assertEqual(self.a.isIsomorphic("egg", "add"), True)
        self.assertEqual(self.a.isIsomorphic("foo", "bar"), False)
        self.assertEqual(self.a.isIsomorphic("paper", "title"), True)


if __name__ == '__main__':
    unittest.main()