# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        queue = [p,q]

        # Option #2:
        while queue:
            for i in range(len(queue)):
                node1 = queue.pop(0)
                node2 = queue.pop(0)
                if not node1 and not node2:
                    break
                elif not node1 or not node2:
                    return False
                elif node1.val != node2.val:
                    return False

                queue.append(node1.left)
                queue.append(node2.left)
                queue.append(node1.right)
                queue.append(node2.right)
        
        return True

        # Option #1:
        # p_queue = [p]
        # p_traverse = []

        # while p_queue:
        #     for i in range(len(p_queue)):
        #         node = p_queue.pop(0)
        #         if not node:
        #             p_traverse.append(node)
        #             break

        #         p_traverse.append(node.val)
        #         if not node.left and not node.right:
        #             break

        #         p_queue.append(node.left)
        #         p_queue.append(node.right)

        # q_queue = [q]
        # q_traverse = []

        # while q_queue:
        #     for i in range(len(q_queue)):
        #         node = q_queue.pop(0)
        #         if not node:
        #             q_traverse.append(node)
        #             break

        #         q_traverse.append(node.val)
        #         if not node.left and not node.right:
        #             break

        #         q_queue.append(node.left)
        #         q_queue.append(node.right)

        # return p_traverse == q_traverse