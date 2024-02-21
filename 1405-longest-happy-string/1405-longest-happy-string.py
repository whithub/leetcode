class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []     
        if a > 0:
            pq.append((-a, 'a'))
        if b > 0:
            pq.append((-b, 'b'))
        if c > 0:
            pq.append((-c, 'c'))

        heapify(pq)
        ans = []
                
        while pq:
            first_count, first_char = heappop(pq)
            if len(ans) > 1 and (first_char == ans[-1] and first_char == ans[-2]):
                if not pq: break 
                second_count, second_char = heappop(pq)
                ans.append(second_char)

                if second_count + 1 != 0: # don't re-add to queue if char_count is 0...
                    heappush(pq, (second_count + 1, second_char))

                heappush(pq, (first_count, first_char))

            else:
                ans.append(first_char)

                if first_count + 1 != 0: # don't re-add to queue if char_count is 0...
                    heappush(pq, (first_count + 1, first_char))

        return''.join(ans)

