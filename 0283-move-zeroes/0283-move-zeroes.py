class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        x = 0
        while x < len(nums) - zero_count:
            if nums[x] == 0:
                nums.append(0)
                nums.pop(x)
            else:
                x += 1
