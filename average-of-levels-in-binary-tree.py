# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        

        def bfs(node):
            queue = deque([node])
            average = []

            while queue:
                length = len(queue)
                sum_val = 0
                for i in range(length):
                    cur_node = queue.popleft()
                    if cur_node.left:
                        queue.append(cur_node.left)
                    if cur_node.right:
                        queue.append(cur_node.right)
                    sum_val += cur_node.val 
                average.append(sum_val / length)
            
            return average 
        return bfs(root)