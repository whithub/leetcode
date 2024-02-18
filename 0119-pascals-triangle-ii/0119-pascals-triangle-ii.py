class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        triangle = [[1], [1,1]]

        for i in range(rowIndex-1):
            previous_row = triangle[-1]
            next_row = []

            for i in range(len(previous_row)-1):
                a,b = previous_row[i], previous_row[i+1]
                next_row.append(a+b)
            
            # bookend with 1's
            next_row.insert(0,1)
            next_row.append(1)
            triangle.append(next_row)

        return triangle[rowIndex]
            


        # [1]
        # [1,1]
        # [1,2,1]
        # [1,3,3,1]
        # [1,4,6,4,1]
        # [1,5,10,10,5,1]