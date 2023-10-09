# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        temp = []

        def dfs(root,temp_val):
            if not root:
                
                return 
            temp_val += root.val
            temp.append(root.val)

            if not root.left and not root.right:
                if temp_val == targetSum:
                    ans.append(temp.copy())
                     
            
            dfs(root.left,temp_val) 
            
            dfs(root.right,temp_val)
            temp.pop()
           
        dfs(root,0)
        return ans