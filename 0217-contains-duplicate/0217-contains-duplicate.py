class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # uniq_nums = set(nums)
        # return len(uniq_nums) != len(nums)

        # If I can't use existing functions above:
        num_counts = {}

        for num in nums:
            if num in num_counts.keys():
                return True
            else:
                num_counts[num] = 1

        return False
