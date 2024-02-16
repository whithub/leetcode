# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # root --> L --> R
        # BFS: ... behaves like a queue
        # iterate over "current queue" which includes nodes for current level
        # add children to queue
        # collect values for all nodes at level; group/keep them together
        # at the end of each level iteration, at level_values to a final result list... 
        # return results list when queue is empty

        queue = [root]
        level_values = []
        result = []

        while queue:
            for i in range(len(queue)): # current queue = []
                node = queue.pop(0) # node = 
                if node:
                    level_values.append(node.val) # []
                    queue.append(node.left)
                    queue.append(node.right) # queue = []
            
            if level_values:
                result.append(level_values) # [[3], [9,20], [15, 7]]
            level_values = []

        return result
