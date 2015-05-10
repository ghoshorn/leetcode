# encoding: utf8
'''
Add Binary
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

从右至左，按位加，按需进位即可。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        c=[]
        if len(a)<len(b):
            a,b=b,a
        la=len(a)
        lb=len(b)
        for i in range(la-1,la-lb-1,-1):
            c.append(int(a[i])+int(b[i-la+lb]))
        if la>lb:
            for i in range(la-lb-1,-1,-1):
                c.append(int(a[i]))
        l=len(c)
        for i in range(l-1):
            if c[i]>1:
                c[i]-=2
                c[i+1]+=1
        if c[l-1]>1:
            c[l-1]-=2
            c.append(1)
        # print c
        ans="".join(map(lambda x:str(x),c[::-1]))
        print ans
        return ans


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.addBinary("11","1"),"100")
        self.assertEqual(self.a.addBinary("1111","1"),"10000")
        self.assertEqual(self.a.addBinary("1111","1111"),"11110")
        self.assertEqual(self.a.addBinary("1110","1"),"1111")       


if __name__ == '__main__':
    unittest.main()
