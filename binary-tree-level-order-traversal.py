# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = defaultdict(list)


        def traverse(root,depth):
            
            if not root:
                return 
            
            ans[depth].append(root.val)

            traverse(root.left,depth+1)
            traverse(root.right,depth+1)

        traverse(root,0)

        arr = []
        n = len(ans)
        for i in range(n):
            arr.append(ans[i])
        
        return arr