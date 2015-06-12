# encoding: utf8
'''
Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
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
    # @return {integer[][]}
    def pathSum(self, root, sum):
        if root==None:
            return []
        self.result=[]
        self.go(root,sum,[])
        return self.result

    def go(self, root, val, path):
        if root==None:
            return
        if root.val==val and root.left==None and root.right==None:
            path+=[val]
            self.result.append(path)
            return
        if root.left:
            self.go(root.left, val-root.val, path+[root.val])
        if root.right:
            self.go(root.right, val-root.val, path+[root.val])

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
        self.assertEqual(self.a.pathSum(a,2),[])

        a=TreeNode(1)
        a.left=TreeNode(2)
        a.right=TreeNode(3)
        self.assertEqual(self.a.pathSum(a,4),[[1,3]])

        a=TreeNode(1)
        a.left=TreeNode(2)
        self.assertEqual(self.a.pathSum(a,1),[])

        a=TreeNode(1)
        self.assertEqual(self.a.pathSum(a,1),[[1]])


if __name__ == '__main__':
    unittest.main()