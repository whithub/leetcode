# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # Option #1 -- Iterative:
        if not root:
            return False

        stack = [(root, 0)]

        while stack:
            node, running_total = stack.pop()

            if node:
                running_total += node.val

                left_node = node.left
                right_node = node.right

                if left_node:
                    stack.append((left_node, running_total)) 
                if right_node:
                    stack.append((right_node, running_total))

                if not left_node and not right_node:
                    if running_total == targetSum:
                        return True
        return False
    
        # Option #2 -- Recursive:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)