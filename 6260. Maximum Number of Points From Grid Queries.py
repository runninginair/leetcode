''' 6260. Maximum Number of Points From Grid Queries

Weekly Contest 323      Problem # 4     

User Accepted:763   User Tried:1884     Total Accepted:821     Total Submissions:3720
Difficulty:Hard

You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queres[i] you start in the top left cell of the matrix and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.

 

Example 1:


Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.
Example 2:


Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
k == queries.length
1 <= k <= 104
1 <= grid[i][j], queries[i] <= 106
'''

import bisect
from collections import Counter
from heapq import heappop, heappush
from math import inf
from typing import List


class Solution: ### My Solution
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        return [-1]

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

class Solution_v1(object):
    def maxPoints(self, grid, queries):
        m = len(grid)
        n = len(grid[0])

        pts = []
        for i in range(m):
            for j in range(n):
                pts.append((grid[i][j], i, j))
        pts.sort(key = lambda x: -x[0])
        
        UF = DisjointSetUnion(m * n)
        best = 1
        
        ans = {}
        for v in sorted(queries):
            while pts and pts[-1][0] < v:
                w, ii, jj = pts.pop()
                
                for di, dj in zip([0,0,-1,1], [1,-1,0,0]):
                    i2, j2 = ii + di, jj + dj
        
                    
                    if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] <= w:
                        UF.union(n * i2 + j2, n * ii + jj)
            
                best = max(best, UF.set_size(n * ii + jj))
                
            ans[v] = UF.set_size(0)
            
        out = [ans[v] if v > grid[0][0] else 0 for v in queries]
        return out


class Solution_v2:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        e = [[0] * n for _ in range(m)]
        e[0][0] = 1
        h = [(grid[0][0] + 1, 0, 0)]
        c = Counter()
        while h:
            req, i, j = heappop(h)
            c[req] += 1
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and e[x][y] == 0:
                    e[x][y] = 1
                    heappush(h, (max(req, grid[x][y] + 1), x, y))
        t = sorted(c.items())
        p = [(0, 0)]
        for a, b in t:
            p.append((a, p[-1][1] + b))
        return [p[bisect.bisect(p, (q, inf))-1][1] for q in queries]