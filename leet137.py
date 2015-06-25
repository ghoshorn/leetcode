# encoding: utf8
'''
Single Number II
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
使用一个sizeof(int)的数组，记录各个位上1的个数。
如果是3的倍数个，忽略；
最后据此计算只出现1次的数字。

但是，如果出现负数怎么办？
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        sizeofint=8*8
        t=[0 for i in range(sizeofint)]
        print t
        for x in nums:
            for i in range(sizeofint):
                t[i]+= (x>>i)&1
        ans=0
        print t
        for i in range(sizeofint):
            if t[i]%3==1:
                ans+=1<<i
        return ans

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        # self.assertEqual(self.a.singleNumber([1,1,1,2,2,2,3]),3)
        # self.assertEqual(self.a.singleNumber([1,2,2,2,3,3,3]),1)
        self.assertEqual(self.a.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]),-4)

if __name__ == '__main__':
    unittest.main()