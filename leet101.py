# encoding: utf8
'''
Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
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
    def isSymmetric(self, root):
        if root==None:
            return True
        return self.check(root.left, root.right)

    def check(self, a, b):
        if a==b==None:
            return True
        if a and b:
            print a.val, b.val
            if a.val!=b.val:
                return False
            else:
                return self.check(a.left, b.right) and self.check(b.left, a.right)
        else:
            return False
        

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=TreeNode(1)
        a.left=TreeNode(2)
        a.right=TreeNode(2)
        self.assertEqual(self.a.isSymmetric(a),True)
        self.assertEqual(self.a.isSymmetric(a.left),True)


if __name__ == '__main__':
    unittest.main()