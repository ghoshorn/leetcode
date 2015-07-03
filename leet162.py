# encoding: utf8
'''
Find Peak Element
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.

首先，只要数组不为空，一定存在一个peak。(why?)
由此，可以采用二分法：首先选取中点mid，如果是peak直接返回即可;
否则: 如果该点比前一个节点小->前半部分肯定存在peak;(why?)
      如果该点比后一个节点小->后半部分肯定存在peak;(why?)
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if nums==[]:
            return
        start  =0
        l= end =len(nums)
        if l==1:
            return 0
        while start<end:
            mid=(start+end)/2
            if mid+1>=l and nums[mid]>nums[mid-1] or \
                mid-1<0 and nums[mid]>nums[mid+1] or \
                nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid]:
                return mid
            if nums[mid]<nums[mid-1]:
                end=mid-1
            else:
                start=mid+1
        return end


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.findPeakElement([1, 2, 3, 1]), 2)
        self.assertEqual(self.a.findPeakElement([1, 3, 2, 1]), 1)
        self.assertEqual(self.a.findPeakElement([1, 2, 1]), 1)
        self.assertEqual(self.a.findPeakElement([1, 2]), 1)


if __name__ == '__main__':
    unittest.main()