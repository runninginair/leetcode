''' 2360. Longest Cycle in a Graph

Hard        815         12          Companies

You are given a directed graph of n nodes numbered from 0 to n - 1, where each
node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n,
indicating that there is a directed edge from node i to node edges[i].
If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists,
return -1.

A cycle is a path that starts and ends at the same node.
 
Example 1:                      (0)
                                 ↓
                         (1) -→ (3) ←-- (4)
                                   ↘   ↗
                                    (2)
Input: edges = [3,3,4,2,3]
Output: 3
Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3 ("2" -> "4" -> "3" -> "2"), so 3 is returned.


Example 2:          (0) -→ (2) -→ (3) -→ (1)

Input: edges = [2,-1,3,1]
Output: -1
Explanation: There are no cycles in this graph.
 

Constraints:            n == edges.length
                        2 <= n <= 10^5
                        -1 <= edges[i] < n
                        edges[i] != i
Accepted:               20.9K
Submissions:            51.1K
Acceptance Rate:        40.9%
'''

from typing import List


# class Solution:
#     def longestCycle(self, edges: List[int]) -> int:
#         N = len(edges)
#         adj = [[] for _ in range(N)]
#         for i, x in enumerate(edges):
#             if x == -1: continue
#             adj[x].append(i)
#         for ad in adj: print(ad)



#         return -1


class Solution:     ### Python DFS      LeetCode ID: hqz3
    def longestCycle(self, edges: List[int]) -> int:
        longest = -1
        cycles = set()

        def dfs(current, visited):
            nonlocal start, longest
            if start == current and current in visited:
                cycles.update(visited)
                longest = max(longest, len(visited))
                return

            if current in visited or current in cycles: return
            visited.add(current)

            next_node = edges[current]
            if next_node < 0: return
            return dfs(next_node, visited)

        for i in range(len(edges)):
            start = i
            dfs(i, set())
        
        return longest

def main():
    sol = Solution()

    edges = [3,3,4,2,3]     # Expect Output: 3
    print(sol.longestCycle(edges))

    edges = [2,-1,3,1]      # Expect Output: -1
    print(sol.longestCycle(edges))


if __name__ == "__main__":
    main()
