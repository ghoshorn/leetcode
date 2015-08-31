# encoding: utf8
'''
Scramble String
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

参考https://leetcode.com/discuss/36470/share-my-4ms-c-recursive-solution
递归的检查s1的前i个和s2的前i个ands 1的后l-i个和s2的后l-i个，
s1的前i个和s2的后i个and s1的前l-i个和s2的后l-i个and
'''

import unittest
from pprint import pprint
import pdb

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1==s2:
            return True
        l=len(s1)
        l2=len(s2)
        if l!=l2:
            return False
        count=[0 for i in range(26)]
        for i in range(l):
            count[ord(s1[i])-ord('a')]+=1
            count[ord(s2[i])-ord('a')]-=1
        for i in range(26):
            if count[i]!=0:
                return False
        for i in range(1,l):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            if self.isScramble(s1[:i],s2[l-i:]) and self.isScramble(s1[i:],s2[:l-i]):
                return True
        return False

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.isScramble("abc", "bca"),True)
        self.assertEqual(self.a.isScramble("rgtae","great"),True)
        self.assertEqual(self.a.isScramble("xstjzkfpkggnhjzkpfjoguxvkbuopi", "xbouipkvxugojfpkzjhnggkpfkzjts"),True)


if __name__ == '__main__':
    unittest.main()