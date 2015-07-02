# encoding: utf8
'''
Maximum Product Subarray 
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

看题解。。
maxProduct一定包含第一个元素或者最后一个元素。(0除外) why?
所有元素必定大于等于1。那么这两个元素或者都是正数，或者都是负数，或者一正一负。
都是正数时，显然中间的乘积再乘上两个正数会更大；负数同理；
遇到0，就相当于把数组拆分为了多个数组。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        if nums==[]:
            return 0
        l=len(nums)
        ans=nums[0]
        tmp=1
        for i in range(l):
            tmp*=nums[i]
            if ans<tmp:
                ans=tmp
            if nums[i]==0:
                tmp=1
        tmp=1
        for i in range(l-1,-1,-1):
            tmp*=nums[i]
            if ans<tmp:
                ans=tmp
            if nums[i]==0:
                tmp=1
        return ans

class Solution1: # wrong solution!
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        if nums==[]:
            return 0
        ans=nums[0]
        tmp=1
        for x in nums:
            if abs(tmp*x)>=abs(x):
                tmp=tmp*x
            else:
                tmp=x
            if tmp>ans:
                ans=tmp
            if x>ans:
                ans=x
        return ans

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.maxProduct([2,3,-2,4]), 6)
        self.assertEqual(self.a.maxProduct([0,2]), 2)
        self.assertEqual(self.a.maxProduct([-2,3,-4]), 24)
        self.assertEqual(self.a.maxProduct([-1,-1]), 1)
        self.assertEqual(self.a.maxProduct([2,-5,-2,-4,3]), 24)

if __name__ == '__main__':
    unittest.main()