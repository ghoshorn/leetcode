# encoding: utf8
'''
Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

假设原来数字为x, 返回的为ret.
从x的末尾依此取出，并入ret的末尾即可。
最后ret不足32位的要在末尾用0补齐。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret=0
        cnt=32
        while n:
            ret=ret<<1 | n&0x1
            cnt-=1
            # print n&0x1,
            n=n>>1
        while cnt:
            ret=ret<<1
            cnt-=1
        return ret

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.reverseBits(43261596), 964176192)


if __name__ == '__main__':
    unittest.main()