# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr = []

        def ans(root,path):
            nonlocal arr
            
            if not root:
                return 
            
            if not root.left and not root.right:
                arr.append('->'.join(map(str,path + [root.val])))
                return

            
            ans(root.left, path + [root.val])
            ans(root.right, path + [root.val])
            

        ans(root, [])
        return arr