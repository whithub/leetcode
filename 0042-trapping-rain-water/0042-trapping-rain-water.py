class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        answer = 0
        n = len(height)
        left_max, right_max = [0] * n, [0] * n

        for i in range(n):
            if i == 0:
                left_max[i] = height[i]
            else:    
                left_max[i] = max(left_max[i - 1], height[i])

        end_idx = n-1
        for i in range(end_idx, -1, -1):
            if i == end_idx:
                right_max[i] = height[i]
            else:
                right_max[i] = max(right_max[i + 1], height[i])

        # left_max = [4, 4, 4, 4, 4, 5]
        # right_max = [5, 5, 5, 5, 5, 5]

        for i in range(1, n):
            answer += min(left_max[i], right_max[i]) - height[i]

        return answer
