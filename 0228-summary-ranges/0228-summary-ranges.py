class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(i) for i in nums]
            # return [str(nums[-1])]
    
        ranges = []
        x = 0
        y = len(nums) - 1

        while x < y:
            if (nums[y] - nums[x]) == (y - x):
                curr_range = f"{nums[x]}->{nums[y]}"
                ranges.append(curr_range)
                x = y + 1
                y = len(nums) - 1

            elif y - x == 1:
                curr_range = f"{nums[x]}"
                ranges.append(curr_range)
                x += 1
                y = len(nums) - 1

            else:
                y -= 1
        
        if x == y:
            curr_range = f"{nums[x]}"
            ranges.append(curr_range)
        
        return ranges