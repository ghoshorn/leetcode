# encoding: utf8
'''
Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

直接递归Memory Limit Exceeded (⊙o⊙)
'''

import unittest
from pprint import pprint
import pdb

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if len(inorder)==0:
            return None
        root=TreeNode(preorder[0])
        pos=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:pos+1],inorder[:pos])
        root.right=self.buildTree(preorder[pos+1:],inorder[pos+1:])
        return root


class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if len(inorder)==0:
            return None
        self.preorder=preorder
        self.inorder=inorder
        self.l=len(preorder)
        ans=self.go([0,len(preorder)-1],[0,len(inorder)-1])
        # print ans.val,ans.left.val,ans.right.val
        return ans

    def go(self, preorder, inorder):
        p1,p2=preorder
        i1,i2=inorder
        if not (0<=p1<=p2<self.l and 0<=i1<=i2<self.l):
        # if p1>=self.l or p2>=self.l or i1>=self.l or i2>=self.l or i1<0 or i2<0 or p1<0 or p2<0:
            return None
        root=TreeNode(self.preorder[p1])
        print preorder,inorder
        print root.val
        if p1==p2 or i1==i2:
            return root
        cnt=0
        for pos in range(i1,i2+1):
            if self.inorder[pos]==root.val:
                break
            cnt+=1
        if cnt>0:
            root.left=self.go([p1+1,p1+cnt],[i1,pos-1])
        # if pos<p2:
        # if pos<i2:
            root.right=self.go([p1+1+cnt,p1+cnt*2],[pos+1,i2])
        return root


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        # a=TreeNode(1)
        # a.left=TreeNode(2)
        # a.right=TreeNode(3)
        r=self.a.buildTree([1,2,3],[2,1,3])
        print r.val,r.left.val,r.right.val

        r=self.a.buildTree([1,2,4,5,3,6,7],[4,2,5,1,6,3,7])
        print r.val
        print r.left.val,r.right.val
        print r.left.left.val, r.left.right.val,
        print r.right.left.val, r.right.right.val

        r=self.a.buildTree([1,2],[2,1])
        print r.val,r.left.val

        r=self.a.buildTree([1,2],[1,2])
        print r.val,r.right.val

        r=self.a.buildTree([4,3,1,2,5,6], [1,2,3,4,5,6])
        print r.val
        print r.left.val,r.right.val
        print r.left.left.val, r.left.left.val,
        print r.right.right.val

        # a=TreeNode(1)
        # a.left=TreeNode(2)
        # a.right=TreeNode(3)
        # self.assertEqual(self.a.buildTree(a),2)


if __name__ == '__main__':
    unittest.main()