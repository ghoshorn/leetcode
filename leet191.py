# encoding: utf8
'''
Number of 1 Bits
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        ret=0
        while n:
            ret += n&0x1
            n=n>>1
        return ret

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.hammingWeight(11), 3)


if __name__ == '__main__':
    unittest.main()