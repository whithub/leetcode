from collections import OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # ------------------------> { key: [value, current_count] }
        self.cached_counts = OrderedDict() # -----> { current_count: [key, key2, ...] }

    def get(self, key: int) -> int:
        if key in self.cache:
            value, old_count = self.cache[key]
            self.cache[key] = [value, old_count + 1]
            self.update_cached_counts(key, old_count)

            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        starter_use_count = 0

        if key in self.cache:
            old_value, old_count = self.cache[key]
            self.cache[key] = [value, old_count + 1]
            self.update_cached_counts(key, old_count)
            return

        if len(self.cache) == self.capacity:
            min_count = min(self.cached_counts.keys())
            lfu_items = self.cached_counts[min_count]
            lfu_key = lfu_items.pop(0)
            self.cache.pop(lfu_key)

        self.cache[key] = [value, starter_use_count + 1]   # {1: [1,1], 2: [2,1]} ---> { key: [value, current_count] }
        self.update_cached_counts(key, starter_use_count)  # {1: [1,2]} -------> { current_count: [key, key2, ...] }

    def update_cached_counts(self, key: int, count: int):
        if count in self.cached_counts:
            self.cached_counts[count].remove(key)
            if not self.cached_counts[count]:
                self.cached_counts.pop(count)

        new_count = count + 1
        if new_count not in self.cached_counts:
            self.cached_counts[new_count] = []

        self.cached_counts[new_count].append(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# [[3],[2,2],[1,1],[1,6],[2],[1],[2],[3,3],[4,4],[3],[2],[1],[4]]
# [3] ----------------------------------------> return null
#   lfu = LFUCache(3)
#   cache = {}
#   cached_counts {}
# 
# [2,2]  -------------------------------------> return null
#   cache = {2: [2,1]}
#   cached_counts {1: [2]}
# 
# [1,1]  -------------------------------------> return null
#   cache = {2: [2,1], 1: [1,1]}
#   cached_counts {1: [2,1]}
#
# [1,6]  -------------------------------------> return null -- important that we hit if key in self.cach: conditional before if len(self.cache) == self.capacity:
#   cache = {2: [2,1], 1: [6,2]}
#   cached_counts {1: [2], 2: [1]}
#  
# [2] ----------------------------------------> return val of 2
#   cache = {2: [2,2], 1: [1,1]}
#   cached_counts {2: [1,2]}
# 
# [1] ----------------------------------------> return val of 1
#   cache = {2: [2,2], 1: [1,2]}
#   cached_counts {2: [2], 3: [1]}
# 
# [2] ----------------------------------------> return val of 2
#   cache = {2: [2,3], 1: [1,1]}
#   cached_counts {3: [1,2]}
# 
# [3,3]
#   we've hit capacity; first reduce cache by:
#     - finding min_count in cached_counts (i.e. 3) --> 3: [1,2]
#     - grab value (a list): --> [1,2]
#     - plucking the first element in this list --> 1
#       (if no further elements remain in this list, remove old_count key from cached_counts...)
#       (i.e cached_count = {3: [2]} ---> still has el: {3: [2]}
#     - we now have our least frequently used key --> 1
#     - now remove that key from the cache: self.cache.pop(1)
#     cache = {2: [2,3], 1: [6,3]} ---------> removal of key `1` leads to: {2: [2,3]}
#     cached_counts = {3: [2]}
#   now update cache & cached_counts with new [3,3] element:
#     cache = {2: [2,3], 3: [3,1]}
#     cached_counts = {3: [2], 1: [3]}
# 
# [4,4]
#   we've hit capacity; first reduce cache by:
#     - finding min_count in cached_counts (i.e. 1) --> 1: [3]
#     - grab value (a list): --> [1,2]
#     - plucking the first element in this list --> 3
#       (if no further elements remain in this list, remove old_count key from cached_counts...)
#       (i.e cached_count = {3: [2], 1: [3]} ---> updates to: {3: [2], 1: []} --> updates to: {3: [2]} )
#     - we now have our least frequently used key --> 3
#     - now remove that key from the cache: self.cache.pop(3)
#     cache = {2: [2,3], 3: [3,1]} ---------> removal leads to: {2: [2,3]}
#     cached_counts {3: [2], 1: [3]} -------> {3: [2]}
#   now update cache & cached_counts with new [4,4] element:
#     cache = {2: [2,3], 4: [4,1]}
#     cached_counts = {3: [2], 1: [4]}
# 
# [3] ----------------------------------------> return val of -1 since 3 is not in cache
#   cache = {2: [2,3], 4: [4,1]} ------ counts aren't effected
#   cached_counts = {3: [2], 1: [4]} -- counts aren't effected
# 
# [2] ----------------------------------------> return val of 2
#   cache = {2: [2,4], 4: [4,1]}
#   cached_counts = {4: [2], 1: [4]}
# 
# [1] ----------------------------------------> return val of -1 since 1 is not in cache
#   cache = {2: [2,4], 4: [4,1]} ------ counts aren't effected
#   cached_counts = {4: [2], 1: [4]} -- counts aren't effected
# 
# [4] ----------------------------------------> return val of 4
#   cache = {2: [2,4], 4: [4,2]}
#   cached_counts = {4: [2], 2: [4]}