# encoding: utf8
'''
Ugly Number
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

使用2,3,5除，到最后如果是1，说明没有其他质因子。
'''

import unittest
from pprint import pprint
import pdb

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num>1 and num%5==0:
            num/=5
        while num>1 and num%3==0:
            num/=3
        while num>1 and num%2==0:
            num/=2
        return True if num==1 else False

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.isUgly(1),True)
        self.assertEqual(self.a.isUgly(6),True)
        self.assertEqual(self.a.isUgly(14),False)

if __name__ == '__main__':
    unittest.main()