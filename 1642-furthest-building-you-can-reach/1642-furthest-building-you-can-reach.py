from heapq import heappop, heappush

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        ladder_allocations = [] # heap

        for idx in range(n):
            next = idx + 1

            if next < n:
                num1 = heights[idx]
                num2 = heights[next]
                climb = num2 - num1

                if climb <= 0:
                    continue

                heappush(ladder_allocations, climb)
                # print("ladder_allocations:", ladder_allocations)

                if len(ladder_allocations) <= ladders:
                    continue

                bricks -= heappop(ladder_allocations)
                # print("bricks:", bricks)

                if bricks < 0:
                    return idx

        return n - 1 # if we've made it here, that means we had enough ladders/bricks to climb every building