# encoding: utf8
'''
Implement Queue using Stacks 
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

使用两个栈，一个用来放新插入的节点，一个用来输出节点。
只有当输出的栈为空的时候，才把输入的栈的内容转移到输出的栈中。
平均下来，时间复杂度为O(1).
'''

import unittest
from pprint import pprint
import pdb

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.input_stack=[]
        self.output_stack=[]

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.input_stack.append(x)

    # @return nothing
    def pop(self):
        if self.output_stack==[]:
            while self.input_stack!=[]:
                self.output_stack.append(self.input_stack.pop())
        if self.output_stack!=[]:
            self.output_stack.pop()

    # @return an integer
    def peek(self):
        if self.output_stack==[]:
            while self.input_stack!=[]:
                self.output_stack.append(self.input_stack.pop())
        if self.output_stack!=[]:
            return self.output_stack[-1]

    # @return an boolean
    def empty(self):
        if self.input_stack==[] and self.output_stack==[]:
            return True
        else:
            return False

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        # self.a=Solution()
        self.b=Queue()

    def testLeet(self):
        self.b.push(2)
        self.assertEqual(self.b.peek(), 2)
        self.b.push(3)
        self.assertEqual(self.b.peek(), 2)
        self.b.pop()
        self.assertEqual(self.b.peek(), 3)


if __name__ == '__main__':
    unittest.main()