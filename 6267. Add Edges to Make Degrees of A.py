''' 6267. Add Edges to Make Degrees of All Nodes Even
User Accepted:492
User Tried:1230
Total Accepted:505
Total Submissions:2287
Difficulty:Hard
There is an undirected graph consisting of n nodes numbered from 1 to n. You are given the integer n and a 2D array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi. The graph can be disconnected.

You can add at most two additional edges (possibly none) to this graph so that there are no repeated edges and no self-loops.

Return true if it is possible to make the degree of each node in the graph even, otherwise return false.

The degree of a node is the number of edges connected to it.

 

Example 1:


Input: n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
Output: true
Explanation: The above diagram shows a valid way of adding an edge.
Every node in the resulting graph is connected to an even number of edges.
Example 2:


Input: n = 4, edges = [[1,2],[3,4]]
Output: true
Explanation: The above diagram shows a valid way of adding two edges.
Example 3:


Input: n = 4, edges = [[1,2],[1,3],[1,4]]
Output: false
Explanation: It is not possible to obtain a valid graph with adding at most 2 edges.
 

Constraints:

3 <= n <= 105
2 <= edges.length <= 105
edges[i].length == 2
1 <= ai, bi <= n
ai != bi
There are no repeated edges.

'''

from typing import List


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for _ in range(n)]
        for a, b in edges:
            if b not in adjList[a - 1]: adjList[a - 1].append(b)
            if a not in adjList[b - 1]: adjList[b - 1].append(a)
        oddcounter = 0
        vetex = 1
        for adj in adjList: 
            print(vetex, sorted(adj))
            vetex += 1
        oddvetex = []
        for i, adj in enumerate(adjList):
            if len(adj) & 1:
                if len(adj) == n - 1: return False
                oddvetex.append(i + 1)
                oddcounter += 1
        print(oddvetex)
        
        if oddcounter & 1 or oddcounter > 4: return False
        return True

def main():
    sol = Solution()

    # n, edges = 5, [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
    # print(sol.isPossible(n, edges))     # Output: true

    # n, edges = 4, [[1,2],[3,4]]   
    # print(sol.isPossible(n, edges))     # Output: true

    # n, edges = 4, [[1,2],[1,3],[1,4]]  
    # print(sol.isPossible(n, edges))     # Output: false

    n, edges = 11, [[5,9],[8,1],[2,3],[7,10],[3,6],[6,7],[7,8],[5,1],[5,7],[10,11],[3,7],[6,11],[8,11],[3,4],[8,9],[9,1],[2,10],[9,11],[5,11],[2,5],[8,10],[2,7],[4,1],[3,10],[6,1],[4,9],[4,6],[4,5],[2,4],[2,11],[5,8],[6,9],[4,10],[3,11],[4,7],[3,5],[7,1],[2,9],[6,10],[10,1],[5,6],[3,9],[2,6],[7,9],[4,11],[4,8],[6,8],[3,8],[9,10],[5,10],[2,8],[7,11]]
    print(sol.isPossible(n, edges))     # Output: false

main()
