''' 1976. Number of Ways to Arrive at Destination

Medium      1.5K       48       Companies

You are in a city that consists of n intersections numbered from 0 to n - 1 with
bi-directional roads between some intersections. The inputs are generated such
that you can reach any intersection from any other intersection and that there
is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = 
[ui, vi, timei] means that there is a road between intersections ui and vi that
takes timei minutes to travel. You want to know in how many ways you can travel
from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest
amount of time. Since the answer may be large, return it modulo 10^9 + 7.


Example 1:
Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

Example 2:
Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
 

Constraints:        1 <= n <= 200
                    n - 1 <= roads.length <= n * (n - 1) / 2
                    roads[i].length == 3
                    0 <= ui, vi <= n - 1
                    1 <= timei <= 10^9
                    ui != vi
                    There is at most one road connecting any two intersections.
                    You can reach any intersection from any other intersection.
Accepted:           24K
Submissions:        75.1K
Acceptance Rate:    31.9%
'''

import collections, heapq, math
from typing import List


class Solution:     ### Brute Force -- Time Limit Exceeded     15 / 54 testcases passed
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        self.dist = float('inf')
        self.num_way = 0
        ajl = [[] for _ in range(n)]
        for road in roads:
            ajl[road[0]].append([road[1], road[2]])
            ajl[road[1]].append([road[0], road[2]])

        def dfs(curr, ajl, path: int, visited) -> None:
            visited.add(curr[0])
            path += curr[1]
            if curr[0] == n - 1:
                if path < self.dist:
                    self.dist = path
                    self.num_way = 1
                elif path == self.dist:
                    self.num_way += 1
            for vertex in ajl[curr[0]]:
                if vertex[0] not in visited and path <= self.dist: dfs(vertex, ajl, path, visited)
            visited.remove(curr[0])

        dfs([0, 0], ajl, 0, set())
        return self.num_way % 1000000007

class Solution_v2:      ### Brute Force -- Time Limit Exceeded     16 / 54 testcases passed
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[0 for column  in range(n)] for row in range(n)]
        for u, v, dis in roads: graph[u][v] = graph[v][u] = dis
        # for gra in graph: print(gra)

        ### Find the shortest path from 0 to n-1
        def dijkstra(graph, start: int) -> int:
            start = 0
            visited = [False for _ in range(n)]
            weights = [math.inf for _ in range(n)]
            path = [None for _ in range(n)]
            queue = []
            weights[start] = 0
            heapq.heappush(queue, (0, start))

            while len(queue) > 0:
                g, u = heapq.heappop(queue)
                visited[u] = True
                for i, w in enumerate(graph[u]):
                    if graph[u][i] != 0 and not visited[i]:
                        f = g + w
                        if f < weights[i]:
                            weights[i] = f
                            path[i] = u
                            heapq.heappush(queue, (f, i))
            # print(path, weights)
            # return path, weights
            return weights[n - 1]
        
        shortest_path = dijkstra(graph, 0)

        self.num_way = 0
        def dfs(curr: int, weight: int, path: int, visited) -> None:
            visited.add(curr)
            path += weight
            # if path > shortest_path: return
            if curr == n - 1:
                if path == shortest_path: self.num_way += 1
            for i, weight in enumerate(graph[curr]):
                if weight != 0 and i not in visited and path + weight <= shortest_path:
                    dfs(i, weight, path, visited)
                # if vertex[0] not in visited and path <= self.dist: dfs(vertex, ajl, path, visited)
            visited.remove(curr)

        dfs(0, 0, 0, set())
        return self.num_way % 1000000007

class Solution_v3:      ### LeetCode ID: DBabichev  
    '''
    The idea of this problem is to use Dijkstra algorithm, but also we need to
    keep not only distances to nodes, but counts as well.

    If we meet candidate == dist[neib], it means we found one more way to reach
    node with minimal cost.
    If candidate < dist[neib], it means that we found better candidate, so we
    update distance and put cnt[neib] = cnt[idx].

    Complexity: It is O((E+V) log V) for time as classical Dijkstra and O(E+V) for space
    '''
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        G = collections.defaultdict(list)
        for x, y, w in roads:
            G[x].append((y, w))
            G[y].append((x, w))
        for key in G: print(key, G[key])
        print("----------------")

        dist, cnt = [math.inf] * n, [0] * n
        start, dist[0], cnt[0] = 0, 0, 1
        heap = [(dist[0], start)]

        while heap:
            print("\n HEAP:", heap)
            (min_dist, idx) = heapq.heappop(heap)
            if idx == n - 1:
                print("RETURN:", dist, cnt, heap)
                return cnt[idx] % (10 ** 9 + 7)
            for neib, weight in G[idx]:
                cost = min_dist + weight
                print("# 0:", " neib =", neib, " weight", weight, " cost = ", cost, " min_dist", min_dist)
                if cost == dist[neib]:               
                    cnt[neib] += cnt[idx]
                    print("  # 1:", "cost =", cost, cnt[neib], cnt[idx])

                elif cost < dist[neib]:
                    print("  # 2 - 1:", cost, dist[neib], heap )
                    dist[neib] = cost
                    heapq.heappush(heap, (cost, neib))
                    print("  # 2 - 2:", cost, dist[neib], heap, cnt[neib], cnt[idx] )
                    cnt[neib] = cnt[idx]
                
class Solution_v4:      ### Adjson Matrix Graph 
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[0 for col in range(n)] for row in range(n)]
        for x, y, dist in roads: graph[x][y] = graph[y][x] = dist
        # for i, row in enumerate(graph): print(i, row)
        dists, counts = [math.inf for _ in range(n)], [0 for _ in range(n)]
        start, dists[0], counts[0] = 0, 0, 1
        heap = [(dists[0], start)]

        while heap:
            min_dis, cur = heapq.heappop(heap)
            if cur == n - 1: return counts[cur] % 1000000007
            for idx in range(n):
                if graph[cur][idx] > 0:
                    cost = min_dis + graph[cur][idx]
                    if cost == dists[idx]:
                        counts[idx] += counts[cur]
                    elif cost < dists[idx]:
                        dists[idx] = cost
                        counts[idx] = counts[cur]
                        heapq.heappush(heap, (cost, idx))
        return -1

def main():
    # sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()
    sol = Solution_v4()

    n, roads = 7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    print(sol.countPaths(n, roads))     # Output: 4

    n, roads = 2, [[1,0,10]]
    print(sol.countPaths(n, roads))     # Output: 1

    n, roads = 29, [[1,0,7443],[2,1,9509],[3,2,8933],[4,3,2714],[2,4,11647],[3,5,8349],[5,0,34234],[6,4,584],[0,6,29183],[3,6,3298],[6,2,12231],[1,6,21740],[3,7,2990],[5,8,7837],[1,8,34628],[6,8,12888],[0,8,42071],[9,8,1650],[4,9,15122],[9,7,14846],[9,5,9487],[9,1,36278],[6,9,14538],[9,3,17836],[1,10,23672],[10,7,2240],[10,4,2516],[7,11,20638],[10,11,18398],[4,11,20914],[11,9,5792],[11,2,32561],[3,11,23628],[1,11,42070],[8,11,7442],[5,11,15279],[11,6,20330],[12,0,54359],[12,2,37407],[12,8,12288],[12,4,25760],[12,10,23244],[11,12,4846],[9,12,10638],[13,5,21367],[13,1,48158],[11,13,6088],[13,2,38649],[9,13,11880],[7,13,26726],[13,4,27002],[13,3,29716],[6,13,26418],[8,13,13530],[13,12,1242],[13,0,55601],[13,10,24486],[14,3,32382],[14,11,8754],[14,7,29392],[8,14,16196],[15,11,7583],[10,15,25981],[14,16,8258],[16,3,40640],[10,16,35410],[16,12,12166],[8,16,24454],[16,4,37926],[5,16,32291],[16,2,49573],[9,17,30859],[17,13,18979],[3,17,48695],[17,11,25067],[17,16,8055],[17,10,43465],[17,8,32509],[5,17,40346],[1,17,67137],[4,17,45981],[15,17,17484],[17,6,45397],[18,15,1705],[10,18,27686],[4,18,30202],[18,6,29618],[18,9,15080],[19,0,67141],[18,19,8340],[7,19,38266],[19,2,50189],[9,20,37879],[4,20,53001],[18,20,22799],[20,14,23333],[17,20,7020],[0,20,81600],[20,12,27241],[20,13,25999],[3,20,55715],[2,20,64648],[11,21,34704],[13,21,28616],[20,21,2617],[7,21,55342],[21,17,9637],[21,4,55618],[21,0,84217],[21,12,29858],[2,21,67265],[21,9,40496],[21,5,49983],[16,21,17692],[21,6,55034],[21,3,58332],[15,21,27121],[8,21,42146],[10,21,53102],[21,19,17076],[22,5,52055],[1,22,78846],[8,22,44218],[22,0,86289],[2,22,69337],[16,22,19764],[12,22,31930],[22,11,36776],[10,22,55174],[14,22,28022],[3,22,60404],[22,20,4689],[22,6,57106],[15,22,29193],[8,23,53441],[23,1,88069],[23,19,28371],[23,22,9223],[14,23,37245],[6,23,66329],[7,23,66637],[0,23,95512],[5,23,61278],[23,18,36711],[23,20,13912],[23,15,38416],[3,23,69627],[23,13,39911],[9,23,51791],[24,23,2196],[24,4,69109],[24,14,39441],[24,1,90265],[24,22,11419],[3,24,71823],[20,25,18955],[25,8,58484],[4,25,71956],[13,25,44954],[25,24,2847],[25,21,16338],[25,7,71680],[3,25,74670],[12,25,46196],[25,10,69440],[25,23,5043],[25,1,93112],[25,9,56834],[19,25,33414],[25,22,14266],[18,25,41754],[25,15,43459],[2,25,83603],[6,25,71372],[11,25,51042],[26,22,17573],[26,0,103862],[26,7,74987],[26,3,77977],[21,26,19645],[26,12,49503],[25,26,3307],[8,26,61791],[26,18,45061],[24,26,6154],[26,5,69628],[16,26,37337],[26,10,72747],[26,1,96419],[26,13,48261],[6,26,74679],[26,15,46766],[9,26,60141],[14,26,45595],[17,26,29282],[26,20,22262],[23,26,8350],[4,26,75263],[26,19,36721],[26,2,86910],[27,25,4616],[27,8,63100],[27,24,7463],[15,27,48075],[14,27,46904],[27,3,79286],[27,2,88219],[28,1,103845],[28,25,10733],[16,28,44763],[28,3,85403],[28,14,53021],[7,28,82413],[27,28,6117],[15,28,54192],[28,5,77054],[6,28,82105],[28,8,69217],[24,28,13580],[2,28,94336],[10,28,80173],[28,26,7426],[28,22,24999],[28,11,61775],[28,19,44147],[28,23,15776],[28,12,56929],[28,13,55687],[4,28,82689]]
    print(sol.countPaths(n, roads))     # Output: 66275


if __name__ == "__main__":
    main()
