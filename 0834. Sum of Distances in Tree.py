''' 834. Sum of Distances in Tree
Hard    3.1K    66     Companies

There is an undirected connected tree with n nodes labeled from 0 to n - 1 and
n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi]
indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances
between the ith node in the tree and all other nodes.


Example 1:              0
                      /    \
                    1        2
                           / | \
                          3  4  5
Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

Example 2:
Input: n = 1, edges = []
Output: [0]

Example 3:              0
                      /
                    1
Input: n = 2, edges = [[1,0]]
Output: [1,1]
 

Constraints:        1 <= n <= 3 * 10^4
                    edges.length == n - 1
                    edges[i].length == 2
                    0 <= ai, bi < n
                    ai != bi
                    The given input represents a valid tree.
Accepted:           48.2K
Submissions:        88.5K
Acceptance Rate:    54.4%
'''

import collections
from typing import List


class Solution:     ### Time Limit Exceeded     64 / 73 testcases passed
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[0 for _ in range(n)] for _ in range(n)]
        adj = [[] for _ in range(n)]
        for a, b in edges:
            graph[a][b] = graph[b][a] = 1
            adj[a].append(b)
            adj[b].append(a)

        def bfs(u: int, v: int) -> int:
            if u == v: return 0
            seen = set([u])
            que = [(u, 0)]
            while que:
                cur, dist = que.pop()
                if cur == v: return dist
                for nxt in adj[cur]:
                    if nxt not in seen:
                        que.append((nxt, dist + 1))
                        seen.add(nxt)
            return -1

        for i in range(n - 1):
            for j in range(i + 1, n):
                if graph[i][j] == 0: graph[i][j] = graph[j][i] = bfs(i, j)

        return [sum(row) for row in graph]

class Solution_v2:     ### Time Limit Exceeded     64 / 73 testcases passed
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[0 for _ in range(n)] for _ in range(n)]
        adj = [[] for _ in range(n)]
        for a, b in edges:
            graph[a][b] = graph[b][a] = 1
            adj[a].append(b)
            adj[b].append(a)

        def bfs(u: int, v: int) -> int:
            if u == v: return 0
            seen = set([u])
            que = [(u, 0)]
            while que:
                cur, dist = que.pop()
                if cur == v: return dist
                for nxt in adj[cur]:
                    if nxt not in seen:
                        que.append((nxt, dist + 1))
                        if graph[u][nxt] == 0:
                            graph[u][nxt] = graph[nxt][u] = dist + 1
                        seen.add(nxt)
            return -1

        for i in range(n - 1):
            for j in range(i + 1, n):
                if graph[i][j] == 0: graph[i][j] = graph[j][i] = bfs(i, j)

        print("Graph:")
        for ele in graph: print(ele)                

        return [sum(row) for row in graph]

class Solution_v3:      ### YouTuber: Timothy Chang     O(n^2)
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)
        
        def travel(i):
            visited = set([i])
            que = collections.deque([(i, 0)])
            output = 0
            while que:
                cur, dis = que.popleft()
                for nxt in graph[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        que.append((nxt, dis + 1))
                        output += (dis + 1)
            return output
        return [travel(i) for i in range(n)]

class Solution_v4:      ### YouTuber: Timothy Chang     O(n)
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)

        output = [0] * n
        count = [1] * n
        self.root = 0

        def dfs(cur, parent, depth):
            op = 1
            for child in graph[cur]:
                if child != parent:
                    op += dfs(child, cur, depth + 1)
                    self.root += (depth + 1)
            count[cur] = op
            return op
        dfs(0, -1, 0)

        def dfs2(cur, parent, ans_p):
            output[cur] = ans_p
            for child in graph[cur]:
                if child != parent:
                    dfs2(child, cur, ans_p + (n - count[child]) - count[child])
        dfs2(0, -1, self.root)

        return output

class Solution_v5(object):      ### YouTuber: happygirlzt     O(n)     Re-root Solution
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        count = [0 for _ in range(n)]
        res = [0 for _ in range(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs (root: int, prev: int):
            for neigh in graph[root]:
                if neigh == prev: continue
                dfs(neigh, root)
                res[root] += res[neigh] + count[neigh]
                count[root] += count[neigh]
            count[root] += 1

        def dfs2 (root: int, prev: int):
            for neigh in graph[root]:
                if neigh == prev: continue
                res[neigh] = res[root] - count[neigh] + len(count) - count[neigh]
                dfs2(neigh, root)

        dfs(0, -1)
        dfs2(0, -1)
        return res


# class Solution_v5(object):      ### YouTuber: Huifeng Guan     O(n)     Re-root Solution
    ''' Re-root
        f(child) --> f(parent) + a - b
        b = subtree_size(child)
        a = n - b

        f(child) = f(parent) + n - 2 * subtree_size(child)

        We gonna use three time recursion to solve this problem
        0 pick up a root
        1 subtree_size of every node
        2 distance sum towards root => f(root)
        3 f(node)
    '''


def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()
    sol = Solution_v4()
    sol = Solution_v5()


    n, edges = 6, [[0,1],[0,2],[2,3],[2,4],[2,5]]  # Output: [8,12,6,10,10,10]
    print(sol.sumOfDistancesInTree(n, edges))

    n, edges = 1, []   # Output: [0]
    print(sol.sumOfDistancesInTree(n, edges))

    n, edges = 2, [[1,0]]  # Output: [1,1]
    print(sol.sumOfDistancesInTree(n, edges))


if __name__ == "__main__":
    main()
