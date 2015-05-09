# encoding: utf8
'''
Rotate List 
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL

思路：类似于找链表的倒数第k个点。
需要考虑的特殊情况：
1，空
2，k比链表的长度更大
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
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if head==None:
            return None
        h2=head
        l=0
        while k>0:
            l+=1
            h2=h2.next
            k-=1
            if h2==None:
                h2=head
                k=k%l
        h1=head
        if h2:
            while h2.next:
                h1=h1.next
                h2=h2.next
            # print h1.val,",",h2.val
            h2.next=head
            head=h1.next
            h1.next=None
            p=head
            # while p:
            #     print p.val,' ',
            #     p=p.next
        return head


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        # self.assertEqual(self.a.rotateRight(None,0),None)
        a=ListNode(1)
        self.assertEqual(self.a.rotateRight(a,99),a)
        a.next=ListNode(2)
        a.next.next=ListNode(3)
        self.assertEqual(self.a.rotateRight(a,200),a)
        a.next.next.next=ListNode(4)
        a.next.next.next.next=ListNode(5)
        self.assertEqual(self.a.rotateRight(a,2),'123')
        

if __name__ == '__main__':
    unittest.main()
