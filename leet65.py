# encoding: utf8
'''
Valid Number
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

需要考虑到所有情况：
不是数字：空，小数点多于1个，e/E多于1个，只有e/E，只有-/+/./e/E，-/+/e/E位于结尾，中间不能有空格之类，e/E后面不能跟小数。。。
可以的情况：小数点开头
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        s=s.strip()
        for x in s:
            if x not in "0123456789.+-eE":
                return False
        l=len(s)
        if l==0:
            return False
        if s.count('.')>1:
            return False
        if s.count('e')+s.count('E')>1:
            return False
        if s.count('e')+s.count('E')>0:
            pos=s.find('e')
            if pos==-1:
                pos=s.find('E')
            if s.find('.')>pos:
                return False
            return self.isNumber(s[:pos]) and self.isNumber(s[pos+1:])
        if s.count('-')>1 or s.count('+')>1:
            return False
        onlynum='0123456789'
        containNum=False
        for i in onlynum:
            if s.count(i)>0:
                containNum=True
        if not containNum:
            return False
        num='0123456789.'
        noSingle="eE+-."
        for i in noSingle:
            if i==s:
                return False
            pos=s.find(i)
            if 0<=pos<l-1:
                if s[pos+1] not in num:
                    return False
        noBefor="+-"
        for i in noBefor:
            pos=s.find(i)
            if pos>0:
                return False
        noStartEnd='eE'
        for i in noStartEnd:
            pos=s.find(i)
            if pos<0:
                continue
            if pos==0 or pos==l-1:
                return False
        noEnd='+-'
        for i in noEnd:
            pos=s.find(i)
            if pos<0:
                continue
            if pos==l-1:
                return False
        chars="0123456789-+eE."
        for i in chars:
            s=s.replace(str(i),'')
        # s=s.strip()
        if s=='':
            return True
        else:
            return False


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.isNumber('123'),True)
        self.assertEqual(self.a.isNumber('12e3'),True)
        self.assertEqual(self.a.isNumber('12.3'),True)
        self.assertEqual(self.a.isNumber('12.a3'),False)
        
        self.assertEqual(self.a.isNumber('e'),False)
        self.assertEqual(self.a.isNumber(' '),False)
        self.assertEqual(self.a.isNumber('.'),False)
        self.assertEqual(self.a.isNumber('5'),True)
        self.assertEqual(self.a.isNumber('.5'),True)
        self.assertEqual(self.a.isNumber('. 5'),False)
        self.assertEqual(self.a.isNumber('.e1'),False)
        self.assertEqual(self.a.isNumber('1+2'),False)
        self.assertEqual(self.a.isNumber('+.2'),True)
        self.assertEqual(self.a.isNumber('1e.'),False)
        self.assertEqual(self.a.isNumber(' -.'),False)
        self.assertEqual(self.a.isNumber('-8-'),False)
        self.assertEqual(self.a.isNumber('6e6.5'),False)
        self.assertEqual(self.a.isNumber('96 e5'),False)
        

if __name__ == '__main__':
    unittest.main()
