class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        ans = []
        curr = []
        self.backtrack(ans, curr, nums)
        return ans
        

    def backtrack(self, ans, curr, nums):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return

        for num in nums:
            if num not in curr:
                curr.append(num)
                self.backtrack(ans, curr, nums)
                curr.pop()
