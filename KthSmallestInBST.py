# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.nums = [float('inf')]
        self.ans = float('inf')
            
        def dfs(node):
            if node:
                dfs(node.left)
                if self.nums[-1] != node.val:
                    self.nums.append(node.val)
                if len(self.nums) == k+1:
                    self.ans = node.val
                dfs(node.right)
           
        dfs(root)
        if self.ans < float('inf'):
            return self.ans
        else:
            return -1
        
        
