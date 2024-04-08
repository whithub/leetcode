class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0

        for i in range(len(vec.nums)):
            num1 = self.nums[i]
            num2 = vec.nums[i]

            result = num1 * num2
            total += result
        
        return total
            

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# PSEUDO:
# length of nums1 == nums2
# lists will never be empty
# iterate over range(len(nums1)), use i (idx) to grab number in each list, multiple, add result to running total, return total..