# encoding: utf8
'''
Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

n!中，有多少个因子5，n!就有多少个0.
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        ret=0
        while n:
            ret+=n/5
            n=n/5
        return ret

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.trailingZeroes(10), 2)
        self.assertEqual(self.a.trailingZeroes(15), 3)
        self.assertEqual(self.a.trailingZeroes(4), 0)


if __name__ == '__main__':
    unittest.main()