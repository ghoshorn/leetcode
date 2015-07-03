# encoding: utf8
'''
Find Minimum in Rotated Sorted Array
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

对于排序后的数组，应该有nums[start]<nums[mid]<nums[end].
如果nums[mid]>nums[end]，说明最小的在后半部分；否则在前半部分。
需要注意如果本来就是有序但未旋转的情况。 
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        l=len(nums)
        if l==0:
            return
        if l==1:
            return nums[0]
        start =0
        end   =l-1
        while start<end:
            if nums[start]<nums[end]:
                return nums[start]
            mid=(start+end)/2
            if nums[mid]>nums[end]:
                start=mid+1
            else:
                # end=mid-1 # Attetion! [3,1,2] will fail
                end=mid
        return nums[end]

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.findMin([4,5,6,7,0,1,2]), 0)
        self.assertEqual(self.a.findMin([4,5,6,7,0,1,2,3]), 0)
        self.assertEqual(self.a.findMin([0,1,2,4,5,6,7]), 0)
        self.assertEqual(self.a.findMin([1,2]), 1)
        self.assertEqual(self.a.findMin([3,1,2]), 1)

if __name__ == '__main__':
    unittest.main()