# encoding: utf8
'''
Linked List Cycle 
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
使用两个指针p1和p2，分别指向head和head.next；
最后每次p1后移1，p2每次后移2：如果期间p1==p2，则存在环；如果最后p2==Null，则不存在环。
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
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head==None:
            return False
        p1=head
        p2=head.next
        while p1 and p2 and p2.next:
            p1=p1.next
            p2=p2.next.next
            if p1==p2:
                return True
        return False
        

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.wordBreak('leetcode',['leet','code']),True)

if __name__ == '__main__':
    unittest.main()