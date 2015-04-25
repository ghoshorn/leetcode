# encoding: utf8
'''
Search for a Range 
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

二分查找的增强版。
如果不在此范围内，直接返回[-1,-1]；
如果中间节点等于目标数，在左边找最靠左的，在右边找最靠右的
[此步骤中，查找左边和右边的时候，可以都把中间节点加上，以免左边或右边没有目标数];
否则在左边或右边递归查找。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        start =0
        end   =len(nums)-1
        mid   =(start+end)/2
        if target<nums[start] or target>nums[end]:
            return [-1,-1]
        if nums[mid]==target:
            left=self.bisearchleft(nums[:mid+1],target)
            right=mid+self.bisearchright(nums[mid:],target)
            return [left,right]
        elif nums[mid]<target:
            pos=self.searchRange(nums[mid+1:],target)
            if pos!=[-1,-1]:
                for i in range(len(pos)):
                    pos[i]=pos[i]+mid+1
            return pos
        elif nums[mid]>target:
            return self.searchRange(nums[:mid],target)

    def bisearchleft(self,nums,target):
        start =0
        end   =len(nums)-1
        pos   =len(nums)
        while start<=end:
            mid=(start+end)/2
            if nums[mid]==target:
                pos=mid
                end=mid-1
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        if pos!=len(nums):
            return pos
        else:
            return -1

    def bisearchright(self,nums,target):
        start =0
        end   =len(nums)-1
        pos   =-1
        while start<=end:
            mid=(start+end)/2
            if nums[mid]==target:
                pos=mid
                start=mid+1
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return pos


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.searchRange([5, 7, 7, 8, 8, 10], 8),[3,4])
        self.assertEqual(self.a.searchRange([5, 7, 7, 8, 8, 10], 7),[1,2])
        self.assertEqual(self.a.searchRange([5, 7, 7, 8, 8, 10], 5),[0,0])
        self.assertEqual(self.a.searchRange([5, 7, 7, 8, 8, 10], 3),[-1,-1])
        self.assertEqual(self.a.searchRange([1], 0),[-1,-1])
        self.assertEqual(self.a.searchRange([2,2], 2),[0,1])
        self.assertEqual(self.a.searchRange([1,5], 4),[-1,-1])


if __name__ == '__main__':
    unittest.main()

