# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        priority_queue = [(root, 0)] # (node, column_number)
        values_per_column = {}
        result = []

        while priority_queue:
            node, column_number = priority_queue.pop(0)

            if node:
                if column_number in values_per_column:
                    values_per_column[column_number] = values_per_column[column_number] + [node.val]
                    # {-1: [9], 0: [3, 15], 1: [20], 2: [7]}
                else:
                    values_per_column[column_number] = [node.val]

                priority_queue.append((node.left, column_number - 1))
                priority_queue.append((node.right, column_number + 1))


        vertical_order_sort = sorted(values_per_column.items()) # [(-1, [9]), (0, [3, 15]), (1, [20])]
        for pair in vertical_order_sort:
            result.append(pair[1])

        # OR sort by:
        # sorted_columns = sorted(values_per_column.keys()) # -------------------------> [-1, 0, 1]
        # vertical_order_sort = {i: values_per_column[i] for i in sorted_columns} # ---> {-1: [9], 0: [3, 15], 1: [20]}
        # result = list(vertical_order_sort.values()) # -------------------------------> [[9], [3, 15], [20]]
        return result

        
        