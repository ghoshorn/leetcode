# encoding: utf8
'''
Sort List
Sort a linked list in O(n log n) time using constant space complexity.
要求O(nlogn)，应该只有归并排序了吧。
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
    def sortList(self, head):
        if head==None:
            return None
        ans=self.mergesort(head)
        return ans

    def mergesort(self, head):
        if head.next==None:
            return head
        slow=head
        fast=head
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        p1=head
        p2=slow.next
        slow.next=None
        l1=self.mergesort(p1)
        l2=self.mergesort(p2)
        return self.merge(l1,l2)

    def merge(self, head1, head2):
        head=ListNode(0)
        p=head
        while head1 and head2:
            if head1.val<=head2.val:
                p.next=head1
                head1=head1.next
            else:
                p.next=head2
                head2=head2.next
            p=p.next
        while head1:
            p.next=head1
            head1=head1.next
            p=p.next
        while head2:
            p.next=head2
            head2=head2.next
            p=p.next
        head=head.next
        return head

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
        x=self.a.sortList(a)
        while x:
            print x.val
            x=x.next
        a=ListNode(1)
        a.next=ListNode(1)
        x=self.a.sortList(a)
        while x:
            print x.val
            x=x.next
        a=ListNode(3)
        a.next=ListNode(2)
        a.next.next=ListNode(4)
        x=self.a.sortList(a)
        while x:
            print x.val
            x=x.next

        b=ListNode(0)
        head=b
        for i in range(1,5000):
            b.next=ListNode(i)
            b=b.next
        self.a.sortList(head)

if __name__ == '__main__':
    unittest.main()