# 12.

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1=[]
        l2=[]
        def trav(root,l):
            if root==None: return 
            l.append(root.val)
            trav(root.left,l)
            trav(root.right,l)
        trav(root1,l1)
        trav(root2,l2)
        print(l1,l2)
        return sorted(l1+l2)