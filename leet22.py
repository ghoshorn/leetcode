import unittest

class Solution:
    def dfs(self,s,left):
        if len(s)==self.num*2:
            self.ans.append(s)
            return
        if left<self.num:
            self.dfs(s+"(",left+1)
        if len(s)-left<left:
            self.dfs(s+")",left)

    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.num=n
        self.ans=[]
        self.dfs("",0)
        return self.ans


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()
    def testLeet(self):
        self.assertEqual(self.a.generateParenthesis(3),["((()))", "(()())", "(())()", "()(())", "()()()"])
        self.assertEqual(self.a.generateParenthesis(0),[""])

if __name__ == '__main__':
    unittest.main()