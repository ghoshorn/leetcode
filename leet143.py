# encoding: utf8
'''
Reorder List
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}
先找到链表的中间节点，断开后把后半部分翻转，然后再合并。
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
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if head==None or head.next==None:
            return
        p=head
        n=0
        while p:
            n+=1
            p=p.next

        p=head
        n=n/2
        while n:
            n-=1
            p=p.next
        p2=p.next
        p.next=None

        if p2==None:
            return
        p=p2.next
        p2.next=None
        while p:
            pp=p.next
            p.next=p2
            p2=p
            p=pp

        # p=head
        # while p:
        #     print p.val,
        #     p=p.next
        # print '\n'

        # p=p2
        # while p:
        #     print p.val,
        #     p=p.next
        # print '\n'

        p1=head
        while p2:
            tmp=p2
            p2=p2.next
            tmp.next=p1.next
            tmp1=p1
            p1=p1.next
            tmp1.next=tmp
        

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        # self.assertEqual(self.a.wordBreak('leetcode',['leet','code']),True)
        a=ListNode(1)
        a.next=ListNode(2)
        a.next.next=ListNode(3)
        a.next.next.next=ListNode(4)
        a.next.next.next.next=ListNode(5)
        # a.next.next.next.next.next=ListNode(6)
        self.a.reorderList(a)
        while a:
            print a.val
            a=a.next
        self.a.reorderList(None)
        self.a.reorderList(ListNode(1))

if __name__ == '__main__':
    unittest.main()