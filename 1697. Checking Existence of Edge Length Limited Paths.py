''' 1697. Checking Existence of Edge Length Limited Paths

Hard        826         16          Companies

An undirected graph of n nodes is defined by edgeList, where edgeList[i] =
[u-i, v-i, dis-i] denotes an edge between nodes u-i and v-i with distance dis-i.
Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [p-j, q-j, limit-j], your task is to
determine for each queries[j] whether there is a path between pj and qj such
that each edge on the path has a distance strictly less than limit-j .

Return a boolean array answer, where answer.length == queries.length
and the j-th value of answer is true if there is a path for queries[j] is true,
and false otherwise.


Example 1:                   (0)
                           /     \
                    2, 16 /       \ 8
                         /    4    \ 
                      (1) --------- (2)
   
Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping
edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2,
thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less
than 5, thus we return true for this query.


Example 2:

Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Exaplanation: The above figure shows the given graph.
 

Constraints:        2 <= n <= 10^5
                    1 <= edgeList.length, queries.length <= 10^5
                    edgeList[i].length == 3
                    queries[j].length == 3
                    0 <= ui, vi, pj, qj <= n - 1
                    ui != vi
                    pj != qj
                    1 <= disi, limitj <= 10^9
                    There may be multiple edges between two nodes.
Accepted:           15.4K
Submissions:        28.9K
Acceptance Rate:    53.4%
'''

from typing import List
import math


class Solution_v1:     ### Time Limit Exceeded       12 / 23 testcases passed
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = [False for _ in range(len(queries))]
        G = [[math.inf for _ in range(n)] for _ in range(n)]
        for a, b, dis in edgeList:
            G[a][b] = G[b][a] = min(G[a][b], dis)

        def BFS(a: int, b: int, limit: int) -> bool:
            q, seen = [a], set([a])
            while q:
                node = q.pop()
                for nei in range(n):
                    if nei not in seen and G[node][nei] < limit:
                        if nei == b: return True
                        seen.add(nei)
                        q.append(nei)
            return False

        for i, query in enumerate(queries):
            x, y, lim = query
            if BFS(x, y, lim):
                ans[i] = True
        return ans

class Solution_v2:     ### Time Limit Exceeded       18 / 23 testcases passed
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = [False for _ in range(len(queries))]
        ADJ = [{} for _ in range(n)]
        for a, b, dis in edgeList:
            if b not in ADJ[a]:
                ADJ[a][b] = ADJ[b][a] = dis
            else:
                ADJ[a][b] = ADJ[b][a] = min(dis, ADJ[a][b])

        def BFS(a: int, b: int, limit: int) -> bool:
            q, seen = [a], set([a])
            while q:
                node = q.pop()
                for nei in ADJ[node]:
                    if nei not in seen and ADJ[node][nei] < limit:
                        if nei == b: return True
                        seen.add(nei)
                        q.append(nei)
            return False

        for i, query in enumerate(queries):
            x, y, lim = query
            if BFS(x, y, lim):
                ans[i] = True
        return ans

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
            elif self.rank[px] > self.rank[py]:
                self.parent[py] = px
            else:
                self.parent[py] = px
                self.rank[px] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution_UnionFind:
    def distanceLimitedPathsExist(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edges = sorted(edges, key=lambda x: x[2])
        ans = [False] * len(queries)
        uf = UnionFind(n)
        i = 0
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][2])
        for q_idx, (u, v, limit) in sorted_queries:
            while i < len(edges) and edges[i][2] < limit:
                uf.union(edges[i][0], edges[i][1])
                i += 1
            ans[q_idx] = uf.connected(u, v)
        return ans


def main():
    sol = Solution_v1()
    sol = Solution_v2()
    sol = Solution_UnionFind()

    n = 3
    edgeList = [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]]
    queries = [[0, 1, 2], [0, 2, 5]]     # Output: [false,true]
    print(sol.distanceLimitedPathsExist(n, edgeList, queries))

    n = 5
    edgeList = [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]]
    queries = [[0, 4, 14], [1, 4, 13]]       # Output: [true,false]
    print(sol.distanceLimitedPathsExist(n, edgeList, queries))


if __name__ == "__main__":
    main()
