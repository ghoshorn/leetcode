# encoding: utf8
'''
Partition List 
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

开始理解错了题意，当做了快排的partition，把比x小的都放到了x左边，比x大的都放到了x右边。
于是用了3个链表head1 xhead head2
而题目只要求把比x小的放比x大的左边就好。只用2个链表即可。
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
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        head1=None
        tail1=None
        head2=None
        tail2=None
        p=head
        while p:
            if p.val<x:
                if tail1:
                    tail1.next=p
                    tail1=tail1.next
                else:
                    head1=p
                    tail1=p
            else:
                if tail2:
                    tail2.next=p
                    tail2=tail2.next
                else:
                    head2=p
                    tail2=p
            p=p.next
        if head1==None:
            head1=head2
        if tail1:
            tail1.next=head2
        if tail2:
            tail2.next=None
        return head1


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=ListNode(1)
        # a.next=ListNode(4)
        # a.next.next=ListNode(3)
        # a.next.next.next=ListNode(2)
        # a.next.next.next.next=ListNode(5)
        # a.next.next.next.next.next=ListNode(2)
        p=self.a.partition(a,1)
        while p:
            print p.val
            p=p.next
        # self.assertEqual(self.a.deleteDuplicates(a),2)


if __name__ == '__main__':
    unittest.main()