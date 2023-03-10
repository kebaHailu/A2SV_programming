# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = defaultdict(list)

        def traverse(root,depth):
            if not root:
                return 
            
            ans[depth].append(root.val)
            traverse(root.left,depth+1)
            traverse(root.right,depth+1)

        
        traverse(root,0)
        arr = []
        for i in range(len(ans)):
            arr.append(ans[i][-1])
        return arr