# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        


        def toarr(root):
            if not root:
                return []

            return toarr(root.left) + [root.val] + toarr(root.right)
        
        count = Counter(toarr(root))

        max_frq = max(count.values())
        nums = []
        for k , v in count.items():
            if v == max_frq:
                nums.append(k)
      
        return nums