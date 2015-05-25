# encoding: utf8
'''
Same Tree
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical 
and the nodes have the same value.
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
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        return self.check(p,q)

    def check(self, a, b):
        if a==b==None:
            return True
        if a and b:
            if a.val!=b.val:
                return False
            else:
                return self.check(a.left,b.left) and self.check(a.right,b.right)
        else:
            return False
        

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=TreeNode(2)
        a.left=TreeNode(1)
        a.right=TreeNode(3)
        self.assertEqual(self.a.isSameTree(a,a),True)
        self.assertEqual(self.a.isSameTree(a,a.left),False)


if __name__ == '__main__':
    unittest.main()