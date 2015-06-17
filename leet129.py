# encoding: utf8
'''
Sum Root to Leaf Numbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
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
    def sumNumbers(self, root):
        self.tot=0
        self.go(0,root)
        return self.tot

    def go(self, now, root):
        if root==None:
            return
        if root.left:
            self.go(10*now+root.val, root.left)
        if root.right:
            self.go(10*now+root.val, root.right)
        if root.left==root.right==None:
            self.tot+= now*10+root.val
            return


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=TreeNode(1)
        a.left=TreeNode(2)
        a.right=TreeNode(3)
        self.assertEqual(self.a.sumNumbers(a),25)
        
        self.assertEqual(self.a.sumNumbers(None),0)

if __name__ == '__main__':
    unittest.main()