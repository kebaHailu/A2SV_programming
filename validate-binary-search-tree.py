# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float("-inf")

        def inorder(rot):
            nonlocal prev 

            if rot is None:
                return True
            
            if not (inorder(rot.left) and prev < rot.val):
                return False 
            prev = rot.val
            return inorder(rot.right)
        
        return inorder(root)