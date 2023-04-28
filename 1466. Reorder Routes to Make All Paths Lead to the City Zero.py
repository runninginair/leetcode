''' 1466. Reorder Routes to Make All Paths Lead to the City Zero

Medium      2.2K      53        Companies

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is
only one way to travel between two different cities (this network form a tree).
Last year, The ministry of transport decided to orient the roads in one
direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents
a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people
want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the
city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.


Example 1:      (2) --> (3) <-- (1) <-- (0) <-- (4) --> (5)

                             1       2               3
                (2) --> (3) --> (1) --> (0) <-- (4) <-- (5)

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can
reach the node 0 (capital).


Example 2:      (0) <-- (1) --> (2) <-- (3) --> (4)

                     1               2
                (0) <-- (1) <-- (2) <-- (3) <-- (4)

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can
reach the node 0 (capital).


Example 3:      (1) --> (0) <-- (2)

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0


Constraints:            2 <= n <= 5 * 10^4
                        connections.length == n - 1
                        connections[i].length == 2
                        0 <= ai, bi <= n - 1
                        ai != bi
Accepted:               75.6K
Submissions:            122.4K
Acceptance Rate:        61.8%
'''

from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjList = [[] for _ in range(n + 1)]
        que, reorienting = [0], 0
        connected = set(que)

        for s, t in connections: 
            adjList[s].append(-t)
            adjList[t].append(s)        
        # for city, nei in enumerate(adjList): print(city, nei)
        while que:
            city = que.pop()
            for nei in adjList[city]:
                if abs(nei) not in connected:
                    if nei < 0:
                        reorienting += 1
                        nei = -nei
                    connected.add(nei)
                    que.append(nei)

        return reorienting

            
def main():
    sol = Solution()

    n, connections = 6, [[0,1],[1,3],[2,3],[4,0],[4,5]]  # Output: 3
    print(sol.minReorder(n, connections))

    n, connections = 5, [[1,0],[1,2],[3,2],[3,4]]        # Output: 2
    print(sol.minReorder(n, connections))

    n, connections = 3, [[1,0],[2,0]]  # Output: 0
    print(sol.minReorder(n, connections))


if __name__ == "__main__":
    main()
