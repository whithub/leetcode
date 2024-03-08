class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False

        deck_partition = {}

        for num in deck:
            if num in deck_partition:
                deck_partition[num] = deck_partition[num] + 1
            else:
                deck_partition[num] = 1
        
        uniq_partitions_count = list(set(deck_partition.values()))
        uniq_partitions_count.sort()

        if len(uniq_partitions_count) < 2:
            return True

        x = uniq_partitions_count[0]
        y = uniq_partitions_count[1]

        greatest_common_demon = math.gcd(x, y)
        if greatest_common_demon < 2:
            return False

        if all(i % greatest_common_demon == 0 for i in uniq_partitions_count):
            return True

        return False