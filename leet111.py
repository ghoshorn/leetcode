# encoding: utf8
'''
Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the 
shortest path from the root node down to the nearest leaf node.

一定要到叶节点！
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
    def minDepth(self, root):
        if root==None:
            return 0
        self.ans=9999999
        self.go(root,1)
        return self.ans

    def go(self, root, level):
        if root.left==None and root.right==None:
            self.ans=min(self.ans,level)
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
        a.left.left=TreeNode(15)
        a.left.right=TreeNode(7)
        self.assertEqual(self.a.minDepth(a),2)

        a=TreeNode(1)
        a.left=TreeNode(2)
        a.right=TreeNode(3)
        self.assertEqual(self.a.minDepth(a),2)

        a=TreeNode(1)
        a.left=TreeNode(2)
        self.assertEqual(self.a.minDepth(a),2)

        a=TreeNode(1)
        self.assertEqual(self.a.minDepth(a),1)


if __name__ == '__main__':
    unittest.main()