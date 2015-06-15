# encoding: utf8
'''
Populating Next Right Pointers in Each Node II
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL

Solution1:
首先想到利用上一题的思路，解决inter的问题的时候分别增加右优先和左优先，
但是遇到
         1
       /  \
      2    3
     / \    \
    4   5    6
   /          \
   7            8
的时候无法使7->8.
改为对每个节点，分别找到其左子树第i层最右边的节点，以及右子树第i层最左边的节点，
然后连接起来，结果超时。。

换种思路（from leetcode-cpp.pdf）
按层次来做，每次记录该层的prev和下一层的第一个节点next_level.
外层循环为按层次循环，每次新进如循环首先设置next_level表示下一层的第一个节点；
内层循环为当前层次从左到右，每次设置prev.next连接到下一个节点；
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
    def connect(self, root, dep=None):
        if root==None:
            return
        while root: # 层次
            prev=None # 该层的前一个节点
            next_level=None # 下一层的第一个节点
            while root: # 当前层还有节点
                if next_level==None:
                    if root.left:
                        next_level=root.left
                    elif root.right:
                        next_level=root.right
                if root.left:
                    if prev:
                        prev.next=root.left
                    prev=root.left
                if root.right:
                    if prev:
                        prev.next=root.right
                    prev=root.right
                root=root.next
            root=next_level

class Solution1:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root, dep=None):
        if dep==None and root:
            dep=min(self.get_depth(root.left),self.get_depth(root.right))
        if root:
            self.inner_connect(root)
            self.inter_connect(root, dep)
            self.connect(root.left, dep-1)
            self.connect(root.right, dep-1)

    def get_depth(self, root):
        if root:
            left=1+self.get_depth(root.left)
            right=1+self.get_depth(root.right)
            return max(left,right)
        else:
            return 0

    # 解决内部的next连接，如2->3, 4->5
    def inner_connect(self, root):
        if root and root.left and root.right:
            root.left.next=root.right

    # 解决之间的next连接，如5->7
    def inter_connect(self, root, dep):
        for d in range(1,dep):
            left=self.get_ith_dep_right_first(root.left, d)
            right=self.get_ith_dep_left_first(root.right, d)
            if left and left.next==None:
                left.next=right
            if left==right==None:
                break

    # 得到第dep层的最靠右的节点
    def get_ith_dep_right_first(self, root, dep):
        if dep==0:
            return root
        if root==None:
            return None
        right=self.get_ith_dep_right_first(root.right, dep-1)
        if right:
            return right
        else:
            left=self.get_ith_dep_right_first(root.left, dep-1)
            return left

    # 得到第dep层的最靠左的节点
    def get_ith_dep_left_first(self, root, dep):
        if dep==0:
            return root
        if root==None:
            return None
        left=self.get_ith_dep_left_first(root.left, dep-1)
        if left:
            return left
        else:
            right=self.get_ith_dep_left_first(root.right, dep-1)
            return right


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a             =TreeLinkNode(1)
        a.left        =TreeLinkNode(2)
        a.right       =TreeLinkNode(3)
        a.left.left   =TreeLinkNode(4)
        a.left.right  =TreeLinkNode(5)
        a.right.right =TreeLinkNode(7)
        self.a.connect(a)
        self.assertEqual(a.left.next.val,3)
        self.assertEqual(a.left.left.next.val,5)
        self.assertEqual(a.left.right.next.val,7)

        a2                   =TreeLinkNode(0)
        a2.left              =TreeLinkNode(2)
        a2.right             =TreeLinkNode(4)
        a2.left.left         =TreeLinkNode(1)
        a2.right.left        =TreeLinkNode(3)
        a2.right.right       =TreeLinkNode(-1)
        a2.left.left.right   =TreeLinkNode(6)
        a2.right.left.right  =TreeLinkNode(8)
        self.a.connect(a2)
        self.assertEqual(a2.left.next.val,4)
        self.assertEqual(a2.left.left.next.val,3)
        self.assertEqual(a2.left.left.right.next.val,8)

        a3                   =TreeLinkNode(1)
        a3.left              =TreeLinkNode(2)
        a3.left.left         =TreeLinkNode(4)
        a3.left.right        =TreeLinkNode(5)
        a3.left.left.left    =TreeLinkNode(7)
        a3.right             =TreeLinkNode(3)
        a3.right.right       =TreeLinkNode(6)
        a3.right.right.right =TreeLinkNode(8)
        self.a.connect(a3)
        self.assertEqual(a3.left.right.next.val, 6)
        self.assertEqual(a3.left.left.left.next.val, 8)

        self.a.connect(None)

        a4                   =TreeLinkNode(1)
        a4.left              =TreeLinkNode(2)
        self.a.connect(a4)


if __name__ == '__main__':
    unittest.main()