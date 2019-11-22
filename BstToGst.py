# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.total = 0    
        self.dfs(root)
        return root
        
    def dfs(self, node: TreeNode):
        if not node:
            return 0
        self.dfs(node.right)
        self.total += node.val
        node.val = self.total
        self.dfs(node.left)
       
        