# encoding: utf8
'''
Kth Smallest Element in a BST 
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

参考了discuss
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
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        if root:
            cnt=self.countnode(root.left)
            if cnt==k-1:
                return root.val
            elif cnt>k-1:
                return self.kthSmallest(root.left, k)
            else:
                return self.kthSmallest(root.right, k-cnt-1)

    def countnode(self, root):
        if root==None:
            return 0
        return 1+self.countnode(root.left)+self.countnode(root.right)
        

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a             =TreeNode(5)
        a.left        =TreeNode(3)
        a.left.left   =TreeNode(1)
        a.left.right  =TreeNode(4)
        a.right       =TreeNode(8)
        a.right.left  =TreeNode(7)
        a.right.right =TreeNode(9)
        self.assertEqual(self.a.kthSmallest(a, 1), 1)
        self.assertEqual(self.a.kthSmallest(a, 2), 3)
        self.assertEqual(self.a.kthSmallest(a, 4), 5)
        self.assertEqual(self.a.kthSmallest(a, 7), 9)


if __name__ == '__main__':
    unittest.main()