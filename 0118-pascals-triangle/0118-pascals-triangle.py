class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        
        result = [[1], [1,1]]

        for i in range(numRows-2):
            previous_row = result[-1]
            next_row = []

            # build next row
            for i in range(len(previous_row)-1):
                a,b = previous_row[i], previous_row[i+1]
                next_row.append(a+b)
            
            # bookend with 1's
            next_row.insert(0,1)
            next_row.append(1)
            result.append(next_row)
        
        return result