# encoding: utf8
'''
Intersection of Two Linked Lists 
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

先求链表a的长度la，再求链表b的长度lb。如果后面相同，则后面的长度也必定相同。
故知道长度以后，长的链表先把头指针后移，使两链表剩下部分长度相同。再依此比较即可。
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
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        la=0
        p=headA
        while p:
            la+=1
            p=p.next
        lb=0
        p=headB
        while p:
            lb+=1
            p=p.next
        pa=headA
        pb=headB
        for i in range(la-lb):
            pa=pa.next
        for i in range(lb-la):
            pb=pb.next
        while pa and pb and pa!=pb:
            pa=pa.next
            pb=pb.next
        return pa


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=MinStack()

    def testLeet(self):
        # self.assertEqual(self.a.findMin([3,1,2]), 1)
        # self.a.push(10)
        # self.a.push(3)
        # print self.a.getMin()
        # self.a.pop()
        # print self.a.getMin()
        
        # self.a.push(-1)
        # print self.a.top()
        # print self.a.getMin()

        self.a.push(-2)
        self.a.push(0)
        self.a.push(-1)
        print self.a.getMin()
        print self.a.top()
        self.a.pop
        print self.a.getMin()


if __name__ == '__main__':
    unittest.main()