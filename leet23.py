# encoding: utf8
'''
Merge k Sorted Lists
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
可以通过leetcode 21的merge Two Lists来解决。

如果从头到尾依此合并，会超时。

改用分治法来调用。链表个数l>3时，mergeTwoLists(self.mergeKLists(lists[:l/2]),self.mergeKLists(lists[l/2:l]))
'''

import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1==None:
            return l2
        if l2==None:
            return l1
        if l1.val<=l2.val:
            head=l1
            l1=l1.next
        else:
            head=l2
            l2=l2.next
        p=head
        while l1 and l2:
            if l1.val<=l2.val:
                p.next=l1
                p=p.next
                l1=l1.next
            else:
                p.next=l2
                p=p.next
                l2=l2.next
        while l1:
            p.next=l1
            p=p.next
            l1=l1.next
        while l2:
            p.next=l2
            p=p.next
            l2=l2.next
        return head

    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists1(self, lists):
        l=len(lists)
        if l==0:
            return None
        if l==1:
            return lists[0]
        head=self.mergeTwoLists(lists[0],lists[1])
        for i in range(2,l):
            head=self.mergeTwoLists(head,lists[i])
        return head

    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        l=len(lists)
        if l==0:
            return None
        elif l==1:
            return lists[0]
        elif l==2:
            return self.mergeTwoLists(lists[0],lists[1])
        else:
            return self.mergeTwoLists(self.mergeKLists(lists[:l/2]),self.mergeKLists(lists[l/2:l]))

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()
    def testLeet(self):
        self.assertEqual(self.a.isValid("()[]{}"),True)
        self.assertEqual(self.a.isValid("(]"),False)
        self.assertEqual(self.a.isValid("([)]"),False)

if __name__ == '__main__':
    # unittest.main()
    head1=ListNode(1)
    head1.next=ListNode(4)
    head2=ListNode(2)
    head2.next=ListNode(5)
    head2.next.next=ListNode(6)
    head3=ListNode(3)
    head3.next=ListNode(8)
    a=Solution()
    p=a.mergeKLists([head1,head2,head3])
    while p:
        print p.val,
        p=p.next