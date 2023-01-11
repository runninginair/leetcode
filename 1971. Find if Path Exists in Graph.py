''' 1971. Find if Path Exists in Graph
Easy    1.8K    95      Companies

There is a bi-directional graph with n vertices, where each vertex is labeled
from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D
integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional
edge between vertex ui and vertex vi. Every vertex pair is connected by at most
one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source
to vertex destination.

Given edges and the integers n, source, and destination, return true if there
is a valid path from source to destination, or false otherwise.


Example 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Example 2:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
 

Constraints:    1 <= n <= 2 * 10^5
                0 <= edges.length <= 2 * 10^5
                edges[i].length == 2
                0 <= ui, vi <= n - 1
                ui != vi
                0 <= source, destination <= n - 1
                There are no duplicate edges.
                There are no self edges.
Accepted:       155.3K
Submissions:    308K
Acceptance Rate: 50.4%

'''

from typing import List


class Solution:     ### DFS Solution    O(n + edges)
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        adjList, seen = {}, set()
        for a, b in edges:
            if a in adjList: adjList[a].append(b)
            else: adjList[a] = [b]
            if b in adjList: adjList[b].append(a)
            else: adjList[b] = [a]

        que = [source]
        while que:
            curr = que.pop()
            if curr == destination: return True
            seen.add(curr)            
            for node in adjList[curr]:
                if node not in seen: que.append(node)

        return False

class Solution_v1:  ### BFS Solution    O(n + edges)
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList, seen = [[] for _ in range(n)], set()
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        que = [source]
        while que:
            curr = que.pop()
            if curr == destination: return True
            seen.add(curr)
            for node in adjList[curr]:
                if node not in seen: que.append(node)
        return False


class Solution_v2:      ### Uion Find Solution
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:    
        # uf = QuickFind(n)
        # uf = QuickUnion(n)
        uf = UnionFind(n)
        for u, v in edges: uf.union(u, v)
        return uf.find(source) == uf.find(destination)

class QuickFind():      ###   Quick Find    Not Efficient TLE
    def __init__(self,N):
        self._parents = list(range(0, N))

    def find(self, p):
        return(self._parents[p])
        
    def union(self, p, q):
        root_p, root_q = self._parents[p], self._parents[q]
        for i in range(0, len(self._parents)):
            if(self._parents[i] == root_p):
                self._parents[i] = root_q

    def connected(self,p,q):
        return self._parents[p] == self._parents[q]

class QuickUnion():
    def __init__(self,N):
        self._parents = list(range(0,N))
    
    def find(self, p):
        while(p != self._parents[p]):
            p = self._parents[p]
        return p
    
    def union(self, p, q):
        root_p, root_q = self.find(p), self.find(q)
        self._parents[root_p] = root_q

    def connected(self, p, q):
        return self.find(p)==self.find(q)

class UnionFind:    ### Weighted Quick Union with optimization
    def __init__(self, N: int):
        self.parent = [node for node in range(N)]
        self.rank = [1 for _ in range(N)]

    def find(self, a: int) -> int:   ### path compression technique
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a: int, b: int) -> bool:   ### Union by rank optimization
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b: return True
        if self.rank[root_a] > self.rank[root_b]: self.parent[root_b] = a
        elif self.rank[root_b] > self.rank[root_a]: self.parent[root_a] = b
        else:
            self.parent[root_a] = root_b
            self.rank[root_b] += 1
        return False

def main():
    # sol = Solution()
    # sol = Solution_v1()
    sol = Solution_v2()

    n, edges, source, destination = 1, [], 0, 0
    print(sol.validPath(n, edges, source, destination)) # Output: true    

    n, edges, source, destination = 3, [[0,1],[1,2],[2,0]], 0, 2
    print(sol.validPath(n, edges, source, destination)) # Output: true

    n, edges, source, destination = 6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5
    print(sol.validPath(n, edges, source, destination)) # Output: false

    n, edges, source, destination = 10, [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]], 5, 9
    print(sol.validPath(n, edges, source, destination)) # Output: True


main()
