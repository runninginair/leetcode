''' 1857. Largest Color Value in a Directed Graph

Hard        736         26          Companies

There is a directed graph of n colored nodes and m edges. The nodes are
numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter
representing the color of the ith node in this graph (0-indexed). You are also
given a 2D array edges where edges[j] = [aj, bj] indicates that there is a
directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk
such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The
color value of the path is the number of nodes that are colored the most
frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1
if the graph contains a cycle.


Example 1:

        (1) <-- (0) --> (2) --> (3) --> (4)

Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a"
(red in the above image).


Example 2:
                (0) <--|
                 |_____|

Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.
 

Constraints:        n == colors.length
                    m == edges.length
                    1 <= n <= 10^5
                    0 <= m <= 10^5
                    colors consists of lowercase English letters.
                    0 <= a-j, b-j < n
Accepted:           16.6K
Submissions:        39.8K
Acceptance Rate:    41.6%
'''

from collections import defaultdict
from typing import List


class Solution:  # toplogic sort solution  YouTuber ID: Elite Code
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # N = len(colors)
        # ### Init G as the adjancent list Graph; V to trace the node if we have visited.
        # G, V = [[] for _ in range(N)], [0] * N
        # for u, v in edges: G[u].append(v)
        # def dfs(u):
        #     print("Node:", u, "\nG:", G, "\nV:", V, end="\n\n")
        #     if V[u] == 2: return True
        #     if V[u] == 1: return False
        #     V[u] = 1    ### Node u marked as 1, means it has been visited.
        #     for nxt in G[u]:
        #         if not dfs(nxt): return False
        #     V[u] = 2    ### Node u marked as 2, means it has been explored.
        #     return True
        # for u in range(N):
        #     if not dfs(u): return -1    ### Line 58 ~ 72 would deteck if G is DAG.

        N = len(colors)
        G, V = [[] for _ in range(N)], [0] * N
        D = [[0] * 26 for _ in range(N)]  ### Use D to track the max color in node.
        for u, v in edges: G[u].append(v)

        def dfs(u):
            if V[u] == 2:
                return True
            if V[u] == 1:
                return False
            V[u] = 1
            for v in G[u]:
                if not dfs(v):
                    return False
                for c in range(26):
                    D[u][c] = max(D[u][c], D[v][c])
            D[u][ord(colors[u]) - ord('a')] += 1
            V[u] = 2
            return True

        for u in range(N):
            if not dfs(u):
                return -1
        return max(max(color) for color in D)


class Solution_Neetcode:  # Youtuber Neetcode solution  T: O(n * m)
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        # Return max freq of color
        def dfs(node):
            if node in path:
                return float("inf")
            if node in visit:
                return 0
            visit.add(node)
            path.add(node)

            colorIndex = ord(colors[node]) - ord('a')
            count[node][colorIndex] = 1

            for nei in adj[node]:
                if dfs(nei) == float('inf'):
                    return float('inf')
                for c in range(26):
                    count[node][c] = max(
                        count[node][c],
                        (1 if c == colorIndex else 0) + count[nei][c]
                    )
            path.remove(node)
            return max(count[node])

        n, res = len(colors), 0
        visit, path = set(), set()
        count = [[0] * 26 for i in range(n)]
        for i in range(n):
            res = max(dfs(i), res)
        return -1 if res == float('inf') else res


def main():
    sol = Solution_Neetcode()
    sol = Solution()

    colors, edges = "abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]     # Output: 3
    print(sol.largestPathValue(colors, edges))

    colors, edges = "abacabca", [[1, 0], [0, 5],[1, 2], [2, 3], [3, 4], [4, 2], [5, 4], [6, 0], [6, 2], [7, 0]]     # Output: -1
    print(sol.largestPathValue(colors, edges))


if __name__ == "__main__":
    main()
