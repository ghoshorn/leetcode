# encoding: utf8
'''
Reverse Linked List 
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

import unittest
from pprint import pprint
import pdb

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head==None:
            return None
        newhead=None
        p=head
        while p:
            headnext=p.next
            p.next=newhead
            newhead=p
            p=headnext
        return newhead

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        # self.assertEqual(self.a.isIsomorphic("paper", "title"), True)
        a=ListNode(1)
        a.next=ListNode(2)
        # a.next.next=ListNode(3)
        self.a.reverseList(a)
        while a:
            print a.val
            a=a.next


if __name__ == '__main__':
    unittest.main()