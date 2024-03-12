class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        island_count = 0

        x = 0
        y = 0
        while x < self.m and y < self.n:
            if grid[x][y] == '1':
                island_count += 1
                self.dfs(grid, x, y)
            y += 1

            if y == self.n:
                x += 1
                y = 0
        return island_count

            
    def dfs(self, grid, x, y):
        directions = [(0,1), (0,-1), (-1,0), (1,0)] # (x,y) --> √Right, √Left, √Up, √Down
                                # (0,1)     |   (0,-1)    |   (-1,0)    |   (1,0)
        for pair in directions: # x=0, y=0  |   x=0, y=0  |   x=0, y=0  |   x=0, y=0
            nx = x + pair[0]    # 0         |   0         |   -1        |   1
            ny = y + pair[1]    # 1         |   -1        |   0         |   0

            if (nx >= 0 and ny >= 0 and nx < self.m and ny < self.n and grid[nx][ny] == '1'):
                grid[nx][ny] = '0' # "visited"
                self.dfs(grid, nx, ny)


# grid = [
#     ["1","1","1","0","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
# ]
# [
#     ["0","1","0"],
#     ["1","0","1"],
#     ["0","1","0"]
# ]