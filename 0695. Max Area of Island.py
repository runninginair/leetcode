''' 695. Max Area of Island
Medium      8047        178     Add to List     Share
You are given an m x n binary matrix grid. An island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,1,1,0,1,0,0,0,0,0,0,0,0],
               [0,1,0,0,1,1,0,0,1,0,1,0,0],
               [0,1,0,0,1,1,0,0,1,1,1,0,0],
               [0,0,0,0,0,0,0,0,0,0,1,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:    m == grid.length
                n == grid[i].length
                1 <= m, n <= 50
                grid[i][j] is either 0 or 1.
Accepted:       623,428
Submissions:    870,324
'''


class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        def bfs(i, j):
            que = [(i, j)]
            area = 0
            while que:
                x, y = que.pop(0)
                if visited[x][y]: continue
                else: visited[x][y] = True
                area += 1
                if x > 0 and grid[x - 1][y] == 1 and not visited[x - 1][y]:
                    que.append((x - 1, y))
                if x < m - 1 and grid[x + 1][y] == 1 and not visited[x + 1][y]:
                    que.append((x + 1, y))
                if y > 0 and grid[x][y - 1] == 1 and not visited[x][y - 1]:
                    que.append((x, y - 1))
                if y < n - 1 and grid[x][y + 1] == 1 and not visited[x][y + 1]:
                    que.append((x, y + 1))
            return area

        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    maxArea = max(maxArea, bfs(i, j))
        return maxArea


def main():
    sol = Solution()
    g = [[1,1,0,0,0],
         [1,1,0,0,0],
         [0,0,0,1,1],
         [0,0,0,1,1]]       # Output: 4
    print(sol.maxAreaOfIsland(g))


main()