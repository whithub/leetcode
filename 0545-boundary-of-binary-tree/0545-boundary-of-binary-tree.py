# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        root_boundary = [root.val]
        left_boundary = self.left_dfs(root.left)
        leaves = self.find_leaves(root.left) + self.find_leaves(root.right)
        right_boundary = self.right_dfs(root.right)

        return root_boundary + left_boundary + leaves + right_boundary


    def find_leaves(self, node):
        if not node:
            return []

        left_node = node.left
        right_node = node.right

        if not left_node and not right_node:
            return [node.val]
        else:
            return self.find_leaves(left_node) + self.find_leaves(right_node)

    def left_dfs(self, node):
        if not node:
            return []

        left_node = node.left
        right_node = node.right
        
        if not left_node and not right_node:
            return []
        else:
            if left_node:
                return [node.val] + self.left_dfs(node.left)
            else:
                return [node.val] + self.left_dfs(node.right)

    def right_dfs(self, node):
        if not node:
            return []

        left_node = node.left
        right_node = node.right
        
        if not left_node and not right_node:
            return []
        else:
            if right_node:
                return self.right_dfs(node.right) + [node.val]
            else:
                return self.right_dfs(node.left) + [node.val]

