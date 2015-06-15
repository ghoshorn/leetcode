# encoding: utf8
'''
Populating Next Right Pointers in Each Node
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
'''

import unittest
from pprint import pprint
import pdb

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            self.inner_connect(root)
            self.inter_connect(root)
            self.connect(root.left)
            self.connect(root.right)

    # 解决内部的next连接，如2->3, 4->5
    def inner_connect(self, root):
        if root and root.left:
            root.left.next=root.right

    # 解决之间的next连接，如5->6
    def inter_connect(self, root):
        if root and root.left and root.left.right:
            p_left=root.left
            p_right=root.right
            while p_left.right and p_right.left:
                p_left=p_left.right
                p_right=p_right.left
                p_left.next=p_right

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        # a             =TreeLinkNode(1)
        # a.left        =TreeLinkNode(2)
        # a.right       =TreeLinkNode(3)
        # a.left.left   =TreeLinkNode(4)
        # a.left.right  =TreeLinkNode(5)
        # a.right.left  =TreeLinkNode(6)
        # a.right.right =TreeLinkNode(7)
        # # self.a.connect(a)
        # self.assertEqual(a.left.next.val,3)
        # self.assertEqual(a.left.left.next.val,5)
        # self.assertEqual(a.left.right.next.val,6)

        a2                   =TreeLinkNode(-1)
        a2.left              =TreeLinkNode(0)
        a2.right             =TreeLinkNode(1)
        a2.left.left         =TreeLinkNode(2)
        a2.left.right        =TreeLinkNode(3)
        a2.right.left        =TreeLinkNode(4)
        a2.right.right       =TreeLinkNode(5)
        a2.left.left.left    =TreeLinkNode(6)
        a2.left.left.right   =TreeLinkNode(7)
        a2.left.right.left  =TreeLinkNode(8)
        a2.left.right.right  =TreeLinkNode(9)
        a2.right.left.left   =TreeLinkNode(10)
        a2.right.left.right  =TreeLinkNode(11)
        a2.right.right.left =TreeLinkNode(12)
        a2.right.right.right =TreeLinkNode(13)
        self.a.connect(a2)
        self.assertEqual(a2.left.next.val,1)
        self.assertEqual(a2.left.left.next.val,3)
        self.assertEqual(a2.left.right.next.val,4)
        self.assertEqual(a2.left.left.left.next.val,7)
        self.assertEqual(a2.left.left.right.next.val,8)
        self.assertEqual(a2.left.right.right.next.val,10)


if __name__ == '__main__':
    unittest.main()