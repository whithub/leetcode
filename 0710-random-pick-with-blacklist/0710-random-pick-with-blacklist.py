import random
class Solution:
    # n = 7
    # blacklist = [2,3,5]

    def __init__(self, n: int, blacklist: List[int]):
        self.whitelist_max_idx_to_care_about = n - 1 - len(blacklist) # 7 - 1- 3 => 3
        self.blacklist_num_mapping = {}
        j = self.whitelist_max_idx_to_care_about + 1 # ---------------> 4

        for num in blacklist: #                                         num = 2                 | num = 3                   | num = 5
            if num <= self.whitelist_max_idx_to_care_about: # --------> 2 < 4                   | 3 < 4                     | 5 < 4 --> !< so exit
                while j < n and j in blacklist: # --------------------> 4 < 7 && 4 in [2,3,5]?  | 5 < 7 && 5 in [2,3,5]?
                    j += 1 # ----------------------------------------->                         | j = 6
                self.blacklist_num_mapping[num] = j # ----------------> {2: 4}                  | {2: 4, 3: 6}
                j+=1 # -----------------------------------------------> j = 5                   | j = 7
            
    def pick(self):
        # whitelist_max_idx_to_care_about = 3
        # blacklist_num_mapping = {2: 4, 3: 6}
        target = random.randint(0, self.whitelist_max_idx_to_care_about) # 0, 1, 2, 3

        return self.blacklist_num_mapping[target] if target in self.blacklist_num_mapping else target
        # target = 0    -------------------->   target NOT in self.blacklist_num_mapping => 0
        # target = 1    -------------------->   target NOT in self.blacklist_num_mapping => 1
        # target = 2    -------------------->   target in self.blacklist_num_mapping => blacklist_num_mapping[2] => 4
        # target = 3    -------------------->   target in self.blacklist_num_mapping => blacklist_num_mapping[3] => 6
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()