# encoding: utf8
'''
Invert Binary Tree
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
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
    # @return {TreeNode}
    def invertTree(self, root):
        if root==None:
            return root
        root.left, root.right=root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root
        

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.calculate("1 + 1"), 2)
        self.assertEqual(self.a.calculate(" 2-1 + 2 "), 3)

if __name__ == '__main__':
    unittest.main()