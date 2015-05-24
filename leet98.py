# encoding: utf8
'''
Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
    · The left subtree of a node contains only nodes with keys less than the node's key.
    · The right subtree of a node contains only nodes with keys greater than the node's key.
    · Both the left and right subtrees must also be binary search trees.
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
    def isValidBST(self, root):
        if not root:
            return True
        return self.isValid(root,None,None)

    def isValid(self, root, minnum, maxnum):
        # !!! 注意，此处不可写为if minnum，否则minnum==0时也是false
        if minnum!=None:
            if root.val<=minnum:
                return False
        if maxnum!=None:
            if root.val>=maxnum:
                return False
        if root.left:
            if self.isValid(root.left,minnum,root.val)==False:
                return False
        if root.right:
            if self.isValid(root.right,root.val,maxnum)==False:
                return False
        return True
        

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=TreeNode(2)
        a.left=TreeNode(1)
        a.right=TreeNode(3)
        self.assertEqual(self.a.isValidBST(a),True)
        self.assertEqual(self.a.isValidBST(None),True)
        a=TreeNode(0)
        a.right=TreeNode(-1)
        self.assertEqual(self.a.isValidBST(a),False)


if __name__ == '__main__':
    unittest.main()