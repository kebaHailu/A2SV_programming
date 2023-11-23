# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        

        def traverse(root):
            if not root:
                return [] 
            
            return [root.val]+traverse(root.left)+traverse(root.right)
        
        arr = traverse(root)
        arr.sort()

        def deep(idx):
            if idx ==  len(arr):
                return 
            node = TreeNode(arr[idx])
            node.left = None 
            node.right = deep(idx+1) 
            return node

        return deep(0)
