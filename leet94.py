# encoding: utf8
'''
Binary Tree Inorder Traversal 
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
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
    # @return {integer[]}
    def inorderTraversal(self, root):
        if root==None:
            return []
        self.ans=[]
        self.inorder(root)
        return self.ans

    def inorder(self, p):
        if p.left:
            self.inorder(p.left)
        self.ans.append(p.val)
        if p.right:
            self.inorder(p.right)

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=TreeNode(1)
        a.right=TreeNode(2)
        a.right.left=TreeNode(3)
        self.assertEqual(self.a.inorderTraversal(a),[1,3,2])


if __name__ == '__main__':
    unittest.main()