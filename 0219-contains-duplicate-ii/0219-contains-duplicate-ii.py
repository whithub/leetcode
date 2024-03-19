class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                diff = abs(hashmap[nums[i]] - i)
                if diff <= k:
                    return True

            hashmap[nums[i]] = i

        return False
