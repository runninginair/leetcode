''' 1254. Number of Closed Islands
Medium      2467        57      Add to List     Share
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal
4-directionally connected group of 0s and a closed island is an island totally
(all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:
Input: grid = [[1, 1, 1, 1, 1, 1, 1, 0],
               [1, 0, 0, 0, 0, 1, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0],
               [1, 0, 0, 0, 0, 1, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [[0, 0, 1, 0, 0],
               [0, 1, 0, 1, 0],
               [0, 1, 1, 1, 0]]
Output: 1
Example 3:

Input: grid = [[1, 1, 1, 1, 1, 1, 1],
               [1, 0, 0, 0, 0, 0, 1],
               [1, 0, 1, 1, 1, 0, 1],
               [1, 0, 1, 0, 1, 0, 1],
               [1, 0, 1, 1, 1, 0, 1],
               [1, 0, 0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1]]
Output: 2
 

Constraints:    1 <= grid.length, grid[0].length <= 100
                0 <= grid[i][j] <=1
Accepted:       112,818
Submissions:    175,696

'''

class Solution:
    def closedIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])        
        if m < 3 or n < 3: return 0
        visited = [[False for _ in range(n)] for _ in range(m)]

    # if [x, y] is an island return True
        def bfs(i, j) -> bool:
            isIsland = True
            que = [[i, j]]
            while que:
                x, y = que.pop(0)
                visited[x][y] = True
                # print("x, y =", x, ",", y)

                if not visited[x - 1][y] and grid[x - 1][y] == 0:
                    if x - 1 == 0: isIsland = False
                    else: que.append([x - 1, y])
                if not visited[x + 1][y] and grid[x + 1][y] == 0:
                    if x + 2 == m: isIsland = False
                    else: que.append([x + 1, y])
                if not visited[x][y - 1] and grid[x][y - 1] == 0:
                    if y - 1 == 0: isIsland = False
                    else: que.append([x, y - 1])
                if not visited[x][y + 1] and grid[x][y + 1] == 0:
                    if y + 2 == n: isIsland = False
                    else: que.append([x, y + 1])
            return isIsland

        res = 0
        for i in range(1, m - 1):
            for j in range (1, n - 1):
                if grid[i][j] == 0 and not visited[i][j]:
                        if bfs(i, j): res += 1
        return res

def main():
    sol = Solution()

    # g = [[1,1,1,1,1,1,1,0],
    #      [1,0,0,0,0,1,1,0],
    #      [1,0,1,0,1,1,1,0],
    #      [1,0,0,0,0,1,0,1],
    #      [1,1,1,1,1,1,1,0]]
    # print(sol.closedIsland(g))
        # 0 1 2 3 4 5 6 7 8 9 
    g = [[0,0,1,1,0,1,0,0,1,0], # 0
         [1,1,0,1,1,0,1,1,1,0], # 1
         [1,0,1,1,1,0,0,1,1,0], # 2
         [0,1,1,0,0,0,0,1,0,1], # 3
         [0,0,0,0,0,0,1,1,1,0], # 4
         [0,1,0,1,0,1,0,1,1,1], # 5
         [1,0,1,0,1,1,0,0,0,1], # 6
         [1,1,1,1,1,1,0,0,0,0], # 7
         [1,1,1,0,0,1,0,1,0,1], # 8
         [1,1,1,0,1,1,0,1,1,0]] # 9
    print(sol.closedIsland(g))


main()
