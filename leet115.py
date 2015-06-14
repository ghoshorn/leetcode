# encoding: utf8
'''
Distinct Subsequences
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

f[i][j]表示s[j]和t[i]中的Distinct Subsequences数；
如果s[j]==t[i], f[i][j]=f[i-1][j-1]+f[i][j-1],
其中f[i-1][j-1]表示使用s[j], f[i][j-1]表示不使用s[j].
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        l1=len(t)
        l2=len(s)
        if l1==0:
            return 1
        if l2==0:
            return 0
        f=[[0 for i in range(l2)] for j in range(l1)]
        for i in range(l1):
            for j in range(i,l2):
                if j>0:
                    f[i][j]=f[i][j-1]
                if t[i]==s[j]:
                    if i>0 and j>0:
                        f[i][j]=f[i-1][j-1]+f[i][j-1]
                    elif j>0:
                        f[i][j]=f[i][j-1]+1
                    else:
                        f[i][j]=1
        pprint(f)
        return f[l1-1][l2-1]

# wrong when s=aabb and t=ab
class Solution1:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        l1=len(t)
        l2=len(s)
        if l1==0:
            return 1
        if l2==0:
            return 0
        f=[[0 for i in range(l2)] for j in range(l1)]
        for i in range(l1):
            for j in range(i,l2):
                if i==j and t[i]==s[j]:
                    if i>0 and j>0:
                        f[i][j]=f[i-1][j-1]
                    else:
                        f[i][j]=1
                elif t[i]!=s[j]:
                    if j>0:
                        f[i][j]=f[i][j-1]
                    else:
                        f[i][j]=0
                else:
                    if i>0 and j>0:
                        f[i][j]=max(f[i-1][j-1],f[i-1][j],f[i][j-1]+1)
                    elif j>0:
                        f[i][j]=f[i][j-1]+1
                    elif i>0:
                        f[i][j]=max(f[i-1][j-1],f[i-1][j])
                    else:
                        f[i][j]=0
        pprint(f)
        return f[l1-1][l2-1]

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.numDistinct("rabbbit","rabbit"),3)
        self.assertEqual(self.a.numDistinct("abccc","abc"),3)
        self.assertEqual(self.a.numDistinct("ccc","c"),3)
        self.assertEqual(self.a.numDistinct("aabb","ab"),4)


if __name__ == '__main__':
    unittest.main()