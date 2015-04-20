import unittest

class Solution:
    def dfs(self,s,si):
        dic={
        "0":" ",
        "1":"",
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
        }
        if si==self.l:
            self.ans.append(s)
            return
        string=dic[self.num[si]]
        for x in string:
            self.dfs(s+x,si+1)

    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        self.num=str(digits)
        self.l=len(self.num)
        if self.l==0:
            return []
        self.ans=[]
        self.dfs("",0)
        return self.ans


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()
    def testLeet(self):
        self.assertEqual(self.a.letterCombinations(""),[])
        self.assertEqual(self.a.letterCombinations(23),["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

if __name__ == '__main__':
    unittest.main()