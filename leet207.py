# encoding: utf8
'''
Course Schedule
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.

click to show more hints.

Hints:
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.

Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.

Topological sort could also be done via BFS.

使用一个数组记录每个节点的前驱节点；
然后每次去除没有前驱的节点，并把该节点的前驱节点数减一；
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        f=[0 for i in range(numCourses)]
        over=[False for i in range(numCourses)]
        for x in prerequisites:
            f[x[1]]+=1
        while over.count(True)!=numCourses:
            changed=False
            for i in range(numCourses):
                if f[i]==0 and over[i]==False:
                    over[i]=True
                    changed=True
                    for x in prerequisites:
                        if x[0]==i:
                            f[x[1]]-=1
            if not changed:
                return False
        return True
        

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        # self.assertEqual(self.a.canFinish(2,[[1,0]]), True)
        # self.assertEqual(self.a.canFinish(2,[[1,0],[0,1]]), False)
        self.assertEqual(self.a.canFinish(3, [[1,0],[2,1]]), True)


if __name__ == '__main__':
    unittest.main()