# from heapq import * # can't use a heap b/c of the given problem setup which includes "key: int, value: int" .. suggesting a hash/dict
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key) # needed in order to mark item as recently used, otherwise it updates in-place and stays in current position in the dict
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
# LRUCache lRUCache = new LRUCache(2); ----------------------> {}
# lRUCache.put(2, 1); // ------------------------------------> {2: 1}
# lRUCache.put(1, 1); // ------------------------------------> {2: 1, 1: 1}
# lRUCache.put(2, 3); // ------------------------------------> {2: 3, 1: 1} - #1 is most recently used/updated, but it updates in-place.
#                        |                                                     I need to manually move to end/"top" of cache: cache.move_to_end(key) --> {1: 1, 2: 3}
#                        |-----------------------------------> {1: 1, 2: 3}
# lRUCache.put(4, 1); // LRU key was 1, evicts key 1 --------> {2: 3, 4:1} -- evicts by: cache.popitem(last=False)
# lRUCache.get(1);    // returns -1 (not found) -------------> {2: 3, 4:1}
# lRUCache.get(2);    // returns 3 --------------------------> {2: 3, 4:1}
# result = [null,null,null,null,null,-1,3]
