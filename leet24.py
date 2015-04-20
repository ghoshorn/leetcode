# encoding: utf8
'''
Swap Nodes in Pairs  
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head==None:
            return None
        if head.next:
            p1=head
            p2=head.next
            p1.next=p2.next
            p2.next=head
            head=p2
        else:
            return head
        pre=p1
        if pre:
            p1=pre.next
            if p1:
                p2=p1.next
        else:
            p1=p2=None
        while p1 and p2:
            pre.next=p2
            p1.next=p2.next
            p2.next=p1
            pre=p1
            if pre:
                p1=pre.next
                if p1:
                    p2=p1.next
        return head


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()
    def testLeet(self):
        self.assertEqual(self.a.letterCombinations(""),[])

if __name__ == '__main__':
    # unittest.main()
    head=ListNode(1)
    head.next=ListNode(2)
    # head.next.next=ListNode(3)
    # head.next.next.next=ListNode(4)
    # head.next.next.next.next=ListNode(5)
    p=head
    while p:
        print p.val,
        p=p.next
    print
    a=Solution()
    p=a.swapPairs(head)
    while p:
        print p.val,
        p=p.next