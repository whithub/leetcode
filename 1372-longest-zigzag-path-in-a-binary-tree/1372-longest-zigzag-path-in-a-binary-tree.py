# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # declare longest_path var
        # declare steps var
        # once leaf node hit, will take max btwn `steps` count is > `longest_path`
        # rules:
        #   1. if direction is L:
        #       a. pass in left_child
        #       b. set direction = Right
        #       c. increment `steps`
        #       d. ALSO NEED TO CHECK OTHER NODE: so also pass in right_child, set direction to L, set steps = 1
        #   2. if direction is R:
        #       a. pass in right_child
        #       b. set direction = Left
        #       c. increment `steps`
        #       d. ALSO NEED TO CHECK OTHER NODE: so also pass in left_child, set direction to R, set steps = 1

        self.longest_path = 0

        self.dfs(root, True, 0)
        self.dfs(root, False, 0)

        return self.longest_path

    def dfs(self, node, go_left, steps):
        if node:
            self.longest_path = max(self.longest_path, steps)

            if go_left:
                self.dfs(node.left, False, steps + 1)
                self.dfs(node.right, True, 1)
            else:
                self.dfs(node.right, True, steps + 1)
                self.dfs(node.left, False, 1)
