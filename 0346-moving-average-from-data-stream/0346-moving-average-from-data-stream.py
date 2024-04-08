class MovingAverage:

    def __init__(self, size: int):
        # size --> sliding windo size
        self.size = size
        self.numbers = []

    def next(self, val: int) -> float:
        # if self.numbers has a length == self.size, pop 0 index el, then append new val
        #   then calc average
        #   then return result

        # if self.numbers has a length < self size, append new el
        #   then calc average
        #   then return result

        if len(self.numbers) == self.size:
            self.numbers.pop(0)

        self.numbers.append(val)

        average = sum(self.numbers) / len(self.numbers)
        return average



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)