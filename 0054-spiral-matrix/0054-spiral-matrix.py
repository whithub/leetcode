class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        if not matrix:
            return answer

        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        direction = "right"

        while top <= bottom and left <= right:
            if direction == "right":
                for col in range(left, right + 1):
                    answer.append(matrix[top][col])
                top += 1
                direction = "down"
            elif direction == "down":
                for row in range(top, bottom + 1):
                    answer.append(matrix[row][right])
                right -= 1
                direction = "left"
            elif direction == "left":
                for col in range(right, left - 1, -1):
                    answer.append(matrix[bottom][col])
                bottom -= 1
                direction = "up"
            elif direction == "up":
                for row in range(bottom, top - 1, -1):
                    answer.append(matrix[row][left])
                left += 1
                direction = "right"
        return answer