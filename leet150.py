# encoding: utf8
'''
Evaluate Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

逆波兰表达式。遇到数字压栈，遇到符号则弹出栈顶元素进行运算，然后将结果入栈。
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        s=[]
        for x in tokens:
            if x=='+':
                x1=s.pop()
                x2=s.pop()
                s.append(x1+x2)
            elif x=='-':
                x1=s.pop()
                x2=s.pop()
                s.append(x2-x1)
            elif x=='*':
                x1=s.pop()
                x2=s.pop()
                s.append(x1*x2)
            elif x=='/':
                x1=s.pop()
                x2=s.pop()
                x=abs(x2)/abs(x1)
                if x1*x2<0:
                    x=-x
                # 6/-132应该等于1，但是python的除法算出等于-1，所以。。特殊处理一下
                s.append(x)
            else:
                s.append(int(x))
            print s
        ans=s.pop()
        return ans

class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        # self.assertEqual(self.a.evalRPN(["2", "1", "+", "3", "*"]),9)
        # self.assertEqual(self.a.evalRPN(["4", "13", "5", "/", "+"]),6)
        self.assertEqual(self.a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]),22)

if __name__ == '__main__':
    unittest.main()