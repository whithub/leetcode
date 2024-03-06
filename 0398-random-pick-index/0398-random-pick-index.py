import random

class Solution:

    def __init__(self, nums: List[int]):
        self.target_indices = {}
        for idx, num in enumerate(nums):
            if num in self.target_indices.keys():
                self.target_indices[num].append(idx)
            else:
                self.target_indices[num] = [idx]
        
    def pick(self, target: int) -> int:
        avail_indices = self.target_indices[target]
        return random.choice(avail_indices)


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)