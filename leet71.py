# encoding: utf8
'''
Simplify Path
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

栈。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        paths=path.split('/')
        now=[]
        for x in paths:
            if x=='.':
                continue
            elif x=='..':
                if len(now)>0:
                    now.pop()
            elif x!='':
                now.append(x)
        ans='/'+'/'.join(now)
        # print now
        # print ans
        return ans


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.simplifyPath("/home/"),"/home")
        self.assertEqual(self.a.simplifyPath("/a/./b/../../c/"),"/c")
        self.assertEqual(self.a.simplifyPath("/../"),"/")
        self.assertEqual(self.a.simplifyPath("/home//foo/"),"/home/foo")


if __name__ == '__main__':
    unittest.main()
