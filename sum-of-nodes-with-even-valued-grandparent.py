# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0

        def evenSum(grand,parent,root):
            nonlocal total
            if not root:
                return 

            if grand and grand.val%2 == 0:
                
                total += root.val

            evenSum(parent,root,root.left)
            evenSum(parent,root,root.right)

        evenSum(None,None,root)
        return total