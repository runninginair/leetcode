''' 2316. Count Unreachable Pairs of Nodes in an Undirected Graph

Medium      574     17      Companies

You are given an integer n. There is an undirected graph with n nodes, numbered
from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi]
denotes that there exists an undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.


Example 1:     (0)-------(2)
                  \     /
                   \   /
                    (1)

Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation: There are no pairs of nodes that are unreachable from each other.
Therefore, we return 0.


Example 2:      (0)----(2)      (3)     (1)
                 |      |                |
                (5)----(4)              (6)

Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation: There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.
 

Constraints:            1 <= n <= 10^5
                        0 <= edges.length <= 2 * 10^5
                        edges[i].length == 2
                        0 <= ai, bi < n
                        ai != bi
                        There are no repeated edges.
Accepted:               21.8K
Submissions:            56.2K
Acceptance Rate:        38.8%
'''

from collections import defaultdict
from typing import List

class Solution_v1:     ### Time Limit Exceeded     56 / 66 testcases passed
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        visited, forrest = set(), []
        def dfs(i) -> int:
            visited.add(i)
            q, cnt = [i], 1
            while q:
                node = q.pop()
                for nei in adjList[node]:
                    if nei not in visited:
                        visited.add(nei)
                        cnt += 1
                        q.append(nei)
            return cnt

        for i in range(n):
            if i not in visited:
                cnt = dfs(i)
                if cnt == n: return 0
                forrest.append(cnt)

        ans = 0
        for i in range(len(forrest) - 1):
            for j in range(i + 1, len(forrest)):
                ans += forrest[i] * forrest[j]
        return ans

class Solution_v1_2:     ### DFS Passed!
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        visited, forrest = set(), []
        def dfs(x) -> int:
            visited.add(x)
            q, cnt = [x], 1
            while q:
                node = q.pop()
                for nei in adjList[node]:
                    if nei not in visited:
                        visited.add(nei)
                        cnt += 1
                        q.append(nei)
            return cnt

        for i in range(n):
            if i not in visited:
                cnt = dfs(i)
                if cnt == n: return 0
                forrest.append(cnt)

        ans = 0
        for tree in forrest: ans += tree * (n - tree)
        return ans >> 1

class Solution_v2:     ### Union Find   TLE     56 / 66 testcases passed
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        djs = DisJointSets(n)
        for x, y in edges: djs.union(x, y)
        # print(djs._parents)
        map, forrest = {}, []
        for i in range(n):
            num = djs.find(i)
            if num in map: map[num] += 1
            else: map[num] = 1
        for val in map.values(): forrest.append(val)
        if len(forrest) == 1: return 0
        ans = 0
        for i in range(len(forrest) - 1):
            for j in range(i + 1, len(forrest)):
                ans += forrest[i] * forrest[j]
        return ans

class Solution_v2_2:     ### Passed!
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        djs = DisJointSets(n)
        for x, y in edges: djs.union(x, y)
        # print(djs._parents)
        map, forrest = {}, []
        for i in range(n):
            num = djs.find(i)
            if num in map: map[num] += 1
            else: map[num] = 1
        for val in map.values(): forrest.append(val)
        if len(forrest) == 1: return 0
        ans = 0
        for tree in forrest: ans += tree * (n - tree)
        return ans >> 1

class DisJointSets():
    def __init__(self, N):
        # Initially, all elements are single element subsets
        self._parents = [node for node in range(N)]
        self._ranks = [1 for _ in range(N)]

    def find(self, u) -> int:
        if u == self._parents[u]: return u
        self._parents[u] = self.find(self._parents[u])
        return self._parents[u]

    def connected(self, u, v) -> bool:
        return self.find(u) == self.find(v)

    def union(self, u, v) -> None:
        # Union by rank optimization
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v: return
        if self._ranks[root_u] > self._ranks[root_v]:
            self._parents[root_v] = root_u
        elif self._ranks[root_v] > self._ranks[root_u]:
            self._parents[root_u] = root_v
        else:
            self._parents[root_u] = root_v
            self._ranks[root_v] += 1

class Solution_v3:  ### DSU 
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        def findParent(i):
            if i == parents[i]: return i
            parents[i] = findParent(parents[i])
            return parents[i]
        for u, v in edges:
            up, vp = findParent(u), findParent(v)
            parents[vp] = up
        count = defaultdict(int) 
        for i in range(n):
            count[findParent(i)] += 1
        res = 0
        valSum = sum(count.values())
        for num in count.values():
            res += num * (valSum - num)
            valSum -= num
        return res

class Solution_v3_2:  ### DSU 
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        def findParent(i):
            if i == parents[i]: return i
            parents[i] = findParent(parents[i])
            return parents[i]
        for u, v in edges:
            up, vp = findParent(u), findParent(v)
            parents[vp] = up
        res, count = 0, defaultdict(int) 
        for i in range(n): count[findParent(i)] += 1
        for num in count.values(): res += num * (n - num)
        return res >> 1


def main():
    sol = Solution_v1()
    sol = Solution_v1_2()

    # sol = Solution_v2()
    # sol = Solution_v2_2()

    # sol = Solution_v3()
    # sol = Solution_v3_2()


    n, edges = 3, [[0,1],[0,2],[1,2]]
    print(sol.countPairs(n, edges))       # Output: 0

    n, edges = 7, [[0,2],[0,5],[2,4],[1,6],[5,4]]
    print(sol.countPairs(n, edges))       # Output: 14

    n, edges = 11, [[5,0],[1,0],[10,7],[9,8],[7,2],[1,3],[0,2],[8,5],[4,6],[4,2]]
    print(sol.countPairs(n, edges))       # Output: 0

    n, edges = 82, [[9,46],[20,5],[32,24],[4,6],[16,71],[36,34],[14,55],[5,1],[11,58],[3,43],[23,26],[8,21],[14,25],[4,16],[63,70],[63,64],[53,50],[28,14],[37,38],[31,34],[22,30],[3,35],[0,2],[33,0],[3,0],[62,7],[47,34],[59,22],[48,25],[14,12],[7,5],[76,22],[1,40],[57,31],[11,7],[6,29],[63,25],[17,49],[37,51],[81,15],[24,9],[33,61],[62,67],[77,51],[69,52],[31,17],[4,3],[18,73],[1,9],[0,8],[12,39],[75,46],[16,17],[65,12],[22,44],[56,72],[6,22],[66,42],[31,79],[74,30],[43,50],[9,15],[14,60],[11,19],[68,42],[80,34],[72,78],[1,0],[12,7],[6,42],[13,8],[10,6],[38,54],[46,52],[13,41],[18,6],[56,3],[38,45],[37,0],[23,0],[27,9]]
    print(sol.countPairs(n, edges))       # Output: 0


if __name__ == "__main__":
    main()
