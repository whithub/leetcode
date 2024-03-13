class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest_count = 0

        nums.sort(reverse=True)

        return nums[k-1]

