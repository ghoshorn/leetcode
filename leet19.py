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