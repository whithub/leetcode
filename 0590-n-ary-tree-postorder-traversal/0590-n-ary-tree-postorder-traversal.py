"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # L --> R --> root
        # goal: recursive?

        if not root:
            return []

        results = [root.val]

        if root.children:
            for child in root.children:
                results += self.postorder(child)
            
            root_node_val = results.pop(0) # to follow L --> R --> root, move root node value after children
            results.append(root_node_val)

        return results