# encoding: utf8
'''
Bitwise AND of Numbers Range
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers 
in this range, inclusive.

For example, given the range [5, 7], you should return 4.

规模太大，如果直接挨个进行AND必然超时。

换一种思路。
例如
7: 1 1 1
6: 1 0 0
5: 1 0 1
--------
   1 0 0
与的次数越多，包含的1个数越少。
假如[m,n]范围内有一个偶数（即最后一位是0），则结果的最后一位必为0；
假如[m,n]范围内有一个数，它的倒数第二位是0，则结果的倒数第二位必为0；
以此类推...
假设m和n的差是dif。
如果dif=1，那么[m,n]范围内必有一个偶数，则结果的最后一位必为0；
如果dif=2，那么[m,n]范围内必有一个数，它的倒数第二位是0，则结果的倒数第二位必为0；
如果dif=4，那么[m,n]范围内必有一个数，它的倒数第三位是0，则结果的倒数第三位必为0；
以此类推...
'''

import unittest
from pprint import pprint
import pdb

class Solution1: # Time Limit Exceeded
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd1(self, m, n):
        ret=n
        for x in xrange(m,n):
            ret=ret & x
            if ret==0:
                return ret
        return ret

class Solution: # AC
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        ret=n&m # why not ret=n?  in case of (2,1)->0
        dif=n-m
        mask=0xFFFFFFFF
        while dif>0:
            mask=mask<<1
            ret=ret & mask
            dif=dif>>1
        return ret

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.rangeBitwiseAnd(1,2), 0)
        self.assertEqual(self.a.rangeBitwiseAnd(5,7), 4)
        self.assertEqual(self.a.rangeBitwiseAnd(5,30000), 0)
        self.assertEqual(self.a.rangeBitwiseAnd(5,2147483647), 0)
        self.assertEqual(self.a.rangeBitwiseAnd(600000000, 2147483645), 0)



if __name__ == '__main__':
    unittest.main()