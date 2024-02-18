# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_tree = root.left
        right_tree = root.right

        if not left_tree and not right_tree:
            return True

        # queue = [left_tree, right_tree]
        # while queue:
        #     left_node = queue.pop(0)
        #     right_node = queue.pop(0)

        #     if left_node and right_node:
        #         if left_node.val == right_node.val:
        #             # appending nodes, outside-->in
        #             queue.append(left_node.left)
        #             queue.append(right_node.right)
        #             queue.append(left_node.right)
        #             queue.append(right_node.left)
        #         else:
        #             return False
            
        #     if (not left_node and right_node) or (left_node and not right_node):
        #         return False
                
        # return True


        # Yuck solution, but just playing around:
        queue = [left_tree, right_tree]
        result = True

        while queue and result:
            for i in range(0, int(len(queue)/2)): # cutting the iteration loop in half since we pluck 2 elements each time...
                left_node = queue.pop(0)          # AND we only append if nodes exist and if vals match..
                right_node = queue.pop(0)

                if left_node and right_node:
                    if left_node.val == right_node.val:
                        # appending nodes, outside-->in
                        queue.append(left_node.left)
                        queue.append(right_node.right)
                        queue.append(left_node.right)
                        queue.append(right_node.left)
                    else:
                        result = False
                        break
                if (not left_node and right_node) or (left_node and not right_node):
                    result = False
                    break
        return result