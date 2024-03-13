class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        x = 0
        y = len(height)-1
        # idea is to start from both ends
        #   - update the smallest vertical line after checking area

        while x < y:
            left_vertical = height[x]
            right_vertical = height[y]
            area = min(left_vertical,right_vertical) * (y-x)

            max_area = max(max_area, area)

            if left_vertical < right_vertical:
                x += 1
            else:                
                y -= 1
        return max_area


        # Time Limit Exceeded solution:
        # max_area = 0
        # x = 0
        # y = 1

        # while x < len(height)-1:
        #     a = height[x]
        #     b = height[y]
        #     area = min(a,b) * (y-x)

        #     max_area = max(max_area, area)

        #     y += 1
        #     if y == len(height):
        #         x += 1
        #         y = x + 1

        # return max_area

        