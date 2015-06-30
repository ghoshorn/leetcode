# encoding: utf8
'''
Insertion Sort List
Sort a linked list using insertion sort.
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
    def insertionSortList(self, head):
        if head==None:
            return None
        head0=head
        shead=head0
        tail=shead
        head0=head0.next
        shead.next=None
        while head0:
            tobeinsert=head0
            head0=head0.next
            tobeinsert.next=None

            if shead.val>=tobeinsert.val:
                tobeinsert.next=shead
                shead=tobeinsert
            else:
                if tobeinsert.val>=tail.val:
                    tail.next=tobeinsert
                    tail=tail.next
                    continue
                p=shead
                # pre=None
                while p and p.val<tobeinsert.val:
                    pre=p
                    p=p.next
                tobeinsert.next=p
                pre.next=tobeinsert
        return shead

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        # self.assertEqual(self.a.preorderTraversal(a),[1,4,2,3])
        a=ListNode(4)
        a.next=ListNode(2)
        a.next.next=ListNode(3)
        a.next.next.next=ListNode(1)
        x=self.a.insertionSortList(a)
        while x:
            print x.val
            x=x.next
        a=ListNode(1)
        a.next=ListNode(1)
        x=self.a.insertionSortList(a)
        while x:
            print x.val
            x=x.next
        a=ListNode(3)
        a.next=ListNode(2)
        a.next.next=ListNode(4)
        x=self.a.insertionSortList(a)
        while x:
            print x.val
            x=x.next

        b=ListNode(0)
        head=b
        for i in range(1,5000):
            b.next=ListNode(i)
            b=b.next
        self.a.insertionSortList(head)

if __name__ == '__main__':
    unittest.main()