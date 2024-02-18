class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurrence_count = {}

        for num in nums:
            if num in occurrence_count.keys():
                current_count = occurrence_count[num]
            else:
                current_count = 0

            occurrence_count[num] = current_count + 1

        for num, count in occurrence_count.items():
            if (len(nums) / 2) <= count :
                return num