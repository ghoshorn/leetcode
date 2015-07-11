# encoding: utf8
'''
Basic Calculator II
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.

和Basic Calculator相比，多了乘除法，少了括号。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        numstack=[]
        optstack=[]
        tmp=0
        s=s+'.'
        for x in s:
            if x==' ':
                continue
            if '0'<=x<='9':
                tmp=tmp*10+int(x)
            else:
                numstack.append(tmp)
                tmp=0
                while len(optstack)>0 and (optstack[-1]=='*' or optstack[-1]=='/'):
                    if optstack[-1]=='*':
                        n2=numstack.pop()
                        n1=numstack.pop()
                        numstack.append(n1*n2)
                    elif optstack[-1]=='/':
                        n2=numstack.pop()
                        n1=numstack.pop()
                        numstack.append(n1/n2)
                    optstack.pop()
                optstack.append(x)
        optstack.pop()
        # numstack.append(tmp)
        print numstack,optstack
        numstack=numstack[::-1]
        optstack=optstack[::-1]
        while len(optstack)>0:
            n1=numstack.pop()
            n2=numstack.pop()
            opt=optstack.pop()
            if opt=='+':
                numstack.append(n1+n2)
            elif opt=='-':
                numstack.append(n1-n2)
            elif opt=='*':
                numstack.append(n1*n2)
            elif opt=='/':
                numstack.append(n1/n2)
            else:
                print "error!",x
        return numstack.pop()


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(self.a.calculate("3+2*2"), 7)
        self.assertEqual(self.a.calculate(" 3/2 "), 1)
        self.assertEqual(self.a.calculate(" 3+5 / 2 "), 5)
        self.assertEqual(self.a.calculate(" 0 "), 0)
        self.assertEqual(self.a.calculate("1-1+1"), 1)
        self.assertEqual(self.a.calculate("0/1"), 0)

if __name__ == '__main__':
    unittest.main()