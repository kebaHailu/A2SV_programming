# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(root,parent):
            if not root:
                return 
            root.parent = parent 
            dfs(root.left,root)
            dfs(root.right,root)
        
        dfs(root,None)
        queue = deque([(target,0)])
        visited = {target}

        while queue:
            node , dist = queue.popleft() 

            if dist == k:
                return [node.val]+[nd.val for nd,ds in queue if ds == k]
            for nb in (node.left,node.right,node.parent):
                if nb and nb not in visited:
                    visited.add(nb)
                    queue.append((nb,dist+1))
        
        return []


        