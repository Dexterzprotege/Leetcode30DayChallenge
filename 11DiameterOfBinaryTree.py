'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    diameter=0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.find_height(root)
        return self.diameter
    
    def find_height(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        l_height=self.find_height(root.left)
        r_height=self.find_height(root.right)
        total=l_height+r_height
        if total>self.diameter:
            self.diameter=total
        return 1+max(l_height,r_height)
        
