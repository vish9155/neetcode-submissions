# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def finds(node,maxVal):
            
            nonlocal count

            if node is None:
                return 

            if node.val>=maxVal:
                count+=1
            
            maxVal=max(maxVal,node.val)

            finds(node.left,maxVal)
            finds(node.right,maxVal)
        finds(root,float('-inf'))
        return count       
                    
