# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder: L --> root --> R

        # Option #1 -- recursive
        # if not root:
        #     return []
        # return  self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


        # Option #2 -- iterative
        traverse = []
        node = root
        stack = []

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop() # back to parent_node
                traverse.append(node.val)
                node = node.right
        return traverse
