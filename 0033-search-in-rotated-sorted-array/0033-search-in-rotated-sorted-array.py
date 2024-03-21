class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if target == nums[low]:  return low
            if target == nums[mid]:  return mid
            if target == nums[high]: return high

            if nums[low] < nums[mid]:
                if nums[low] < target < nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                if nums[mid] < target < nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1

        # Option #2:
        # if target not in nums:
        #         return -1

        # return nums.index(target)