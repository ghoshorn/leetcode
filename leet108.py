# encoding: utf8
'''
Convert Sorted Array to Binary Search Tree
Given an array where elements are sorted in ascending order, 
convert it to a height balanced BST.
'''

import unittest
from pprint import pprint
import pdb

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        if nums==[]:
            return None
        mid=len(nums)/2
        root=TreeNode(nums[mid])
        root.left=self.sortedArrayToBST(nums[:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:])
        return root


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=TreeNode(1)
        a.left=TreeNode(2)
        a.right=TreeNode(3)
        # self.assertEqual(self.a.sortedArrayToBST([1,2,3]),a)
        r=self.a.sortedArrayToBST([1,2,3])
        print r.val, r.left.val, r.right.val


if __name__ == '__main__':
    unittest.main()