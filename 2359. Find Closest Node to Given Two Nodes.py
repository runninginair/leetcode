''' 2359. Find Closest Node to Given Two Nodes

Medium      440     89      Companies

You are given a directed graph of n nodes numbered from 0 to n - 1,
where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n,
indicating that there is a directed edge from node i to node edges[i].
If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2,
such that the maximum between the distance from node1 to that node, and
from node2 to that node is minimized. If there are multiple answers, return
the node with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.


Example 1:
Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation: The distance from node 0 to node 2 is 1,
and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1.
It can be proven that we cannot get a node with a smaller maximum distance
than 1, so we return node 2.

Example 2:
Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
Explanation: The distance from node 0 to node 2 is 2,
and the distance from node 2 to itself is 0.
The maximum of those two distances is 2.
It can be proven that we cannot get a node with a smaller maximum distance
than 2, so we return node 2.
 

Constraints:        n == edges.length
                    2 <= n <= 10^5
                    -1 <= edges[i] < n
                    edges[i] != i
                    0 <= node1, node2 < n
Accepted:           18K
Submissions:        52.3K
Acceptance Rate:    34.4%
'''

from typing import List


class Solution:     ### 62 / 77 testcases passed
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        seen, seen2, hasCircle, n1, n2, cnt = set(), set(), False, node1, node2, 0
        while edges[n1] != -1 and edges[n1] not in seen:
            seen.add(edges[n1])
            if edges[n1] == node1:
                hasCircle = True
                break
            n1 = edges[n1]
        if not hasCircle: seen.add(node1)
        # print(seen, "\n", seen2)
        if n2 in seen:
            if not hasCircle: return n2
            else:
                while edges[n2] != node1:
                    cnt += 1
                    n2 = edges[n2]
                if (cnt == 0 and len(seen) == 2) or cnt * 2 == len(seen): return min(node1, node2)
                return node1 if cnt < len(seen) else node2
        n2 = node2
        if edges[n2] in seen: return edges[n2]
        seen2.add(n2)
        while edges[n2] != -1 and edges[n2] not in seen and edges[n2] not in seen2:
            seen2.add(edges[n2])
            n2 = edges[n2]
        return n2 if n2 in seen else -1


class Solution_v2:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        INF, N = float('inf'), len(edges)
        dist_node1, dist_node2 = [INF for _ in range(N)], [INF for _ in range(N)]

        def dfs(node, di, d):
            if d[node] > di: 
                d[node] = di
                if edges[node] != -1:
                    dfs(edges[node], di+1, d)

        dfs(node1, 0, dist_node1)
        dfs(node2, 0, dist_node2)
        print(dist_node1, "\n", dist_node2)

        for i in range(N): dist_node1[i] = max(dist_node1[i], dist_node2[i])

        ans = dist_node1.index(min(dist_node1))
        return ans if dist_node1[ans] != INF else -1

def main():
    sol = Solution()
    sol = Solution_v2()

    # edges, node1, node2 = [2, 2, 3, -1],  0, 1                      # Expect Output: 2
    # print(sol.closestMeetingNode(edges, node1, node2))

    # edges, node1, node2 = [1, 2, -1], 0, 2                          # Expect Output: 2
    # print(sol.closestMeetingNode(edges, node1, node2))

    # edges, node1, node2 = [5, 3, 1, 0, 2, 4, 5], 3, 2               # Expect Output: 3
    # print(sol.closestMeetingNode(edges, node1, node2))

    # edges, node1, node2 = [4, 3, 0, 5, 3, -1], 4, 0                 # Expect Output: 4
    # print(sol.closestMeetingNode(edges, node1, node2))

    # edges, node1, node2 = [2, 0, 0], 2, 0                           # Expect Output: 0
    # print(sol.closestMeetingNode(edges, node1, node2))

    # edges, node1, node2 = [5, 4, 5, 4, 3, 6, -1], 0, 1              # Expect Output: -1
    # print(sol.closestMeetingNode(edges, node1, node2))

    ### 63 / 77 testcase: 
    edges, node1, node2 = [4, 4, 8, -1, 9, 8, 4, 4, 1, 1], 5, 6     # Expect Output: 1
    print(sol.closestMeetingNode(edges, node1, node2))


if __name__ == "__main__":
    main()
