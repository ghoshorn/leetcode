# encoding: utf8
'''
Interleaving String 
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

思路：DP. 如下:
定义为f. 
f[i][j]=-1说明s2的前i位和s1的前j位不能够长s3的Interleaving String;
f[i][j]>0即表示当前已经对应到s3的f[i][j]位。
以s1 = "aabcc",s2 = "dbbca",s3 = "aadbbcbcac"为例：
    s1  nul     a   a   b   c   c
s2
nul     -1      0   1   -1  -1  -1
d       -1          2   3
b       -1          3   4   5
b       -1          4       6
a       -1          5       7
c       -1          6   7   8
a       -1                  9   10
'''

import unittest
from pprint import pprint
import pdb


class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        l1=len(s1)
        l2=len(s2)
        l3=len(s3)
        if l1+l2!=l3:
            return False
        if l1==0 or l2==0:
            if s1+s2==s3:
                return True
            else:
                return False
        f=[[-1 for i in range(l1+1)] for j in range(l2+1)]
        for i in range(l1):
            if s3[i]==s1[i]:
                f[0][i+1]=i
            else:
                break
        for j in range(l2):
            if s3[j]==s2[j]:
                f[j+1][0]=j
            else:
                break
        for i in range(1,l2+1):
            for j in range(1,l1+1):
                if f[i-1][j]>=0 and s2[i-1]==s3[f[i-1][j]+1]:
                    f[i][j]=f[i-1][j]+1
                elif f[i][j-1]>=0 and s1[j-1]==s3[f[i][j-1]+1]:
                    f[i][j]=f[i][j-1]+1
        # pprint(f)
        if f[l2][l1]>=0:
            return True
        else:
            return False

        

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.isInterleave("aabcc","dbbca","aadbbcbcac"),True)
        self.assertEqual(self.a.isInterleave("aabcc","dbbca","aadbbbaccc"),False)
        self.assertEqual(self.a.isInterleave("","",""),True)
        self.assertEqual(self.a.isInterleave("a","b","a"),False)
        self.assertEqual(self.a.isInterleave("db", "b", "cbb"),False)


if __name__ == '__main__':
    unittest.main()