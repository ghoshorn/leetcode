# encoding: utf8
'''
Remove Nth Node From End of List  
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

用两个指针p1=head, p2=head。先让p2后移n次，再同步后移至p2==Null即可。
需要注意当p2后移n次时，p2==Null的情况。
'''

import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        p2=head;
        while (n>0):
            p2=p2.next
            n-=1
        if p2==None:
            return head.next
        p1=head
        while p2.next:
            p1=p1.next
            p2=p2.next
        p1.next=p1.next.next
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
    # head.next=ListNode(2)
    # head.next.next=ListNode(3)
    # head.next.next.next=ListNode(4)
    # head.next.next.next.next=ListNode(5)
    p=head
    while p:
        print p.val,
        p=p.next
    print
    a=Solution()
    p=a.removeNthFromEnd(head,1)
    while p:
        print p.val,
        p=p.next