import math
from heapq import heappop, _heapify_max

class Solution:
    keypad_size = 9

    def minimumKeypresses(self, s: str) -> int:
        # create maxheap that consists of letter counts
        letter_count = [] #=> [('p', 2), ('a', 1), ('l', 1) ('e', 1)]
        while s:
            char = s[0]
            x = s.count(char)
            letter_count.append((x, char))
            s = s.replace(char, '')

        heapq._heapify_max(letter_count)

        uniq_letters = set()
        keypress_count = 0

        # iterate thru heap, hitting multi-used letters first, btn_press * 1 -- up until 9 uniq letters, then btn_press += 1
        while letter_count:
            char_count, char = heappop(letter_count)

            if char not in uniq_letters:
                uniq_letters.add(char)

            btn_press_val = math.ceil(len(uniq_letters) / self.keypad_size)
            keypress_count += (char_count * btn_press_val)
            heapq._heapify_max(letter_count)

        return keypress_count





        