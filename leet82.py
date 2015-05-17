# encoding: utf8
'''
Remove Duplicates from Sorted List II
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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
        newhead=head
        if head.next and head.val!=head.next.val:
            newhead=head
        else:
            while newhead:
                if newhead.next and newhead.val==newhead.next.val:
                    tmp=newhead.val
                    while newhead and newhead.val==tmp:
                        newhead=newhead.next
                else:
                    break
        if newhead:
            print 'newhead '+str(newhead.val)
        pre=newhead
        if pre:
            p=pre.next
        else:
            p=None
        while p:
            while p and p.next and p.val==p.next.val:
                tmp=p.val
                while p and p.val==tmp:
                    p=p.next
            pre.next=p
            pre=pre.next
            if p:
                p=p.next
        return newhead

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=ListNode(1)
        a.next=ListNode(2)
        a.next.next=ListNode(2)
        # a.next.next.next=ListNode(3)
        # a.next.next.next.next=ListNode(4)
        # a.next.next.next.next.next=ListNode(4)
        # a.next.next.next.next.next.next=ListNode(5)
        p=self.a.deleteDuplicates(a)
        while p:
            print p.val
            p=p.next
        # self.assertEqual(self.a.deleteDuplicates(a),2)


if __name__ == '__main__':
    unittest.main()