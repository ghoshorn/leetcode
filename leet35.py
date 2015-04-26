# encoding: utf8
'''
Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

还是二分查找的增强版。
如果在，则返回该位置；不在的话，返回第一个比它大的数的位置。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        start =0
        end   =len(nums)-1
        while start<=end:
            mid=(start+end)/2
            if nums[mid]==target:
                return mid
            elif nums[start]>=target:
                return start
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return start


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.searchInsert([1,3,5,6], 5),2)
        self.assertEqual(self.a.searchInsert([1,3,5,6], 2),1)
        self.assertEqual(self.a.searchInsert([1,3,5,6], 7),4)
        self.assertEqual(self.a.searchInsert([1,3,5,6], 0),0)



if __name__ == '__main__':
    unittest.main()

