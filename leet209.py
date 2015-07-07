# encoding: utf8
'''
Minimum Size Subarray Sum
Given an array of n positive integers and a positive integer s, find the minimal length 
of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time 
complexity is O(n log n).

设置两个指针，一前一后(start,end)。每次计算两个指针之间的数的和。
如果和大于s，则更新结果，然后start后移；
如果和小于s，则end后移；
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if nums==[] or sum(nums)<s:
            return 0
        l=len(nums)
        ans=l
        tot=nums[0]
        start=0
        end=0
        while end<l and start<=end:
            if tot>=s:
                ans=min(ans,end-start+1)
                tot-=nums[start]
                start+=1
            else:
                end+=1
                if end>=l:
                    break
                tot+=nums[end]
        return ans


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.minSubArrayLen(7, [2,3,1,2,4,3]), 2)
        self.assertEqual(self.a.minSubArrayLen(11, [1,2,3,4,5]), 3)


if __name__ == '__main__':
    unittest.main()