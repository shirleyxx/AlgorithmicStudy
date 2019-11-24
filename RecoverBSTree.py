# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.ordered = []
        self.swap = []
        
        def inorder(root):
            if root.left:
                inorder(root.left)
                
            if self.ordered and self.ordered[-1].val>root.val: 
                if self.swap:
                    self.swap[0].val, root.val = root.val, self.swap[0].val
                    self.swap = None
                    return
                else:
                    self.swap = [self.ordered[-1], root]
                
            self.ordered.append(root)
            
            if root.right:
                inorder(root.right)
            return 
        
        inorder(root)
        if self.swap:
            self.swap[0].val, self.swap[1].val = self.swap[1].val, self.swap[0].val
        
        
            
                
        