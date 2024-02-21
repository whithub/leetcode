class Solution:
    def reorganizeString(self, s: str) -> str:
        characters = list(s)
            # ['a', 'a', 'a', 'a', 'b', 'b', 'c', ]
        uniq_chars = set(characters)
        char_count_pq = []
        for char in uniq_chars:
            count = characters.count(char)
            char_count_pq.append((count, char))
            # char_count_pq = [(1, 'c'), (4, 'a'), (2, 'b')]

        heapq._heapify_max(char_count_pq) # => char_count_pq still looks out of order: [(1, 'c'), (4, 'a'), (2, 'b')]
                                          # But it's turned the char_count_pq List into a heap/priority_queue...
                                          # So that when we call heappop, it will select the correct element
            # For min-heap: heapq.heapify(char_count_pq) ------- heappop(char_count_pq) => (1, 'c')
            # For max-heap: heapq._heapify_max(char_count_pq) -- heappop(char_count_pq) => (4, 'a')

        answer = []
        while char_count_pq:
            count, char = heappop(char_count_pq)

            if not answer:
                answer.append(char)
                count -= 1

            if count == 0 and len(char_count_pq) == 0:
                break

            if answer[-1] != char:
                answer.append(char)
                count -= 1
            elif answer[-1] == char and len(char_count_pq) >=1:
                count_2, char_2 = heappop(char_count_pq)
                answer.append(char_2)
                count_2 -= 1
                if count_2 > 0:
                    heappush(char_count_pq, (count_2, char_2))
            elif answer[-1] == char and len(char_count_pq) == 0:
                answer = []
                char_count_pq = []
                break

            if count > 0:
                heappush(char_count_pq, (count, char))
                heapq._heapify_max(char_count_pq)

        return ''.join(answer)