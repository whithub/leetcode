import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w # [1,5,8,11]
        self.weights = [i*1 for i in w] # don't really need to do this, but clarifies in my head there's a diff btwn w list and weight
        self.total_sum = 0  #=> ends up being 25
        self.cuml_weights = [] #=> ends up being [1,6,14,25]
        for weight in self.weights:
            self.total_sum += weight
            self.cuml_weights.append(self.total_sum)

    def pickIndex(self) -> int:
        # target = random.randint(0, self.total_sum-1)  # float btwn 0.0-3.99
        #   ^^ if using this: the below line of code can read `>` -----> if target > self.cuml_weights[mid_idx]:
        # or
        target = random.randint(0, self.total_sum-1) # int btwn 0-24
        #   ^^ if using this: the below line of code must read `>=` ---> if target >= self.cuml_weights[mid_idx]:

        # linear... O(n)
        # for idx, weight in enumerate(self.cuml_weights):
        #     if target < weight:
        #         return idx

        # binary search... O(log n)
        low_idx, high_idx = 0, len(self.cuml_weights)-1
        while low_idx < high_idx:
            mid_idx = (low_idx + high_idx) // 2

            if target >= self.cuml_weights[mid_idx]:
                low_idx = mid_idx + 1
            else:
                high_idx = mid_idx

        return low_idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()