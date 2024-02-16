# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Use a stack to store levels (current depth) while iterating
        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            # Update maximum depth if this level is deeper than seen before
            max_depth = max(max_depth, depth)

            # Push children to the stack with their corresponding depth level
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return max_depth




        max_level = 0
        if not root:
            return max_level

        node = root
        nodes_at_level = []
        queue = [node]

        while queue: # "current" queue consisting of current level nodes => [1]
            for i in range(len(queue)): # --- iterate through current level nodes...
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left) # ...appending child nodes to queue as we iterate over current level nodes ... => [2,3]
                if node.right:
                    queue.append(node.right)
            
            # for loop complete
            #    which means: we're done checking current level nodes...
            #                 Now increase max_level count:
            max_level += 1

            # The "current" queue now consists of any children node from it's parent(s).
            # The process continues...

        return max_level


        # recursion solution:
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

