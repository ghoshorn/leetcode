# encoding: utf8
'''
Search in Rotated Sorted Array
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

就是在一个有序但旋转过的数组中查找元素。
分情况，直接二分查找或者递归的调用函数。
1 左半边有序，且在左半边
2 右半边有序，且在右半边
3 左半边无序，且在左半边
4 右半边无序，且在右半边
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        l=len(nums)
        if l==1 and nums[0]!=target:
            return -1
        if l==2:
            if nums[0]==target:
                return 0
            elif nums[1]==target:
                return 1
            else:
                return -1
        start =0
        end   =l-1
        mid   =l/2
        if nums[mid]==target:
            return mid
        if nums[start]<nums[end] and (nums[start]>target or nums[end]<target):
            return -1
        if nums[start]<=target<=nums[mid] or nums[end]<=target<=nums[mid]:
            pos=self.bisearch(nums[start:mid+1],target)
            if pos!=-1:
                return start+pos
        if nums[mid]<=target<=nums[end] or nums[start]>=target>=nums[mid]:
            pos=self.bisearch(nums[mid:end+1],target)
            if pos!=-1:
                return mid+pos
        if target<=nums[end]:
            pos=self.search(nums[mid:end+1],target)
            if pos!=-1:
                return mid+pos
        if target<=nums[mid]:
            pos=self.search(nums[0:mid+1],target)
            if pos!=-1:
                return pos
        if target>=nums[mid]:
            pos=self.search(nums[mid:end+1],target)
            if pos!=-1:
                return mid+pos
        if target>=nums[start]:
            pos=self.search(nums[0:mid+1],target)
            if pos!=-1:
                return pos
        return -1

    def bisearch(self,nums,target):
        start =0
        end   =len(nums)-1
        while start<=end:
            mid=(start+end)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return -1


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.search([4,5,6,7,0,1,2],5),1)
        self.assertEqual(self.a.search([4,5,6,7,0,1,2],1),5)
        self.assertEqual(self.a.search([6,7,0,1,2,3,4],1),3)
        self.assertEqual(self.a.search([6,7,0,1,2,3,4],3),5)
        self.assertEqual(self.a.search([6,7,0,1,2,3,4],7),1)
        self.assertEqual(self.a.search([1],0),-1)
        self.assertEqual(self.a.search([1,3],4),-1)
        self.assertEqual(self.a.search([3,1],4),-1)
        self.assertEqual(self.a.search([1,3],1),0)
        self.assertEqual(self.a.search([3,5,1], 0),-1)
        self.assertEqual(self.a.search([4,5,6,7,0,1,2], 0),4)
        self.assertEqual(self.a.search([2,3,4,5,6,7,8,9,1], 9),7)


if __name__ == '__main__':
    unittest.main()

