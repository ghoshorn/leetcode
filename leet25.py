import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head==None:
            return None
        if k==1:
            return head
        cnt=1
        p=head
        while p and cnt<k:
            p=p.next
            cnt+=1
        if cnt<k or p==None:
            return head
        p1=head
        p2=p1.next
        p3=p2.next
        cnt=1
        p1.next=p.next
        pre=p1
        while cnt<k:
            p2.next=p1
            p1=p2
            p2=p3
            if p3:
                p3=p3.next
            cnt+=1
        head=p

        while  True:
            cnt=1
            p=pre.next
            while p and cnt<k:
                p=p.next
                cnt+=1
            if cnt<k or p==None:
                break
            p1=pre.next
            p2=p1.next
            p3=p2.next
            cnt=1
            while cnt<k:
                p2.next=p1
                p1=p2
                p2=p3
                if p3:
                    p3=p3.next
                cnt+=1
            tmp=pre.next
            # pre.next=p2
            pre.next=p1 #mod
            pre=tmp
            tmp.next=p2 #add

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
    head.next.next=ListNode(3)
    head.next.next.next=ListNode(4)
    # head.next.next.next.next=ListNode(5)
    p=head
    while p:
        print p.val,
        p=p.next
    print
    a=Solution()
    p=a.reverseKGroup(head,2)
    while p:
        print p.val,
        p=p.next