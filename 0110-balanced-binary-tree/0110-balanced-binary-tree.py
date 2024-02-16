# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # check height of left side to right side... DFS
        # divide tree into left tree and right tree
        # will need to check/compare the height of left side to right side for each sub tree as well...

        if not root:
            return True

        left_tree = root.left
        right_tree = root.right

        left_total_depth = self.depth(root.left)
        right_total_depth = self.depth(root.right)

        return abs(left_total_depth - right_total_depth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        #                                                         ^^ checking each L subtree --- checking each R subtree

    def depth(self, node):
        if not node:
            return 0

        return max(self.depth(node.left), self.depth(node.right)) + 1

