import random

class RandomizedSet:

    def __init__(self):
        self.set = set()
        

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        else:
            self.set.add(val)
            return True
        # insert value into set if not already present
        # return True if not already present, otherwise, return False
        

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False
        # removes value from set if present
        # return True if item was present, otherwise, return False
        

    def getRandom(self) -> int:
        # Returns a random element from the current set of elements
        # Each element must have the same probability of being returned.... 
        return random.choice(list(self.set))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()