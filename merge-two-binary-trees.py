# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def merger(rot1,rot2):
         
            if not rot1 and not rot2:
                return None

            if not rot1:
                return rot2

            if not rot2:
                return rot1
               
            
            
            mergedTree = TreeNode()
            mergedTree.val = rot1.val + rot2.val
            mergedTree.left = merger(rot1.left,rot2.left)
            mergedTree.right = merger(rot1.right,rot2.right)
            return mergedTree


        return merger(root1,root2)