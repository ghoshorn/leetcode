# encoding: utf8
'''
Binary Tree Right Side View 
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4]

采用按层次遍历的方法即可。
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
    def rightSideView(self, root):
        if root==None:
            return []
        queue =[root]
        ret   =[]
        head  =tail = 0
        right = root
        while head<=tail:
            p=queue[head]
            if p==right:
                ret.append(p.val)
                right=None
            if p.right:
                queue.append(p.right)
                tail+=1
                if right==None:
                    right=p.right
            if p.left:
                queue.append(p.left)
                tail+=1
                if right==None:
                    right=p.left
            head+=1
        return ret

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=TreeNode(1)
        a.left=TreeNode(2)
        a.right=TreeNode(3)
        a.left.right=TreeNode(5)
        a.right.right=TreeNode(4)
        self.assertEqual(self.a.rightSideView(a), [1,3,4])


if __name__ == '__main__':
    unittest.main()