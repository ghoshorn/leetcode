'''
Add Two Numbers
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        n1=l1
        n2=l2
        result=n1.val+n2.val
        carry=result%10
        if result>=10:
            carry=1
            result-=10
        else:
            carry=0
        head=ListNode(result)
        p=head
        n1=n1.next
        n2=n2.next
        while n1 and n2:
            result=n1.val+n2.val+carry
            if result>=10:
                carry=1
                result-=10
            else:
                carry=0
            n=ListNode(result)
            p.next=n
            p=n
            n1=n1.next
            n2=n2.next
        while n1:
            result=n1.val+carry
            if result>=10:
                carry=1
                result-=10
            else:
                carry=0
            n=ListNode(result)
            p.next=n
            p=n
            n1=n1.next
        while n2:
            result=n2.val+carry
            if result>=10:
                carry=1
                result-=10
            else:
                carry=0
            n=ListNode(result)
            p.next=n
            p=n
            n2=n2.next
        if carry==1:
            n=ListNode(1)
            p.next=n
        return head


a=Solution()
l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)
l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)
l=a.addTwoNumbers(l1,l2)
while l:
    print l.val
    l=l.next

l1=ListNode(5)
l2=ListNode(5)
l=a.addTwoNumbers(l1,l2)
while l:
    print l.val
    l=l.next