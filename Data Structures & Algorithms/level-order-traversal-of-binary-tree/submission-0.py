# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root):

        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:

            size = len(queue)
            level = []

            for i in range(size):

                e = queue.popleft()

                level.append(e.val)

                if e.left is not None:
                    queue.append(e.left)

                if e.right is not None:
                    queue.append(e.right)

            result.append(level)

        return result         