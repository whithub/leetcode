class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)       # 3
        cols = len(img[0])    # 3

        result = [[0] * cols for _ in range(rows)] # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(rows):
            for j in range(cols):
                total_sum = 0
                count = 0

                for x in range(max(0, i-1), min(rows, i+2)):
                    for y in range(max(0, j-1), min(cols, j+2)):
                        total_sum += img[x][y]
                        count += 1

                result[i][j] = total_sum // count
                # [[137, 0, 0], [0, 0, 0], [0, 0, 0]]
                # [[137, 141, 0], [0, 0, 0], [0, 0, 0]]
                # [[137, 141, 137], [0, 0, 0], [0, 0, 0]]
                # [[137, 141, 137], [141, 0, 0], [0, 0, 0]]
                # [[137, 141, 137], [141, 138, 0], [0, 0, 0]]
                # [[137, 141, 137], [141, 138, 141], [0, 0, 0]]
                # [[137, 141, 137], [141, 138, 141], [137, 0, 0]]
                # [[137, 141, 137], [141, 138, 141], [137, 141, 0]]
                # [[137, 141, 137], [141, 138, 141], [137, 141, 137]]

        return result