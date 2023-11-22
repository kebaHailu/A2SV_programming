# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum_ans = 0

        def dfs(root):
            nonlocal sum_ans
            if not root:
                return 
            
            if low <= root.val <= high:
                sum_ans += root.val 
            
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return sum_ans