# encoding: utf8
'''
Compare Version Numbers
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
需要考虑特殊情况，如1和1.1; 1和1.0.
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1=version1.split('.')
        v2=version2.split('.')
        while len(v1)<len(v2):
            v1.append('0')
        while len(v2)<len(v1):
            v2.append('0')
        for x1,x2 in zip(v1,v2):
            ver1=int(x1)
            ver2=int(x2)
            if ver1>ver2:
                return 1
            elif ver1<ver2:
                return -1
        return 0


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.compareVersion('0.1','1.1'), -1)
        self.assertEqual(self.a.compareVersion('1.1','1.1'), 0)
        self.assertEqual(self.a.compareVersion('1.2','1.1'), 1)
        self.assertEqual(self.a.compareVersion("1", "1.1"), -1)
        self.assertEqual(self.a.compareVersion("1", "1.0"), 0)


if __name__ == '__main__':
    unittest.main()