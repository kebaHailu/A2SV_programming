# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        leftNode = root.left 
        rightNode = root.right

        def is_it(left,right):
            if (not left and right) or (not right and left):
                return False
            if (left is None) and (right is None):
                return True


            return left.val == right.val and is_it(left.right,right.left) and is_it(right.right,left.left)
        
        return is_it(leftNode,rightNode)