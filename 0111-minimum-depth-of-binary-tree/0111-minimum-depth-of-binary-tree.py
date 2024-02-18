# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive:
        # if not root:
        #     return 0

        # # below 2 if conditionals were added in for trees completely skewed to one side:  ie.   1
        # if not root.left:                                                                  #     \
        #     return self.minDepth(root.right) + 1                                           #      2
        # if not root.right:                                                                 #       \
        #     return self.minDepth(root.left) + 1                                            #        3
        # # ^^ otherwise, with no L nodes, minDepth would be 1 L-side depth is 0             #         \
        # #                                                                                  #          4
        
        # return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        

        # Iterative:
        if not root:
            return 0

        min_depth = float('inf')
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()

            # Update minimum depth if a leaf node is reached
            if not node.left and not node.right:
                min_depth = min(min_depth, depth)

            # This was key: Push children to the stack ONLY if minimum depth hasn't been found yet
            if depth < min_depth:
                if node.left:
                    stack.append((node.left, depth + 1))
                if node.right:
                    stack.append((node.right, depth + 1))

        return min_depth
