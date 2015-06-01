# encoding: utf8
'''
Convert Sorted Array to Binary Search Tree
Given an array where elements are sorted in ascending order, 
convert it to a height balanced BST.
和leetcode 108 的思路一样
'''

import unittest
from pprint import pprint
import pdb

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if head==None:
            return None
        if head.next==None:
            return TreeNode(head.val) # 此处不要写为 return head
        cnt=0
        p=head
        while p:
            p=p.next
            cnt+=1
        cnt=cnt/2
        p=head.next
        cnt-=1
        pre=head
        while cnt:
            cnt-=1
            pre=p
            p=p.next
        pre.next=None
        root=TreeNode(p.val)
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(p.next)
        return root


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        sl=ListNode(1)
        sl.next=ListNode(2)
        sl.next.next=ListNode(3)
        # self.assertEqual(self.a.sortedArrayToBST([1,2,3]),a)
        r=self.a.sortedListToBST(sl)
        print r.val, r.left.val, r.right.val

        sl=ListNode(1)
        sl.next=ListNode(3)
        # self.assertEqual(self.a.sortedArrayToBST([1,2,3]),a)
        r=self.a.sortedListToBST(sl)
        print r.val, r.left.val

if __name__ == '__main__':
    unittest.main()