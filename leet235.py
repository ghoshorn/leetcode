# encoding: utf8
'''
Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in 
the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow 
    a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of 
nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

OJ上WA
Input: [2,1], node with value 2, node with value 1
Output: 0
Expected: 2
但是本地测试是输出的2.。。
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

class Solution1:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if p<root.val and q<root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p>root.val and q>root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root.val

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root==None:
            return 0
        elif root.val==p: # p在当前节点，q在子树
            if self.hasX(root.left, q) or self.hasX(root.right, q):
                return root.val
        elif root.val==q: # q在当前节点，p在子树
            if self.hasX(root.left, p) or self.hasX(root.right, p):
                return root.val
        elif self.hasX(root.left, p) and self.hasX(root.right, q) or \
            self.hasX(root.left, q) and self.hasX(root.right, p): # 分别在左右子树
            return root.val
        elif self.hasX(root.left, p) and self.hasX(root.left, q): # 都在左子树
            return self.lowestCommonAncestor(root.left, p, q)
        elif self.hasX(root.right, p) and self.hasX(root.right, q): # 都在右子树
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return 0

    def hasX(self, root, x):
        if root==None:
            return False
        if root.val==x:
            return True
        if x<root.val:
            return self.hasX(root.left, x)
        else:
            return self.hasX(root.right, x)
        

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        b=TreeNode(2)
        b.left=TreeNode(1)
        self.assertEqual(self.a.lowestCommonAncestor(b, 2, 1), 2)

        c=TreeNode(1)
        c.right=TreeNode(2)
        self.assertEqual(self.a.lowestCommonAncestor(c, 2, 1), 1)

        a=TreeNode(6)
        a.left=TreeNode(2)
        a.left.left=TreeNode(0)
        a.left.right=TreeNode(4)
        a.left.right.left=TreeNode(3)
        a.left.right.right=TreeNode(5)
        a.right=TreeNode(8)
        a.right.left=TreeNode(7)
        a.right.right=TreeNode(9)
        self.assertEqual(self.a.lowestCommonAncestor(a, 2, 8), 6)
        self.assertEqual(self.a.lowestCommonAncestor(a, 2, 4), 2)


if __name__ == '__main__':
    unittest.main()