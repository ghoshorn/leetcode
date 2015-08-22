# encoding: utf8
'''
Sliding Window Maximum
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

滑动窗口内，使用一个deque(double ended queue).
如果新加入的元素比队尾元素大，则弹出队尾所有比新元素小的数
（因为在新元素滑出窗口之前，deque中这些比它小的，肯定不会成为Maximum）
当deque的队首元素滑出窗口，弹出。
注：让数组的下标入队列，方便滑出窗口时弹出。
'''

import unittest
from pprint import pprint
import pdb

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        d=deque()
        l=len(nums)
        ans=[]
        for i in xrange(l):
            while len(d)>0 and nums[d[-1]]<=nums[i]:
                d.pop()
            d.append(i)
            if i>=k-1:
                ans.append(nums[d[0]])
            if d[0]==i-k+1:
                d.popleft()
        return ans

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3), [3,3,5,5,6,7])

if __name__ == '__main__':
    unittest.main()