# encoding: utf8
'''
Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
注意： 必须到叶节点
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
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if root==None:
            return False
        self.result=False
        self.go(root,sum)
        return self.result

    def go(self, root, val):
        if root==None:
            return
        if root.val==val and root.left==None and root.right==None:
            self.result=True
            return
        if root.left:
            self.go(root.left, val-root.val)
        if root.right:
            self.go(root.right, val-root.val)

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
        self.assertEqual(self.a.hasPathSum(a,2),False)

        a=TreeNode(1)
        a.left=TreeNode(2)
        a.right=TreeNode(3)
        self.assertEqual(self.a.hasPathSum(a,4),True)

        a=TreeNode(1)
        a.left=TreeNode(2)
        self.assertEqual(self.a.hasPathSum(a,1),False)

        a=TreeNode(1)
        self.assertEqual(self.a.hasPathSum(a,1),True)


if __name__ == '__main__':
    unittest.main()