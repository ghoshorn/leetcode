# encoding: utf8
'''
Sqrt(x)
Implement int sqrt(int x).

Compute and return the square root of x.

通过二分查找来找其平方根。
注意：当起平方根不是整数时，应返回floor(sqrt(x))
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        start=0
        end=x
        while start<=end:
            mid=(start+end)/2
            pingfang=mid*mid
            if pingfang==x:
                return mid
            elif pingfang>x:
                end=mid-1
            else:
                start=mid+1
        while mid*mid>x:
            mid-=1
        return mid


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.mySqrt(4),2)
        self.assertEqual(self.a.mySqrt(16),4)
        self.assertEqual(self.a.mySqrt(49),7)
        self.assertEqual(self.a.mySqrt(0),0)
        self.assertEqual(self.a.mySqrt(2),1)


if __name__ == '__main__':
    unittest.main()
