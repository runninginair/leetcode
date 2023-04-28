''' 2492. Minimum Score of a Path Between Two Cities

Medium      356       55        Companies

You are given a positive integer n representing n cities numbered from 1 to n.
You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that
there is a bidirectional road between cities ai and bi with a distance equal to distancei.
The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in
this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

 * A path is a sequence of roads between two cities.

 * It is allowed for a path to contain the same road multiple times, and you can visit
   cities 1 and n multiple times along the path.

 * The test cases are generated such that there is at least one path between 1 and n.
 

Example 1:
Input: n = 4, roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4.
The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.

Example 2:
Input: n = 4, roads = [[1, 2, 2], [1, 3, 4], [3, 4, 7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4.
The score of this path is min(2,2,4,7) = 2.
 

Constraints:            2 <= n <= 10^5
                        1 <= roads.length <= 10^5
                        roads[i].length == 3
                        1 <= a-i, b-i <= n
                        ai != bi
                        1 <= distancei <= 10^4
                        There are no repeated edges.
                        There is at least one path between 1 and n.
Accepted:               16.4K
Submissions:            34.8K
Acceptance Rate:        47.0%
'''

from typing import List

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.score = {}
    
    def union(self, a, b, dis):
        a, b = self.find(a, dis), self.find(b, dis)
        if a == b: return
        if self.score[a] < self.score[b]:
            self.parent[b], self.score[b] = a, self.score[a]
        else:
            self.parent[a], self.score[a] = b, self.score[b]

    def find(self, x, dis):
        if x not in self.parent:
            self.parent[x], self.score[x] = x, dis
        if x != self.parent[x]:
            min_dis = min(dis, self.score[x], self.score[self.parent[x]])
            self.score[x] = self.score[self.parent[x]] = min_dis
            self.parent[x] = self.find(self.parent[x], min_dis)
        return self.parent[x]

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind()
        for i, j, dis in roads: uf.union(i, j, dis)
        x = 1
        while x != uf.parent[x]: x = uf.parent[x]
        return uf.score[x]

        
class UnionFind_v2:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: return
        if self.rank[a] == self.rank[b]: self.rank[a] += 1
        elif self.rank[b] > self.rank[a]: a, b = b, a
        self.parent[b] = a

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0        
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution_v2:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind_v2()
        ans = float('inf')        
        for a, b, d in roads:
            uf.union(a, b)
        for a, b, d in roads:
            if uf.find(a) == uf.find(1): ans = min(ans, d)
        return ans


def main():
    sol = Solution()
    sol = Solution_v2()

    n, roads = 4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]
    print(sol.minScore(n, roads))  # Output: 5

    n, roads = 4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]
    print(sol.minScore(n, roads))  # Output: 2

    n, roads = 6, [[4,5,7468],[6,2,7173],[6,3,8365],[2,3,7674],[5,6,7852],[1,2,8547],
                   [2,4,1885],[2,5,5192],[1,3,4065],[1,4,7357]]
    print(sol.minScore(n, roads))  # Output: 1885

    n, roads = 20, [[18,20,9207],[14,12,1024],[11,9,3056],[8,19,416],[3,18,5898],[17,3,6779],[13,15,3539],[15,11,1451],[19,2,3805],[9,8,2238],[1,16,618],[16,14,55],[17,7,6903],[12,13,1559],[2,17,3693]]
    print(sol.minScore(n, roads))  # Output: 55


main()
