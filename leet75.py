# encoding: utf8
'''
Sort Colors
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

思路。
Solution1:two-pass algorithm

Solution:one-pass algorithm
分别设置red=0,blue=l-1指向下一个存放red和blue的位置。
从头遍历，如果是红色则和red位置的交换；蓝色则和blue位置的交换；
当i>blue的时候，说明已经有序。(为什么不是i==blue? 因为blue只是下一个蓝色需要放置的位置，此刻blue的位置并非蓝色。)

'''

import unittest
from pprint import pprint
import pdb

# two-pass algorithm
class Solution1:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        red=white=blue=0
        for x in nums:
            if x==0:
                red+=1
            elif x==1:
                white+=1
            else:
                blue+=1
        i=0
        while red:
            nums[i]=0
            i+=1
            red-=1
        while white:
            nums[i]=1
            i+=1
            white-=1
        while blue:
            nums[i]=2
            i+=1
            blue-=1
        return None

# less one-pass algorithm
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        l    =len(nums)
        red  =0
        blue =l-1
        i    =0
        while i<=blue:
            if nums[i]==0:
                nums[red],nums[i]=nums[i],nums[red]
                red +=1
                i   +=1
            elif nums[i]==2:
                nums[blue],nums[i]=nums[i],nums[blue]
                blue -=1
                # i    +=1
            else:
                i+=1
        # print(nums)
        return None


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        s=[1,1,2,0]
        self.a.sortColors(s)
        self.assertEqual(s,[0,1,1,2])
        s=[1,2,0]
        self.a.sortColors(s)
        self.assertEqual(s,[0,1,2])
        s=[0,0]
        self.a.sortColors(s)
        self.assertEqual(s,[0,0])
        s=[1,0,0]
        self.a.sortColors(s)
        self.assertEqual(s,[0,0,1])


if __name__ == '__main__':
    unittest.main()
