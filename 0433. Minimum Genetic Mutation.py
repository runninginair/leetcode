''' 433. Minimum Genetic Mutation
Medium      1126      120       Add to List     Share

A gene string can be represented by an 8-character long string, with choices
from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene
string end where one mutation is defined as one single character changed in
the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations.
A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the
minimum number of mutations needed to mutate from start to end. If there is
no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be
included in the bank.


Example 1:
Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:
Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Example 3:
Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
Output: 3
 

Constraints:    start.length == 8
                end.length == 8
                0 <= bank.length <= 10
                bank[i].length == 8
                start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
Accepted:       62,430
Submissions:    129,673
'''

from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end: return 0
        n = len(bank)
        if n == 0 or end not in bank: return -1

        def isValidMutation(a: str, b: str) -> bool:
            diff = 0
            for i in range(8):
                if a[i] != b[i]: diff += 1
            return diff == 1
        
        start_nxt , end_index = [], -1
        g = [[ 0 for _ in range(n)] for _ in range(n)]
        seen = set()
        for nxt in start_nxt: seen.add(nxt)

        ## Find the start's next vertex, and the index of end.
        for i in range(n):
            if bank[i] == end:
                end_index = i
            if isValidMutation(start, bank[i]):
                start_nxt.append(i)
                if i == end_index: return 1

        ### Convert the gene nodes to ajson-matrix
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if isValidMutation(bank[i], bank[j]):
                    g[i][j] = g[j][i] = 1

        path = 0
        ### BFS find the shortest path
        while start_nxt:
            nxt = []
            while start_nxt:
                nxt.append(start_nxt.pop(0))
            path += 1
            for v in nxt:
                if v == end_index: return path
                seen.add(n)
                for k in range(n):
                    if g[v][k] == 1 and k not in seen:
                        start_nxt.append(k)
                        seen.add(k)
        return -1

def main():
    sol = Solution()

    start, end, bank = "AACCGGTT",  "AACCGGTA",  ["AACCGGTA"]   # Output: 1
    print(sol.minMutation(start, end, bank))

    start, end, bank = "AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]   # Output: 2
    print(sol.minMutation(start, end, bank))

    start, end, bank = "AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC"]   # Output: 3
    print(sol.minMutation(start, end, bank))

main()
