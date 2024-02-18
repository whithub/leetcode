# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # split sorted list:
        # middle_idx value is going to = root/parent node:
        # left half will build left branches
        # right half will build right branches
        # recursive: find middle value of left half... becomes that subtree's parent node...

        if not nums:
            return None

        # nums = [-10,-3,0,5,9]
        middle_idx = len(nums) // 2        # 2

        middle_value = nums[middle_idx]    # 0
        left_half = nums[:middle_idx]      # [-10, -3]
        right_half = nums[middle_idx + 1:] # [5, 9]

        return TreeNode(middle_value, self.sortedArrayToBST(left_half), self.sortedArrayToBST(right_half))
        
