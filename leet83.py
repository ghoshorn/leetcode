# encoding: utf8
'''
Remove Duplicates from Sorted List 
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
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
    def deleteDuplicates(self, head):
        if head==None:
            return None
        p=head
        while p:
            if p.next and p.val==p.next.val:
                p.next=p.next.next
            else:
                p=p.next
        return head

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=ListNode(1)
        a.next=ListNode(1)
        a.next.next=ListNode(1)
        a.next.next.next=ListNode(2)
        a.next.next.next.next=ListNode(3)
        self.a.deleteDuplicates(a)
        p=a
        while p:
            print p.val
            p=p.next
        # self.assertEqual(self.a.deleteDuplicates(a),2)


if __name__ == '__main__':
    unittest.main()