# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Neetcode 150 (Important)

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:
# https://assets.leetcode.com/uploads/2021/02/19/tree.jpg
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 
# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.idx = 0
        def traversal(preorder, inorder, start, end):
            if start>end:
                return
            rootVal = preorder[self.idx]
            i = start
            while True:
                if (inorder[i] == rootVal):
                    break
                i+=1
            self.idx+=1
            root = TreeNode(rootVal)
            root.left = traversal(preorder, inorder, start, i-1)
            root.right = traversal(preorder, inorder, i+1, end)

            return root
        return traversal(preorder, inorder, 0, len(inorder)-1)
        


            