# encoding: utf8
'''
Min Stack 
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

import unittest
from pprint import pprint
import pdb

class MinStack:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    # initialize your data structure here.
    def __init__(self):
        self.ptop=None
        self.min=None

    # @param x, an integer
    # @return nothing
    def push(self, x):
        p=self.ListNode(x)
        p.next=self.ptop
        self.ptop=p

        if self.min==None or x<self.min.val:
            p=self.ListNode(x)
        else:
            p=self.ListNode(self.min.val)
        p.next=self.min
        self.min=p

    # @return nothing
    def pop(self):
        self.ptop=self.ptop.next
        self.min=self.min.next

    # @return an integer
    def top(self):
        return self.ptop.val

    # @return an integer
    def getMin(self):
        return self.min.val


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