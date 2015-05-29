# encoding: utf8
'''
Binary Tree Zigzag Level Order Traversal 
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

类似leetcode 102 Binary Tree Level Order Traversal,
每层加入节点的时候，如果该层是偶数层（0开始），则append(*);如果是奇数层，则insert(0,*)
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
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        self.ans=[]
        if root:
            self.go(root, 0)
        return self.ans

    def go(self, root, level):
        try:
            if level%2==0:
                self.ans[level].append(root.val)
            else:
                self.ans[level].insert(0,root.val)
        except Exception, e:
            self.ans.append([root.val])
        if root.left:
            self.go(root.left, level+1)
        if root.right:
            self.go(root.right, level+1)

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=TreeNode(3)
        a.left=TreeNode(9)
        a.right=TreeNode(20)
        a.right.left=TreeNode(15)
        a.right.right=TreeNode(7)
        self.assertEqual(self.a.zigzagLevelOrder(a),[[3],[20,9],[15,7]])

        a=TreeNode(1)
        a.left=TreeNode(2)
        a.right=TreeNode(3)
        self.assertEqual(self.a.zigzagLevelOrder(a),[[1],[3,2]])


if __name__ == '__main__':
    unittest.main()