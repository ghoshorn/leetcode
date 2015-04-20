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
    head1.next=ListNode(3)
    head2=ListNode(2)
    head2.next=ListNode(4)
    head2.next.next=ListNode(5)
    a=Solution()
    p=a.mergeTwoLists(head1,head2)
    while p:
        print p.val,
        p=p.next