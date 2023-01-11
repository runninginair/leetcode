''' 547. Number of Provinces
Medium      6408       270      Add to List     Share
There are n cities. Some of them are connected, while some are not. If city a
is connected directly with city b, and city b is connected directly with city c,
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other
cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith
city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.


Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:    1 <= n <= 200
                n == isConnected.length
                n == isConnected[i].length
                isConnected[i][j] is 1 or 0.
                isConnected[i][i] == 1
                isConnected[i][j] == isConnected[j][i]
Accepted:       551,501
Submissions:    871,631

'''

class Solution:
    # def findCircleNum(self, isConnected: List[List[int]]) -> int:
    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected)
        uf = UF(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        s = set(uf.roots)
        # return len(s)
        return len(set([uf.find(root) for root in uf.roots]))

class UF:
    def __init__(self, n):
        self.roots = [x for x in range(n)]
        self.ranks = [0 for _ in range(n)]

    def find(self, x):
        if x != self.roots[x]:
            self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False   # Already unioned.
        if self.ranks[rx] < self.ranks[ry]: self.roots[rx] = ry
        elif self.ranks[rx] > self.ranks[ry]: self.roots[ry] = rx
        else:
            self.roots[ry] = rx
            self.ranks[rx] += 1
        return True

def main():
    sol = Solution()
    g = [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
         [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],
         [0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],
         [0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
         [0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],
         [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
         [0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
         [0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
         [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],
         [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]   ### Output: 3

    print(sol.findCircleNum(g))

main()
