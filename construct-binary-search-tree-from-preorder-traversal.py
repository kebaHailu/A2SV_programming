# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])


        def helper(root,val):
            if root.val > val:
                if root.left:
                    helper(root.left,val)
                else:
                    root.left = TreeNode(val)
                    return 

            if root.val < val:
                if root.right:
                    helper(root.right,val)
                else:
                    root.right = TreeNode(val)
                    return 
            
        for val in preorder[1:]:
            helper(root,val)

        return root