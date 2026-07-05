# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        Balanced = True
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal Balanced
            if abs(right - left) > 1:
                Balanced = False
            return 1 + max(right, left)
        if not root:
            return True
        
        dfs(root)
        return Balanced
        
        