# encoding: utf8
'''
Remove Duplicates from Sorted Array II
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. 
It doesn't matter what you leave beyond the new length.

思路：
设置两个指针i,j. 为了最后原地改变数组，每次令nums[i+1]=nums[j]。
另设一个hasTwo，True表示已经i已经指向了第二个重复的数字，此时应该让j+=1直到nums[i]!=nums[j]，长度做相应减少，并令nums[i+1]=nums[j]后，让nums[i+1]与nums[j+1]继续比较。
False表示还没有两个重复数字，i+=1,j+=1，继续比较即可。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        l=ll=len(nums)
        print nums
        i=0
        j=1
        hasTwo=False
        while j<ll:
            nums[i+1]=nums[j]
            if nums[i]==nums[j]:
                if hasTwo:
                    while j<ll and nums[j]==nums[i]:
                        j +=1
                        l -=1
                    i+=1
                    if j<ll:
                        nums[i] =nums[j]
                        j       +=1
                        hasTwo  =False
                else:
                    i      +=1
                    j      +=1
                    hasTwo =True
            else:
                hasTwo =False
                i      +=1
                j      +=1
        print nums
        return l

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.removeDuplicates([1,1,1,2,2,3]),5)
        self.assertEqual(self.a.removeDuplicates([1,1,1]),2)


if __name__ == '__main__':
    unittest.main()