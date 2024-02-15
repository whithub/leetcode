class Solution:
    def climbStairs(self, n: int) -> int:            # Sensing some fibonacci...
        step_count = [1,1]
        # ^^ 0 stairs: 1 way (staying put)
        #    1 stair: 1 way (taking 1 step)

        for i in range(n-1):
            sum = step_count[i] + step_count[i+1]
            step_count.append(sum)
            # n = 4 ... we won't only 3 iterations... range(n-1)
            # iterations: 0,1,2
            # 0 => 1 + 1
            #      [1,1,2]
            # 1 => 1 + 2
            #      [1,1,2,3]
            # 2 => 2 + 3
            #      [1,1,2,3,5]

        return step_count[-1]