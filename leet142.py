# encoding: utf8
'''
Linked List Cycle II
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?
接上题Linked List Cycle
使用两个指针p1和p2，分别指向head和head.next；
# !!! p1和p2都指向head!!!
最后每次p1后移1，p2每次后移2：如果期间p1==p2，则存在环；如果最后p2==Null，则不存在环。

存在环之后，怎么判断环的初始位置？
     n6--------n5
     |          |
n1---n2---n3---n4
假设p1,p2在n5相遇；
设n1-n2距离为a，n2-n5距离为b，n5到n2距离为c
p1走了a+b距离；p2走了a+b+c+b
且p2肯定是p1的两倍，所以(a+b)*2=a+b+c+b。所以a=c.

故p1,p2相遇后，再设一个指针p0从head处，p0和p1一起走，相遇点即为环的起始点。

注意：初始p1和p2都指向head!!!
如果p1和p2，分别指向head和head.next，那么在
n1---n2
|    |
+----+
的时候，就会无休止的循环。
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
    # @return a list node
    def detectCycle(self, head):
        if head==None:
            return None
        p1=head
        p2=head
        while p1 and p2 and p2.next:
            p1=p1.next
            p2=p2.next.next
            if p1==p2:
                p0=head
                while p0!=p1:
                    p0=p0.next
                    p1=p1.next
                return p0
        return None
        

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        # self.assertEqual(self.a.wordBreak('leetcode',['leet','code']),True)
        a=ListNode(1)
        a.next=ListNode(2)
        a.next.next=a
        self.a.detectCycle(a)

if __name__ == '__main__':
    unittest.main()