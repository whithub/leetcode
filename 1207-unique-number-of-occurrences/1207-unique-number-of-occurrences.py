class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # arr = [-3,0,1,-3,1,1,1,-3,10,0]

        el_counts = {}

        for el in arr:
            if el in el_counts.keys():
                el_counts[el] = el_counts[el] + 1
            else:
                el_counts[el] = 1
        # el_counts = {-3: 3, 0: 2, 1: 4, 10: 1}

        uniq_counts = set(el_counts.values()) # {1, 2, 3, 4}
        uniq_el = set(arr)                    # {0, 1, 10, -3}

        return len(uniq_counts) == len(uniq_el)