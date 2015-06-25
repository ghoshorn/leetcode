# encoding: utf8
'''
Single Number
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
使用异或。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        ans=0
        for x in nums:
            ans=ans ^ x
        return ans

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.singleNumber([1,1,2,2,3]),3)
        self.assertEqual(self.a.singleNumber([1,2,2,3,3]),1)

if __name__ == '__main__':
    unittest.main()