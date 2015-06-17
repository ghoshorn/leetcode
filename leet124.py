# encoding: utf8
'''
Binary Tree Maximum Path Sum
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,
  1
 / \
2   3
Return 6.

递归的查找当前节点中，左子树和右子树的最大值，则当前节点的最大值为
当前节点本身/当前节点加上左子树/当前节点加上右子树/当前节点加上左右子树。
注意，当查找子树的最大值时，不可同时包含左右子树。
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
    def maxPathSum(self, root):
        if root==None:
            return 0
        self.max=None
        max1=self.maxsum(root)
        return max(max1, self.max)

    # 返回值只可能包含左/右子树其中之一，不可以都有。
    # self.max只可以都包含。
    def maxsum(self, root):
        if root==None:
            return -32768
        left=right=-32768
        if root.left:
            left=self.maxsum(root.left)
        if root.right:
            right=self.maxsum(root.right)
        if self.max==None:
            self.max=max(left, right, left+right+root.val)
        else:
            self.max=max(left, right, left+right+root.val, self.max)
        return max(left+root.val, root.val+right, root.val)

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=TreeNode(1)
        a.left=TreeNode(2)
        a.right=TreeNode(3)
        self.assertEqual(self.a.maxPathSum(a.left),2)
        self.assertEqual(self.a.maxPathSum(a.right),3)
        self.assertEqual(self.a.maxPathSum(a),6)

        a2=TreeNode(-1)
        a2.left=TreeNode(2)
        a2.right=TreeNode(4)
        a2.left.left=TreeNode(3)
        a2.right.left=TreeNode(-2)
        a2.right.right=TreeNode(1)
        self.assertEqual(self.a.maxPathSum(a2),9)

        a3=TreeNode(-2)
        a3.left=TreeNode(1)
        self.assertEqual(self.a.maxPathSum(a3),1)

        a4=TreeNode(-3)
        self.assertEqual(self.a.maxPathSum(a4),-3)

        a5=TreeNode(1)
        a5.left=TreeNode(-2)
        a5.right=TreeNode(-3)
        a5.left.left=TreeNode(1)
        a5.left.right=TreeNode(3)
        a5.right.left=TreeNode(-2)
        a5.left.left.left=TreeNode(-1)
        self.assertEqual(self.a.maxPathSum(a5.left.left.left),-1)
        self.assertEqual(self.a.maxPathSum(a5.right.left),-2)
        self.assertEqual(self.a.maxPathSum(a5.left.left),1)
        self.assertEqual(self.a.maxPathSum(a5.left),3)
        self.assertEqual(self.a.maxPathSum(a5),3)

        a6=TreeNode(5)
        a6.left=TreeNode(4)
        a6.left.left=TreeNode(11)
        a6.right=TreeNode(8)
        a6.right.left=TreeNode(13)
        a6.right.right=TreeNode(4)
        a6.right.left.left=TreeNode(7)
        a6.right.left.right=TreeNode(2)
        a6.right.left.left.right=TreeNode(1)
        self.assertEqual(self.a.maxPathSum(a6),49)

if __name__ == '__main__':
    unittest.main()