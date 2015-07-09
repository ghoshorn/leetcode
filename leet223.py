# encoding: utf8
'''
Rectangle Area 
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
Assume that the total area is never beyond the maximum possible value of int.
好无聊的题。。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        if E>=C or F>=D or A>=G or B>=H:
            return (D-B)*(C-A)+(H-F)*(G-E)
        x1=max(A,E)
        y1=max(B,F)
        x2=min(C,G)
        y2=min(D,H)
        return (D-B)*(C-A)+(H-F)*(G-E)-(y2-y1)*(x2-x1)

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.computeArea(-3,0,3,4,0,-1,9,2), 45)
        self.assertEqual(self.a.computeArea(0, 0, 0, 0, -1, -1, 1, 1), 4)

if __name__ == '__main__':
    unittest.main()