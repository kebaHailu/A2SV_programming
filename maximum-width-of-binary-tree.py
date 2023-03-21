# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

					nodes = defaultdict(list)

					def helper(root,level,value):
							if not root:
								return 
						
							nodes[level].append(value)
							helper(root.left,level+1,value*2)
							helper(root.right,level+1,value*2+1)
						
					helper(root,0,1)	
					ans = 0

					for interval in nodes.values():
							ans = max(ans,interval[-1]-interval[0]+1)

					return ans