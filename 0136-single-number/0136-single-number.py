class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dupes = []

        for el in nums:
            if el in dupes:
                dupes.remove(el)
            else:
                dupes.append(el)

        return dupes[0]