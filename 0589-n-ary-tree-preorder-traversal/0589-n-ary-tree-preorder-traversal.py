"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # root --> L --> R
        if not root:
            return []

        tree = [root.val]

        if root.children:
            for child in root.children:
                tree += self.preorder(child)

        return tree
