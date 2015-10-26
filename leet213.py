# encoding: utf8
'''
House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain 
amount of money stashed, the only constraint stopping you from robbing each of them is that 
adjacent houses have security system connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

DP.
f[i]=max(
    f[i-1],  # 抢劫了i-1
    f[i-2]+nums[i] # 不抢劫i-1,抢劫i
    )
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        l=len(nums)
        if l==0:
            return 0
        if l==1:
            return nums[0]
        f=[0 for x in range(l)]
        for i in range(l):
            try:
                f[i]=max(f[i-2]+nums[i],f[i-1])
            except Exception, e:
                f[i]=nums[i]
        return max(f[-1], f[-2])

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.rob([1,1,1,1,1]), 3)


if __name__ == '__main__':
    unittest.main()