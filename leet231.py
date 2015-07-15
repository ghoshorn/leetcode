# encoding: utf8
'''
Power of Two 
Given an integer, write a function to determine if it is a power of two.

在剑指offer上见过吧？
利用二进制的知识。
2**n=(1000....)2
2**n-1=(0111....)2
则每一位都不相同，所以
(2**n) & (2**n-1) == 0
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        else:
            return True if n & (n-1)==0 else False

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.isPowerOfTwo(0), False)
        self.assertEqual(self.a.isPowerOfTwo(2), True)
        self.assertEqual(self.a.isPowerOfTwo(4), True)
        self.assertEqual(self.a.isPowerOfTwo(6), False)
        self.assertEqual(self.a.isPowerOfTwo(8), True)


if __name__ == '__main__':
    unittest.main()