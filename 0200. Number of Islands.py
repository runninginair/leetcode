''' 200. Number of Islands
Medium      17605       403     Add to List     Share
Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.


Example 1:
Input: grid = [ ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"] ]
Output: 1

Example 2:
Input: grid = [ ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"] ]
Output: 3

Constraints:    m == grid.length
                n == grid[i].length
                1 <= m, n <= 300
                grid[i][j] is '0' or '1'.
Accepted:       1,931,166
Submissions:    3,436,320
'''

class Solution:         ### T(n) = O(n^2)   S(n) = O(n^2)
    def numIslands(self, grid) -> int:
        m, n, counter = len(grid), len(grid[0]), 0
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        # print(visited)
        # print(grid)
        def bfs(i, j):
            q = [(i, j)]
            while q:
                x, y = q.pop(0)
                visited[x][y] = True
                if x > 0 and grid[x - 1][y] == '1' and not visited[x - 1][y]:
                    visited[x - 1][y] = True
                    q.append((x - 1, y))
                if x < m - 1 and grid[x + 1][y] == '1' and not visited[x + 1][y]:
                    visited[x + 1][y] = True
                    q.append((x + 1, y))
                if y > 0 and grid[x][y - 1] == '1' and not visited[x][y - 1]:
                    visited[x][y - 1] = True
                    q.append((x, y - 1))
                if y < n - 1 and grid[x][y + 1] == '1' and not visited[x][y + 1]:
                    visited[x][y + 1] = True
                    q.append((x, y + 1))
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    # print(visited)
                    counter += 1
                    bfs(i, j)
        return counter

class Solution_v2:      ### T(n) = O(n^2)   S(n) = O(1)
    def numIslands(self, grid) -> int:
        m, n, counter = len(grid), len(grid[0]), 0
        
        def bfs(i, j):
            q = [(i, j)]
            while q:    ### Mark the grid as "X" means has been visited.
                x, y = q.pop(0)
                grid[x][y] = 'X'
                if x > 0 and grid[x - 1][y] == '1':
                    grid[x - 1][y] = 'X'
                    q.append((x - 1, y))
                if x < m - 1 and grid[x + 1][y] == '1':
                    grid[x + 1][y] = 'X'
                    q.append((x + 1, y))
                if y > 0 and grid[x][y - 1] == '1':
                    grid[x][y - 1] = 'X'
                    q.append((x, y - 1))
                if y < n - 1 and grid[x][y + 1] == '1':
                    grid[x][y + 1] = 'X'
                    q.append((x, y + 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    counter += 1
                    bfs(i, j)
        return counter

class Solution_v3:      ### Union Find // (Also called) Disjoint Set
    def numIslands(self, grid) -> int:
        '''
        DSU (Disjoint Set Union)
        '''
        dsu = DSU()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    print("Position[i][j] =", i, j)
                    # _ = dsu.find((i, j))
                    dsu.find((i, j))
                    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        # print("DSU Roots:", dsu.roots)
                        if (x, y) in dsu.roots:
                            dsu.union((i, j), (x, y))
                            print("AfterUnion:", dsu.roots, end="\n\n")
        return len(set([dsu.find(root) for root in dsu.roots.values()]))

class DSU:  ### Disjoint Set Uion (Union Find)
    def __init__(self) -> None:
        self.roots = {}     # root, also called parent or representative
        self.ranks = {}

    def find(self, pos):
        if pos not in self.roots:
            self.roots[pos] = pos
            self.ranks[pos] = 1
            print("\t #0 Find - pos", pos)
            return pos
        else:
            res = pos
            path = set()
            while res != self.roots[res]:
                path.add(res)
                res = self.roots[res]
            # path compression
            for node in path:
                self.roots[node] = res
                print("\t # Find - path compression:", self.roots[node])
            print("\t #1 Find - res", res)
            return res
        
    def union(self, pos1, pos2):
        r1, r2 = self.find(pos1), self.find(pos2)
        if r1 != r2:
            print("\t #0 Union Ranks:(r_pos1, r_pos2) ",self.ranks[r1], self.ranks[r2])
            if self.ranks[r1] >= self.ranks[r2]:
                self.roots[r2] = r1
                self.ranks[r1] += self.ranks[r2]
                print("\t #1 Union Ranks:(r_pos1, r_pos2) ",self.ranks[r1], self.ranks[r2])
            else:
                self.roots[r1] = r2
                self.ranks[r2] += self.ranks[r1]
                print("\t #2 Union Ranks:(r_pos1, r_pos2) ",self.ranks[r1], self.ranks[r2])


def main():
    # sol = Solution()
    # sol = Solution_v2()
    sol = Solution_v3()

    grid = [ ["1","1"],
             ["0","1"],
             ["1","1"] ]     # Output: 3
    print(sol.numIslands(grid))

    # grid = [ ["1","1","1","1","0"],
    #          ["1","1","0","1","0"],
    #          ["1","1","0","0","0"],
    #          ["0","0","0","0","0"] ]     # Output: 1
    # print(sol.numIslands(grid))

    # grid = [ ["1","1","0","0","0"],
    #          ["1","1","0","0","0"],
    #          ["0","0","1","0","0"],
    #          ["0","0","0","1","1"] ]     # Output: 3
    # print(sol.numIslands(grid))

    # grid = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
    #         ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
    #         ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
    #         ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    #         ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    #         ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
    #         ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
    #         ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
    #         ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
    #         ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    #         ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
    #         ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    #         ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    #         ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
    #         ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
    #         ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
    #         ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
    #         ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    #         ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    #         ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
    # print(sol.numIslands(grid))


main()
