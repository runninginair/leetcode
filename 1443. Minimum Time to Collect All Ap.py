''' 1443. Minimum Time to Collect All Apples in a Tree

Medium      1.2K      95       Companies

Given an undirected tree consisting of n vertices numbered from 0 to n-1, which
has some apples in their vertices. You spend 1 second to walk over one edge of
the tree. Return the minimum time in seconds you have to spend to collect all
apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where
edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.
Additionally, there is a boolean array hasApple, where hasApple[i] = true means
that vertex i has an apple; otherwise, it does not have any apple.


Example 1:
Input:  n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], 
        hasApple = [false,false,true,false,true,true,false]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have
an apple. One optimal path to collect all apples is shown by the green arrows.  


Example 2:
Input:  n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
        hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have
an apple. One optimal path to collect all apples is shown by the green arrows.  
Example 3:

Input:  n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
        hasApple = [false,false,false,false,false,false,false]
Output: 0


Constraints:        1 <= n <= 10^5
                    edges.length == n - 1
                    edges[i].length == 2
                    0 <= ai < bi <= n - 1
                    fromi < toi
                    hasApple.length == n
Accepted:           33.4K
Submissions:        59.4K
Acceptance Rate:    56.1%
'''

from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node: int, parent: int) -> int:
            totalTime = 0
            for child in adj[node]:
                if child == parent: continue
                childTime = dfs(child, node)
                if hasApple[child] or childTime: totalTime += childTime + 2
            return totalTime
        return dfs(0, -1)

class Solution_v1:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        # for i, ad in enumerate(adj): print(i, ad)
        
        self.cnt = 0

        def dfs(node: int, parent: int) -> int:
            self.cnt += 1
            totalTime = childTime = 0
            # print("\n#", self.cnt * "-", "  node =", node, "  parent =", parent, adj[node])
            for child in adj[node]:
                if child == parent: continue
                childTime = dfs(child, node)
                if childTime or hasApple[child]:
                    # print("@", childTime, hasApple[child])
                    totalTime += childTime + 2
                # print("#", self.cnt * "-", "totalTime =", totalTime, " childTime =", childTime)
            return totalTime

        return dfs(0, -1)


'''     ### LeetCode Official Solution C++
class Solution {
public:
    int dfs(int node, int parent, vector<vector<int>>& adj, vector<bool>& hasApple) {
        int totalTime = 0, childTime = 0;
        for (auto child : adj[node]) {
            if (child == parent) continue;
            childTime = dfs(child, node, adj, hasApple);
            // childTime > 0 indicates subtree of child has apples. Since the root node of the
            // subtree does not contribute to the time, even if it has an apple, we have to check it
            // independently.
            if (childTime || hasApple[child]) totalTime += childTime + 2;
        }

        return totalTime;
    }

    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        vector<vector<int>> adj(n);
        for (auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        return dfs(0, -1, adj, hasApple);
    }
};
'''
class Solution_v0:  
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        return self.dfs(0, -1, adj, hasApple)

    def dfs(self, node, parent, adj, hasApple) -> int:
        totalTime = childTime = 0
        for child in adj[node]:
            if child == parent: continue
            childTime = self.dfs(child, node, adj, hasApple)
            if childTime or hasApple[child]: totalTime += childTime + 2
        return totalTime


def main():
    sol = Solution()
    # sol = Solution_v0()

    n, edges = 7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], 
    hasApple = [False, False, True, False, True, True, False]
    print(sol.minTime(n, edges, hasApple))       # Output: 8

    # n, edges = 7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
    # hasApple = [False, False, True, False, False, True, False]
    # print(sol.minTime(n, edges, hasApple))       # Output: 6

    # n, edges = 7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
    # hasApple = [False, False, False, False, False, False, False]
    # print(sol.minTime(n, edges, hasApple))       # Output: 0

    # n, edges = 4,[[0,1],[1,2],[0,3]]
    # hasApple = [True, True, True, True]
    # print(sol.minTime(n, edges, hasApple))       # Output: 6

    # n, edges = 5, [[0,1],[0,2],[1,3],[0,4]]
    # hasApple = [False, False, False, True, False]   
    # print(sol.minTime(n, edges, hasApple))       # Output: 4


if __name__ == "__main__":
    main()
