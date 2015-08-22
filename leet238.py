# encoding: utf8
'''
Product of Array Except Self 
Given an array of n integers where n > 1, nums, return an array output such that 
output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not 
    count as extra space for the purpose of space complexity analysis.)

使用一个数组pre[i]记录前i项的乘积，post[i]记录后i项的乘积。
空间O(n),时间O(n).
'''

import unittest
from pprint import pprint
import pdb

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre=[]
        post=[]
        ans=[]
        product=1
        l=len(nums)
        for x in nums:
            product*=x
            pre.append(product)
        product=1
        for i in xrange(l-1,-1,-1):
            product*=nums[i]
            post.insert(0,product)
        # print pre
        # print post
        ans.append(post[1])
        for i in xrange(1,l-1):
            ans.append(pre[i-1]*post[i+1])
        ans.append(pre[-2])
        return ans

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.productExceptSelf([1,2,3,4]), [24,12,8,6])

if __name__ == '__main__':
    unittest.main()