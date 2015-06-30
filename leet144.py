# encoding: utf8
'''
Binary Tree Preorder Traversal
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
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
    # @return {integer[]}
    def preorderTraversal(self, root):
        self.ans=[]
        self.go(root)
        return self.ans

    def go(self, root):
        if root:
            self.ans.append(root.val)
            if root.left:
                self.go(root.left)
            if root.right:
                self.go(root.right)

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        ans=[]
        queue=[]
        head=0
        tail=0
        if root:
            queue.append(root)
            tail=1
        while head<tail:
            ans.append(queue[head].val)
            if queue[head].right:
                queue.insert(head+1,queue[head].right)
                tail+=1
            if queue[head].left:
                queue.insert(head+1,queue[head].left)
                tail+=1
            head+=1
        return ans

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=TreeNode(1)
        a.left=TreeNode(4)
        a.right=TreeNode(3)
        a.left.left=TreeNode(2)
        self.assertEqual(self.a.preorderTraversal(a),[1,4,2,3])
        

if __name__ == '__main__':
    unittest.main()