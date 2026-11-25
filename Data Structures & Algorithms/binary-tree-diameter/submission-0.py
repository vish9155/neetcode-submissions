# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):

        if root is None:
            return 0

        def height(node):

            if node is None:
                return 0

            lh = height(node.left)
            rh = height(node.right)

            return max(lh, rh) + 1

        diml = self.diameterOfBinaryTree(root.left)

        dimr = self.diameterOfBinaryTree(root.right)

        currdiam = height(root.left) + height(root.right)

        return max(currdiam, diml, dimr)