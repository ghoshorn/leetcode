# encoding: utf8
'''
Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.
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
    # @return {integer}
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
        a=TreeNode(3)
        a.left=TreeNode(9)
        a.right=TreeNode(20)
        a.right.left=TreeNode(15)
        a.right.right=TreeNode(7)
        self.assertEqual(self.a.maxDepth(a),3)

        a=TreeNode(1)
        a.left=TreeNode(2)
        a.right=TreeNode(3)
        self.assertEqual(self.a.maxDepth(a),2)


if __name__ == '__main__':
    unittest.main()