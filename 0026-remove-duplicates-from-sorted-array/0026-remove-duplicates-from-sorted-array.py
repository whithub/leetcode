class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        og_length = len(nums)

        if og_length <= 1:
            return og_length

        a_idx = 0
        b_idx = 1
        a, b = nums[a_idx], nums[b_idx]

        for el in nums:
            if b == None or (b_idx == og_length):
                break
            if a == b:
                nums.pop(b_idx) #Or: nums.remove(b)
                nums.append(None)
                a, b = nums[a_idx], nums[b_idx]
            else:
                a_idx += 1
                b_idx += 1
                if (b_idx == og_length):
                    break
                a, b = nums[a_idx], nums[b_idx]

        uniq_nums_count = og_length - nums.count(None)
        return uniq_nums_count #, nums