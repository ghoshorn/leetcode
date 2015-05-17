# encoding: utf8
'''
Search in Rotated Sorted Array II
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

Search in Rotated Sorted Array的思路
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
    # @return {boolean}
    def search(self, nums, target):
        l=len(nums)
        if l==1 and nums[0]!=target:
            return False
        if l==2:
            if nums[0]==target or nums[1]==target:
                return True
            else:
                return False
        start =0
        end   =l-1
        mid   =l/2
        if nums[mid]==target:
            return True
        if nums[start]<nums[end] and (nums[start]>target or nums[end]<target):
            return False
        if nums[start]<=target<=nums[mid] or nums[end]<=target<=nums[mid]:
            pos=self.bisearch(nums[start:mid+1],target)
            if pos!=-1:
                return True
        if nums[mid]<=target<=nums[end] or nums[start]>=target>=nums[mid]:
            pos=self.bisearch(nums[mid:end+1],target)
            if pos!=-1:
                return True
        if target<=nums[end]:
            pos=self.search(nums[mid:end+1],target)
            if pos:
                return pos
        if target<=nums[mid]:
            pos=self.search(nums[0:mid+1],target)
            if pos:
                return pos
        if target>=nums[mid]:
            pos=self.search(nums[mid:end+1],target)
            if pos:
                return pos
        if target>=nums[start]:
            pos=self.search(nums[0:mid+1],target)
            if pos:
                return pos
        return False

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
        self.assertEqual(self.a.search([4,4,5,6,7,0,1,2],5),True)
        self.assertEqual(self.a.search([4,4,5,6,7,0,1,2],1),True)
        self.assertEqual(self.a.search([6,7,0,1,1,2,3,4],1),True)
        self.assertEqual(self.a.search([6,7,0,1,2,3,4],3),True)
        self.assertEqual(self.a.search([6,7,0,1,2,3,4],7),True)
        self.assertEqual(self.a.search([1],0),False)
        self.assertEqual(self.a.search([1,3],4),False)
        self.assertEqual(self.a.search([3,1],4),False)
        self.assertEqual(self.a.search([1,3],1),True)
        self.assertEqual(self.a.search([3,5,1], 0),False)
        self.assertEqual(self.a.search([4,5,6,7,0,1,2], 0),True)
        self.assertEqual(self.a.search([2,3,4,5,6,7,8,9,1], 9),True)


if __name__ == '__main__':
    unittest.main()

