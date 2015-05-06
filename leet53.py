# encoding: utf8
'''
Maximum Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

不可默认初始化为0，因为可能出现全为负数的情况。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        l=len(nums)
        from copy import deepcopy
        f=deepcopy(nums)
        tmp=nums[0]
        f[0]=tmp
        ans=tmp
        for i in range(1,l):
            tmp+=nums[i]
            ans=max(ans,tmp)
            if tmp>f[i]:
                f[i]=tmp
            else:
                tmp=f[i]
                ans=max(ans,tmp)
        return ans


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]),6)
        self.assertEqual(self.a.maxSubArray([-3,-1,2,-3,2,-1,2,3]),6)
        self.assertEqual(self.a.maxSubArray([0]),0)
        self.assertEqual(self.a.maxSubArray([-1]),-1)
        self.assertEqual(self.a.maxSubArray([-2,-1]),-1)


if __name__ == '__main__':
    unittest.main()
