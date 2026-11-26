# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result=float('-inf')
        def dfs(node):
            nonlocal result
            if node is None:
                return 0
            left=max(0,dfs(node.left))
            right=max(0,dfs(node.right))

            pathSum=node.val+left+right

            result=max(result,pathSum)    
            
            return node.val+max(left,right)
        dfs(root)
        return result    