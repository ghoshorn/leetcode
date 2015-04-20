import unittest
from pprint import pprint
import pdb

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if s=="" and p=="":
            return True
        if p=="":
            return False
        l1=len(s)
        l2=len(p)
        f=[[False]*l1 for i in xrange(l2)]
        last=None # element before *
        for i in range(l2):
            for j in range(l1):
                if i==0 and j==0:
                    if p[i]==s[j] or p[i]==".":
                        f[i][j]=True
                elif j==0 and p[i]==s[j]:
                        f[i][j]=f[i-1][j]
                elif i==0:
                    pass
                elif p[i]==s[j] or p[i]==".":
                    f[i][j]=f[i-1][j-1]
                elif p[i]=="*" and s[j]==last:
                    f[i][j]=True
            last=p[i]
        return f[l2-1][l1-1]

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.isMatch("aa","a"),False)
        self.assertEqual(self.a.isMatch("aa","aa"),True)
        self.assertEqual(self.a.isMatch("aaa","aa"),False)
        self.assertEqual(self.a.isMatch("aa", "a*"),True)
        self.assertEqual(self.a.isMatch("aa", ".*"),True)
        self.assertEqual(self.a.isMatch("ab", ".*"),True)
        self.assertEqual(self.a.isMatch("aab", "c*a*b"),True)
        self.assertEqual(self.a.isMatch("aab", "c*a.b"),True)
        self.assertEqual(self.a.isMatch("", ".*"),True)
        self.assertEqual(self.a.isMatch("abcd", "d*"),False)
        self.assertEqual(self.a.isMatch("aaa", "aaaa"),False)


if __name__ == '__main__':
    unittest.main()