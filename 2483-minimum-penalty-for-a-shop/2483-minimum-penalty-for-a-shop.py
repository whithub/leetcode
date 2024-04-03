class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        # Potentially short circuit 2 scenarios: all Y and all N:
        if "Y" not in customers: # all N -- "NNNN"
            return 0
        if "N" not in customers: # all Y -- "YYYY"
            return n

        # We do not need the actual penalty values. The problem only requires the earliest hour with the lowest penalty.
        #   what matters is the penalty of the hours relative to each other
        
        cur_penalty = 0
        min_penalty = 0
        closing_hour = 0

        for hour in range(n):
            if customers[hour] == 'Y':
                cur_penalty -= 1
            else:
                cur_penalty += 1
            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                closing_hour = hour + 1

        return closing_hour

        # It makes a little more sense to me if cur_penalty = len(customers) vs. going into the negatives

        # customers = "YYNYNYYY"      | Y Y N Y N Y Y Y
        # cur_penalty  = 8            | 7 6 7 6 7 6 5 4
        # min_penalty  = float('inf') | 7 6 6 6 6 6 5 4
        # closing_hour = 0            | 1 2 2 2 2 2 7 8 ---> return closing_hour (8)

        # customers = "YNNY"          | Y N N Y
        # cur_penalty  = 4            | 3 4 5 4
        # min_penalty  = float('inf') | 3 3 3 3
        # closing_hour = 0            | 1 1 1 1 ---> return closing_hour (1)

        # customers = "NNNNN"         | N N N N N 
        # cur_penalty  = 5            | 4 3 2 1 0
        # min_penalty  = float('inf') | 4 3 2 1 0
        # closing_hour = 0            | 1 2 3 4 5 ---> return closing_hour (5)