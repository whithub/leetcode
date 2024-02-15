"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        level_values = []
        queue = []
        result = []

        queue.append(root)
        
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                level_values.append(node.val)
                if node.children:
                    for child_node in node.children:
                        queue.append(child_node)
                        
            result.append(level_values)
            level_values = []

        return result
        