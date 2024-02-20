class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort()
        results = [intervals[0]]

        for interval in intervals[1:]:
            set1 = results[-1]
            set2 = interval

            a1 = set1[0]
            b1 = set2[0]
            a2 = set1[1]
            b2 = set2[1]

            merged_interval = []
            if a2 >= b1:
                merged_interval.append(min(a1, b1))
                merged_interval.append(max(a2, b2))
                results[-1] = merged_interval
            else:
                results.append(set2)
        
        return results
                
