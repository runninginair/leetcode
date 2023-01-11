''' 797. All Paths From Source to Target

Medium      5.4K    127     Companies

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find
all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit
from node i (i.e., there is a directed edge from node i to node graph[i][j]).


Example 1:         (0) ---> (1) ---
                  /                 \
                  \-> (2) --> (3) <-/
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
 

Constraints:        n == graph.length
                    2 <= n <= 15
                    0 <= graph[i][j] < n
                    graph[i][j] != i (i.e., there will be no self-loops).
                    All the elements of graph[i] are unique.
                    The input graph is guaranteed to be a DAG.
Accepted:           364.1K
Submissions:        446.4K
Acceptance Rate:    81.6%
'''

from typing import List
'''
class Solution:   ### Solution for search from all start nodes to all tails.
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n, tails, ans = len(graph), [], []
        s = set([x for x in range (n)])

        for i in range(n):
            if graph[i] == []: tails.append(i)
            else:
                for vertex in graph[i]:
                    if vertex in s: s.remove(vertex)
        heads = list(s)

        def bfs(heads: List[int], trace: List[int]) -> None:
            for v in heads:
                trace.append(v)
                if v in tails: ans.append(trace.copy())
                else: bfs(graph[v], trace)
                trace.remove(v)

        bfs(heads, [])

        return ans
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n, ans = len(graph), []
        def bfs(nodes: List[int], trace: List[int]) -> None:
            for node in nodes:
                trace.append(node)
                if node == n - 1: ans.append(trace.copy())
                else: bfs(graph[node], trace)
                trace.remove(node)
        bfs([0], [])
        return ans

class Solution_v2:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1
        def dfs (node, path, output):
            if node == end:
                output.append(path)
            for nx in graph[node]:
                dfs(nx, path + [nx], output)
        output = []
        dfs(0, [0], output)
        return output

class Solution_v3:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return self.dfs(graph, [], 0, [])

    def dfs(self, graph, path, curr, res):
        path.append(curr)
        if curr == len(graph) - 1: res.append(path.copy())
        for vertex in graph[curr]:
            self.dfs(graph, path, vertex, res)
        path.pop(-1)
        return res

class Solution_v4:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(curr, graph, path, res):
            path.append(curr)
            if curr == len(graph) - 1: res.append(path.copy())
            for vertex in graph[curr]: dfs(vertex, graph, path, res)
            path.pop(-1)
            return res
        return dfs(0, graph, [], [])


def main():
    # sol = Solution()
    # sol = Solution_v2()
    sol = Solution_v4()

    graph = [[1,2],[3],[3],[]]     # Output: [[0,1,3],[0,2,3]]
    print(sol.allPathsSourceTarget(graph))

    graph = [[4,3,1],[3,2,4],[3],[4],[]]    # Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    print(sol.allPathsSourceTarget(graph))

    graph = [[2],[2],[]]        # Expect output: [[0,2]]
    print(sol.allPathsSourceTarget(graph))

    graph = [[4,3,1],[3,2,4],[],[4],[]]    # Expect output: [[0,4],[0,3,4],[0,1,3,4],[0,1,4]]
    print(sol.allPathsSourceTarget(graph))


if __name__ == "__main__":
    main()
