# encoding: utf8
'''
Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
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
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if head==None:
            return
        while head and head.val==val:
            head=head.next
        p=head
        if p:
            while p.next:
                if p.next.val==val:
                    p.next=p.next.next
                else:
                    p=p.next
        return head

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        # self.assertEqual(self.a.isHappy(19), True)
        a=ListNode(1)
        a.next=ListNode(2)
        a.next.next=ListNode(6)
        a.next.next.next=ListNode(3)
        a.next.next.next.next=ListNode(4)
        self.a.removeElements(a,6)
        while a:
            print a.val,
            a=a.next

        a=ListNode(1)
        self.a.removeElements(a,1)
        while a:
            print a.val,
            a=a.next


if __name__ == '__main__':
    unittest.main()