''' 261. Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
'''


class Solution:

    def validTree(self, n, edges):
        if not n:
            return True
        
        adj = { i:[] for i in range(n) }
        for n1, n2, in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        ### Print out adj list:
        for key in adj: print("adj[", key, "] =", adj[key])

        visit = set()
        def dfs(i, prev):
            if i in visit: return False
            else: visit.add(i)
            
            for j in adj[i]:
                if j == prev: continue
                if not dfs(j, i): return False
            return True

        return dfs(0, -1) and n == len(visit)


def main():
    sol = Solution()
    n, edges = 5, [[0, 1], [0, 2], [0, 3], [1, 4]]  # return True
    print(sol.validTree(n, edges))

    n, edges = 5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]] # return false
    print(sol.validTree(n, edges))

main()
