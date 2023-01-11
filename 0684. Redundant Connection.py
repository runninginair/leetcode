''' 684. Redundant Connection
Medium      4640    325     Add to List     Share

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n,
with one additional edge added. The added edge has two different vertices chosen
from 1 to n, and was not an edge that already existed. The graph is represented
as an array edges of length n where edges[i] = [ai, bi] indicates that there is
an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes.
If there are multiple answers, return the answer that occurs last in the input.


Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 
Constraints:        n == edges.length
                    3 <= n <= 1000
                    edges[i].length == 2
                    1 <= ai < bi <= edges.length
                    ai != bi
                    There are no repeated edges.
                    The given graph is connected.
Accepted:       245,050
Submissions:    395,113
'''

class Solution:
    #def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    def findRedundantConnection(self, edges):
        n = len(edges)
        uf = UF(n + 1)
        for edge in edges:
            join = uf.union(edge[0], edge[1])
            if not join:
                return edge

class UF:
    def __init__(self, n):
        self.parents = [ x for x in range(n + 1)]
        self.ranks = [ 0 for _ in range(n + 1)]

    def find(self, x) -> int:
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            ### print("px =", px, "\t py =", py)
            return False    ### It means x, y are already unioned.
        else:
            if self.ranks[px] < self.ranks[py]: self.parents[px] = py
            elif self.ranks[px] > self.ranks[py]: self.parents[py] = px
            else:
                self.parents[py] = px
                self.ranks[px] += 1
            return True


def main():
    sol = Solution()
    edges = [[1,2],[1,3],[2,3]] # Output: [2,3]
    print(sol.findRedundantConnection(edges))

main()
