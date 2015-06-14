# encoding: utf8
'''
Flatten Binary Tree to Linked List
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hints:
If you notice carefully in the flattened tree, each node's 
right child points to the next node of a pre-order traversal.

如果有左子树和右子树，则把右子树挂到左子树的右叶节点，然后把左子树挂到右子树的位置，递归。
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
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        if root==None:
            return
        if root.left==None:
            self.flatten(root.right)
            return
        left=root.left
        right=root.right
        root.right=left
        root.left=None
        while left.right:
            left=left.right
        left.right=right
        self.flatten(root.right)

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=TreeNode(3)
        a.left=TreeNode(9)
        a.left.left=TreeNode(15)
        a.left.right=TreeNode(7)
        a.right=TreeNode(20)
        self.a.flatten(a)
        print(a.val, a.right.val, a.right.right.val, a.right.right.right.val)

        a=TreeNode(1)
        a.left=TreeNode(2)
        a.right=TreeNode(3)
        self.a.flatten(a)
        print(a.val, a.right.val, a.right.right.val)

        a=TreeNode(1)
        a.left=TreeNode(2)
        self.a.flatten(a)
        print(a.val, a.right.val)

        a=TreeNode(1)
        self.a.flatten(a)


if __name__ == '__main__':
    unittest.main()