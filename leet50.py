# encoding: utf8
'''
Pow(x, n)
Implement pow(x, n).

需要考虑n>0,n=0,n<0。
另外，当n过大时，直接for i in range(n)会超内存/超时，需加优化：记录x的1,2,4,8,16...次幂，大大缩小循环的次数。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n==0:
            return 1
        ans=x
        nn=abs(n)
        i=1
        powx={}
        while i<=nn:
            powx[i]=ans
            ans*=ans
            i*=2
        i/=2
        ans=1
        while nn>0:
            while i<=nn:
                ans*=powx[i]
                nn-=i
            i/=2
        if n<0:
            ans=1.0/ans
        return ans



class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.myPow(2,3),8)
        self.assertEqual(self.a.myPow(2,-3),0.125)
        self.assertEqual(self.a.myPow(2,0),1)
        self.assertEqual(self.a.myPow(2.0,4),16)
        self.assertEqual(self.a.myPow(0.00001, 2147483647),0)
        self.assertEqual(self.a.myPow(8.95371, -1),1/8.95371)


if __name__ == '__main__':
    unittest.main()
