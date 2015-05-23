# encoding: utf8
'''
Reverse Linked List II
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
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
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if m==n:
            return head
        p=head
        cnt1=m-1
        cnt2=n-m+1
        tail1=None
        if cnt1:
            tail1=p
            cnt1-=1
            p=p.next
        while p and cnt1:
            tail1=p
            p=p.next
            cnt1-=1
        head2=p
        tail2=p
        if cnt2:
            cnt2-=1
            p=p.next
        while p and cnt2:
            tmp=p.next
            p.next=head2
            head2=p
            p=tmp
            cnt2-=1
        if tail1:
            tail1.next=head2
        tail2.next=p
        if m==1:
            return head2
        else:
            return head

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=ListNode(1)
        a.next=ListNode(2)
        a.next.next=ListNode(3)
        a.next.next.next=ListNode(4)
        a.next.next.next.next=ListNode(5)
        p=self.a.reverseBetween(a,3,4)
        while p:
            print p.val
            p=p.next
        # self.assertEqual(self.a.deleteDuplicates(a),2)


if __name__ == '__main__':
    unittest.main()