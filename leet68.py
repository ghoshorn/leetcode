# encoding: utf8
'''
Text Justification
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.

注意：
不可以if len(x)==maxWidth的时候直接ans.append(x)，否则会乱序；
一行中，不一定只有第一次出现的空格可能是多个，因为要求尽可能的平均（isFirst->extraSpace）；
'''

import unittest
from pprint import pprint
import pdb

class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        ans =[]
        tmp =[]       # this line's words
        l   =maxWidth # this line's left space
        n   =0        # this line's words number
        for x in words:
            # if len(x)==maxWidth:
            #     ans.append(x)
            #     continue
            if len(x)<=l-n:
                tmp.append(x)
                l=l-len(x)
                n+=1
            else:
                if n==1:
                    line=tmp[0]+' '*(maxWidth-len(tmp[0]))
                else:
                    extraSpace=l-l/(n-1)*(n-1)
                    # isFirst=True
                    line=""
                    for xx in tmp:
                        # if isFirst:
                        if extraSpace>0:
                            # isFirst=False
                            extraSpace-=1
                            line=line+xx+' '*(l/(n-1)+1)
                        else:
                            line=line+xx+' '*(l/(n-1))
                    line=line.strip()
                ans.append(line)
                tmp=[]
                tmp.append(x)
                l=maxWidth-len(x)
                n=1
        if tmp!=[]:
            line=tmp[0]
            for i in range(1,n):
                line=line+' '+tmp[i]
            if len(line)<maxWidth:
                line=line+' '*(maxWidth-len(line))
            ans.append(line)
        print(ans)
        return ans


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        self.assertEqual(
            self.a.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16),\
            ["This    is    an", "example  of text", "justification.  "])
        self.assertEqual(
            self.a.fullJustify(["Listen","to","many,","speak","to","a","few."], 6),\
            ['Listen', 'to    ', 'many, ', 'speak ', 'to   a', 'few.  '])
        self.assertEqual(
            self.a.fullJustify(["What","must","be","shall","be."], 5),\
            ["What ","must ","be   ","shall","be.  "])
        self.assertEqual(
            self.a.fullJustify(["What","must","be","shall","be."], 12),\
            ["What must be","shall be.   "])
        self.assertEqual(
            self.a.fullJustify(["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."], 30),\
            ["Don't  go  around  saying  the","world  owes  you a living; the","world owes you nothing; it was","here first.                   "])

if __name__ == '__main__':
    unittest.main()
