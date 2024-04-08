class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # binary search to find timestamps within self.hits that are within the PAST 300 seconds of the given timestamp
        earliest_ts_idx = self.findEarliestValidTimestampIdx(timestamp)
        latest_ts_idx = self.findLatestTimestampIdx(timestamp)

        return (latest_ts_idx - earliest_ts_idx) + 1 # account for 0-indexed

    def findEarliestValidTimestampIdx(self, timestamp: int) -> int:
        low, high = 0, len(self.hits) - 1

        while low <= high:
            mid = (high + low) // 2
            if (timestamp - self.hits[mid]) < 300:
                high = mid - 1
            else:
                low = mid + 1

        return low
    
    def findLatestTimestampIdx(self, timestamp: int) -> int:
        low, high = 0, len(self.hits) - 1

        while low < high:
            mid = (high + low) // 2

            if self.hits[mid] <= timestamp:
                low = mid + 1
            else:
                high = mid - 1

        return high

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)