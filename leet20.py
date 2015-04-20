import unittest

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack=[]
        left=('(','{','[')
        right=(')','}',']')
        dic={
        "(":")",
        "[":"]",
        "{":"}",
        }
        for x in s:
            if x in left:
                stack.append(x)
            elif x in right:
                tmp=stack.pop()
                if dic[tmp]!=x:
                    return False
            else:
                return False
        if stack==[]:
            return True
        return False


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()
    def testLeet(self):
        self.assertEqual(self.a.isValid("()[]{}"),True)
        self.assertEqual(self.a.isValid("(]"),False)
        self.assertEqual(self.a.isValid("([)]"),False)

if __name__ == '__main__':
    unittest.main()
