''' 200. Number of Islands
Medium      17129   394     Add to List     Share
Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:
Input: grid = [["1","1","1","1","0"],
               ["1","1","0","1","0"],
               ["1","1","0","0","0"],
               ["0","0","0","0","0"]]   Output: 1

Example 2:
Input: grid = [["1","1","0","0","0"],
               ["1","1","0","0","0"],
               ["0","0","1","0","0"],
               ["0","0","0","1","1"]]   Output: 3
 
Constraints:    m == grid.length
                n == grid[i].length
                1 <= m, n <= 300
                grid[i][j] is '0' or '1'.

Accepted:       1,877,788
Submissions:    3,354,486
'''

import time


class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    def numIslands(self, grid) -> int:
        num, m, n = 0, len(grid), len(grid[0])
        res = [[0 for _ in range(n)] for _ in range(m)]        

        def dfs(x, y):
            stack = []
            stack.append([x, y])
            while stack:
                t = stack.pop(-1)
                if t[0] > 0 and grid[t[0]-1][t[1]] == '1' and res[t[0]-1][t[1]] == 0:       # Up
                    res[t[0]-1][t[1]] = res[t[0]][t[1]]
                    stack.append([t[0]-1, t[1]])
                if t[0] < m - 1 and grid[t[0]+1][t[1]] == '1' and res[t[0]+1][t[1]] == 0:   # Down
                    res[t[0]+1][t[1]] = res[t[0]][t[1]]
                    stack.append([t[0]+1, t[1]])
                if t[1] > 0 and grid[t[0]][t[1]-1] == '1' and res[t[0]][t[1]-1] == 0:       # Left
                    res[t[0]][t[1]-1] = res[t[0]][t[1]]
                    stack.append([t[0], t[1]-1])
                if t[1] < n - 1 and grid[t[0]][t[1]+1] == '1' and res[t[0]][t[1]+1] == 0:   # Right
                    res[t[0]][t[1]+1] = res[t[0]][t[1]]
                    stack.append([t[0], t[1]+1])

        for i in range(m):
            for j in range(n):        
                if grid[i][j] == '1' and res[i][j] == 0:
                    num += 1
                    res[i][j] = num
                    dfs(i, j)

        return num

def main():
    sol = Solution()
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]   # Output: 1
    print(sol.numIslands(grid))

main()
