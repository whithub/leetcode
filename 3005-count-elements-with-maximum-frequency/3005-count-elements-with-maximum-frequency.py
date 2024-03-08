class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1

        max_freq = max(freq.values())

        total_max_freq = 0
        for i in freq.values():
            if i == max_freq:
                total_max_freq += i

        return total_max_freq

