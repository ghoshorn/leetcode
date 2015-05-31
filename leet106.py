# encoding: utf8
'''
Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
和leetcode 105 Construct Binary Tree from Preorder and Inorder Traversal几乎一样。
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


class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if len(inorder)==0:
            return None
        self.inorder=inorder
        self.postorder=postorder
        self.l=len(postorder)
        ans=self.go([0,len(inorder)-1], [0,len(postorder)-1])
        # print ans.val,ans.left.val,ans.right.val
        return ans

    def go(self, inorder, postorder):
        i1,i2=inorder
        p1,p2=postorder
        if not (0<=p1<=p2<self.l and 0<=i1<=i2<self.l):
            return None
        root=TreeNode(self.postorder[p2])
        if p1==p2 or i1==i2:
            return root
        cnt=0 # 右子树节点个数
        for pos in range(i2,i1-1,-1):
            if self.inorder[pos]==root.val:
                break
            cnt+=1
        if cnt>0: # 右子树非空
            root.right=self.go([pos+1,i2], [p2-cnt,p2-1])
        # if pos<p2:
        if i2-i1-cnt>0: # 左子树非空
            root.left=self.go([i1,pos-1],[p1,p2-cnt-1])
            # root.right=self.go([p1+cnt+1,p1+cnt*2],[pos+1,i2])
        return root


class testCase(unittest.TestCase):
    def setUp(self):
        pass
        self.a=Solution()

    def testLeet(self):
        # a=TreeNode(1)
        # a.left=TreeNode(2)
        # a.right=TreeNode(3)
        r=self.a.buildTree([2,1,3],[2,3,1])
        print r.val,r.left.val,r.right.val

        r=self.a.buildTree([4,2,5,1,6,3,7],[4,5,2,6,7,3,1])
        print r.val
        print r.left.val,r.right.val
        print r.left.left.val, r.left.right.val,
        print r.right.left.val, r.right.right.val

        r=self.a.buildTree([2,1],[2,1])
        print r.val,r.left.val

        r=self.a.buildTree([1,2],[2,1])
        print r.val,r.right.val

        # a=TreeNode(1)
        # a.left=TreeNode(2)
        # a.right=TreeNode(3)
        # self.assertEqual(self.a.buildTree(a),2)


if __name__ == '__main__':
    unittest.main()