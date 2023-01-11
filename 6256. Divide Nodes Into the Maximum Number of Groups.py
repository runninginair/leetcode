''' 6256. Divide Nodes Into the Maximum Number of Groups

Weekly Contest 323      Problem #4      2022/12/03

User Accepted:122       User Tried:370      Total Accepted:125      Total Submissions:623
Difficulty:Hard

You are given a positive integer n representing the number of nodes in an
undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi]
indicates that there is a bidirectional edge between nodes ai and bi.
Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

 *  Each node in the graph belongs to exactly one group.
 *  For every pair of nodes in the graph that are connected by an edge [ai, bi],
    if ai belongs to the group with index x, and bi belongs to the group with
    index y, then |y - x| = 1.

Return the maximum number of groups (i.e., maximum m) into which you can divide
the nodes.
Return -1 if it is impossible to group the nodes with the given conditions.



Example 1:     (5) -- (1) -- (2) -- (3)
                          \      \
                           \      \         ==>     [(5), (1), (2, 4), (3, 6)]
                            (4) -- (6)
Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
Output: 4
Explanation: As shown in the image we:
- Add node 5 to the first group.
- Add node 1 to the second group.
- Add nodes 2 and 4 to the third group.
- Add nodes 3 and 6 to the fourth group.
We can see that every edge is satisfied.
It can be shown that that if we create a fifth group and move any node from the
third or fourth group to it, at least on of the edges will not be satisfied.


Example 2:       (1) ----- (2)
                     \   /
                      (3)
Input: n = 3, edges = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: If we add node 1 to the first group, node 2 to the second group,
and node 3 to the third group to satisfy the first two edges, we can see that
the third edge will not be satisfied.
It can be shown that no grouping is possible.
 

Constraints:    1 <= n <= 500
                1 <= edges.length <= 10^4
                edges[i].length == 2
                1 <= ai, bi <= n
                ai != bi
                There is at most one edge between any pair of vertices.
'''


from collections import defaultdict, deque
import collections
from typing import List


# class Solution:
#     def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
#         ### Write your code here
#
#         return -1

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):      # merge means union here.
        self.parent[self.find(b)] = self.find(a)

    ### __str__ being used to show object and test.
    def __str__(self) -> str:
        return str(self.parent)

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        path = defaultdict(list)
        union = UnionFind(n + 1)
        print("# 1", union, end="\n\n")
        for x, y in edges:
            union.merge(x, y)
            path[x].append(y)
            path[y].append(x)
        print("# 2", union, end="\n\n")
        for key in path: print(key, ":", path[key])
        
        ans = [-1] * (n + 1)
        for i in range(1, n + 1):
            if ans[i] == -1:
                ans[i] = 0
                q = deque([i])
                while q:
                    p = q.popleft()
                    for newp in path[p]:
                        if ans[newp] == -1:
                            ans[newp] = 1 - ans[p]
                            q.append(newp)
                        elif ans[newp] + ans[p] != 1: return -1
        
        visited = defaultdict(int)
        for i in range(1, n + 1):
            ans[i] = 0
            q = deque([i])
            v = {i}
            cnt = 0
            while q:
                cnt += 1
                for _ in range(len(q)):
                    p = q.popleft()
                    for newp in path[p]:
                        if newp not in v:
                            v.add(newp)
                            q.append(newp)
            visited[union.find(i)] = max(visited[union.find(i)], cnt)

        return sum(visited.values())


class Solution_v2(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        e = [(u -1, v - 1) for u, v in edges]
        
        adj = [[] for _ in range(n)]
        for u, v in e:
            adj[u].append(v)
            adj[v].append(u)
            
        best = [0] * n
        bad = False
        
        for i in range(n):
            curr = [-1] * n
            curr[i] = 0
            up = [i]
            it = 0
            while up:
                nex = []
                it += 1
                for u in up:
                    assert curr[u] == it - 1
                    for v in adj[u]:
                        if curr[v] == it - 1:
                            bad = True
                        elif curr[v] == -1:
                            curr[v] = it
                            nex.append(v)
                up = nex
            val = max(curr) + 1
            for i in range(n):
                if curr[i] != -1:
                    best[i] = max(best[i], val)
                    break
        if bad:
            return -1
        return sum(best)


class Solution_v3:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        d = list(range(n+1))
        
        def find(a):
            nonlocal d
            if d[a] == a:
                return a
            d[a] = find(d[a])
            return d[a]
        
        gr = [[] for i in range(n+1)]
        
        for a,b in edges:
            d[find(a)] = find(b)
            gr[a].append(b)
            gr[b].append(a)
        
        zr = [-1] * (n+1)
        
        for i in range(1, n+1):
            vis = [0] *(n+1)
            candi = [i]
            
            vis[i] = 1
            h= 0
            ok = True
            while ok and h<len(candi):
                u = candi[h]
                h += 1
                for v in gr[u]:
                    if vis[v] >0:
                        if abs(vis[v] - vis[u])!=1:
                            ok = False
                            break
                    else:
                        vis[v] = vis[u] + 1
                        candi.append(v)
            if ok:
                zr[find(i)] = max(zr[find(i)], vis[candi[-1]])
        r = 0
        for i in range(1,n+1):
            if i!= find(i):
                continue
            if zr[i] <0:
                return -1
            r += zr[i]
        return r


class Solution_v4:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = [set() for _ in range(n + 1)]
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        visited = set()
        res = 0
        color = {}
        for i in range(1, n + 1):
            if i not in visited:
                cur = self.bfs(i, visited, color, g)
                if cur == []:
                    return -1
                tmp = 0
                for start in cur:
                    tmp = max(tmp, self.bfs2(start, g))
                res += tmp
        return res
    def bfs2(self, start, g):
        visited = set([start])
        eq = collections.deque([start])
        res = 0
        while eq:
            res += 1
            for _ in range(len(eq)):
                cur = eq.popleft()
                for v in g[cur]:
                    if v not in visited:
                        visited.add(v)
                        eq.append(v)
        return res
    def bfs(self, start, visited, color, g):
        visited.add(start)
        color[start] = 0
        eq = collections.deque([start])
        res = [start]
        while eq:
            # res += 1
            for _ in range(len(eq)):
                cur = eq.popleft()
                curcolor = color[cur]
                for v in g[cur]:
                    if v not in visited:
                        visited.add(v)
                        color[v] = (1 ^ curcolor)
                        eq.append(v)
                        res.append(v)
                    else:
                        if color[v] != (1 ^ curcolor):
                            return []
        return res

''' Java Solution

class Solution {
public:
    int magnificentSets(int n, vector<vector<int>>& edges) {
        vector<vector<int>>g(n+5);
        for(auto&e:edges){
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        vector<int>dis(n+5,n+5);
        queue<int>q;
        vector<int>s(n+5,0);
        for(int i=1;i<=n;++i){
            q.push(i);
            fill(dis.begin(),dis.end(),n+5);
            dis[i]=0;
            int mx=0,mi=i;
            while(!q.empty()){
                int x=q.front();q.pop();
                for(int v:g[x])if(dis[v]==n+5){
                    dis[v]=dis[x]+1;
                    mx=max(mx,dis[v]);
                    mi=min(mi,v);
                    q.push(v);
                }else if(dis[v]%2!=(dis[x]+1)%2){
                    return -1;
                }
            }
            // cout<<i<<" "<<mi<<" "<<mx<<endl;
            s[mi]=max(s[mi],mx+1);
        }
        int ans=0;
        for(int i=1;i<=n;++i){
            ans+=s[i];
        }
        return ans;
    }
};

'''


def test():
    sol = Solution()
    n, edges = 6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
    print(sol.magnificentSets(n, edges), end="\n\n")

    n, edges = 3, [[1,2],[2,3],[3,1]]
    print(sol.magnificentSets(n, edges), end="\n\n")

    n, edges = 4, [[1,2],[2,3],[3,4],[4,1]]
    print(sol.magnificentSets(n, edges), end="\n\n")

    n, edges = 5, [[1,2],[2,3],[3,4],[4,5],[5,1]]
    print(sol.magnificentSets(n, edges), end="\n\n")

if __name__ == "__main__":
    test()
