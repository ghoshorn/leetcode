# encoding: utf8
'''
Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

把前半部分链表逆序后，再与后半部分链表比较。
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
    # @return {boolean}
    def isPalindrome(self, head):
        if head==None:
            return True
        p   =head
        cnt =0
        while p:
            p   =p.next
            cnt +=1
        if cnt%2==1:
            odd=True
        else:
            odd=False
        cnt =(cnt-1)/2
        p   =head
        while cnt>0:
            p=p.next
            cnt-=1
        p2     =p.next # p2=behind half linked list
        p.next =None 
        p      =head # p=front half linked list
        # reverse the front half
        post   =p.next
        p.next =None
        while post:
            pre    =p
            p      =post
            post   =p.next
            p.next =pre
        if odd:
            p=p.next
        while p and p2:
            if p.val!=p2.val:
                return False
            p=p.next
            p2=p2.next
        return True

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        a=ListNode(1)
        a.next=ListNode(2)
        a.next.next=ListNode(3)
        a.next.next.next=ListNode(2)
        a.next.next.next.next=ListNode(1)
        self.assertEqual(self.a.isPalindrome(a), True)
        self.assertEqual(self.a.isPalindrome(ListNode(1)), True)
        self.assertEqual(self.a.isPalindrome(None), True)


if __name__ == '__main__':
    unittest.main()