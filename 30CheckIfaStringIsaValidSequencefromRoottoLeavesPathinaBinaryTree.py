'''Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 
We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.

Example 1:
             0
           /    \
         1       0
        /  \    /
      0     1   0
       \   / \
        1 0   0
Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
Output: true
Explanation: 
The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure). 
Other valid sequences are: 
0 -> 1 -> 1 -> 0 
0 -> 0 -> 0

Example 2:
             0
           /    \
         1       0
        /  \    /
      0     1   0
       \   / \
        1 0   0
Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
Output: false 
Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.

Example 3:
             0
           /    \
         1       0
        /  \    /
      0     1   0
       \   / \
        1 0   0
Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
Output: false
Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.

Constraints:
1 <= arr.length <= 5000
0 <= arr[i] <= 9
Each node’s value is between [0 – 9].'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        n = len(arr)
        def isLeaf(node):
            return node.left is None and node.right is None
        def visit(node, index):
            if index == n-1:
                return node.val == arr[index] and isLeaf(node)
            if node == None:
                return False
            if node.val == arr[index]:
                return visit(node.left, index+1) or visit(node.right, index+1)
            return False
        return visit(root, 0)


    
