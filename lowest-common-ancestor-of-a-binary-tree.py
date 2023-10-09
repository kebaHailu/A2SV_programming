# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        ans = TreeNode()
        def dfs(root):
            nonlocal ans
            if not root:
                return False 
            
            if root == p or root == q:
                if dfs(root.left) or dfs(root.right):
                    ans = root
                return True 
            left = dfs(root.left)
            right = dfs(root.right)
            if left and right:
                ans = root 
            
            return left or right
        
        dfs(root)
        return ans