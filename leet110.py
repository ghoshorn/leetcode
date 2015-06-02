# encoding: utf8
'''
Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.
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
    # @return {boolean}
    def isBalanced(self, root):
        if root==None:
            return True
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        print(left,right)
        if abs(left-right)>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        self.ans=0
        if root:
            self.go(root, 1)
        return self.ans

    def go(self, root, level):
        if root:
            self.ans=max(self.ans,level)
        if root.left:
            self.go(root.left, level+1)
        if root.right:
            self.go(root.right, level+1)


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        r=TreeNode(1)
        r.left=TreeNode(2)
        r.right=TreeNode(3)
        r.left.left=TreeNode(3)
        r.left.right=TreeNode(3)
        r.left.left.left=TreeNode(4)
        r.left.left.right=TreeNode(4)
        self.assertEqual(self.a.isBalanced(r),False)

        r=TreeNode(1)
        r.right=TreeNode(2)
        r.right.right=TreeNode(3)
        self.assertEqual(self.a.isBalanced(r),False)


if __name__ == '__main__':
    unittest.main()