''' 839. Similar String Groups

Hard    1.2K    184     Companies

Two strings X and Y are similar if we can swap two letters (in different positions) of X,
so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and
"rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.
Notice that "tars" and "arts" are in the same group even though they are not similar.
Formally, each group is such that a word is in the group if and only if it is similar
to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every
other string in strs. How many groups are there?
 

Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2


Example 2:

Input: strs = ["omv","ovm"]
Output: 1
 

Constraints:        1 <= strs.length <= 300
                    1 <= strs[i].length <= 300
                    strs[i] consists of lowercase letters only.
                    All words in strs have the same length and are anagrams of each other.
Accepted:           70.9K
Submissions:        143.8K
Acceptance Rate:    49.3%
'''

import collections
from typing import List

class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0 for _ in range(n)]
        self.count = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y: return
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] == root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        self.count -= 1


class Solution_UnionFind:
    def numSimilarGroups(self, strs: List[str]) -> int:
        ### s1 and s2 have the same length and are anagrams of each other.
        def isSimilarAnagrams(s1: str, s2: str) -> bool:
            cntDiff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]: cntDiff += 1
            return cntDiff <= 2
        n = len(strs)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i+1, n):
                if isSimilarAnagrams(strs[i], strs[j]):
                    uf.union(i, j)
        return uf.count
    

class Solution_BFS:
    def similar(self, string1: str, string2: str) -> bool:
        count = 0        
        for i in range(len(string2)):
            if string1[i] != string2[i]: count += 1
            if count > 2: return False
        return count == 0 or count == 2
    
    def graph(self, strs):
        n = len(strs)
        group = {string: [] for string in strs}
        for i in range(n):
            for j in range(i+1, n):
                if self.similar(strs[i], strs[j]):
                    group[strs[i]].append(strs[j])
                    group[strs[j]].append(strs[i])
        return group
                
    def bfs(self,visited, node, graph):
        q = collections.deque([node])
        visited.add(node)
        while q:
            curr_node = q.popleft()
            for neighbor in graph[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        
    def numSimilarGroups(self, strs: List[str]) -> int:
        group = self.graph(strs)
        visited = set()
        group_count = 0
        for node in group:
            if node not in visited:
                self.bfs(visited, node, group)
                group_count += 1
        return group_count
        

def main():
    sol = Solution_UnionFind()
    sol = Solution_BFS()

    strs = ["tars","rats","arts","star"]    # Output: 2
    print(sol.numSimilarGroups(strs))

    strs = ["omv","ovm"]    # Output: 1
    print(sol.numSimilarGroups(strs))

if __name__ == "__main__":
    main()
