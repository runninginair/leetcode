''' 60. Permutation Sequence
Hard       5.1k     427       Companies

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following
sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.


Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"

Example 3:
Input: n = 3, k = 1
Output: "123"
 

Constraints:        1 <= n <= 9
                    1 <= k <= n!
Accepted:           309K
Submissions:        703.2K
Acceptance Rate:    43.9%
'''

class Solution:   ### Brute Force -- Backtrack
    def getPermutation(self, n: int, k: int) -> str:
        res, seen = [], set()
        def backTrack(m, n, curr):
            curr.append(m)
            if len(curr) == n:
                res.append(curr.copy())
                return
            seen.add(m)
            for i in range(1, n + 1):
                if i not in seen: backTrack(i, n, curr)
            seen.remove(m)

        for num in range(1, n + 1):
            backTrack(num, n, [])
        return res

class Solution_v0: ### Time Limit Exceeded
    def getPermutation(self, n: int, k: int) -> str:
        def permutation(list):
            res = []
            helper(list, [], res)
            return res
        def helper(list, partial, res):
            if not list: return res.append(partial)
            for i in range(len(list)):
                helper(list[:i] + list[i + 1:], partial + [list[i]], res)
        list = [str(i) for i in range(1, n + 1)]
        res = permutation(list)
        return "".join(res[k - 1])


from itertools import islice, permutations 
class Solution_v1:
    # Get all permutations of length 3 
    def getPermutation(self, n: int, k: int) -> str:
        perm = permutations([x for x in range(1, n + 1)], n)
        res = ""
        # print(type(perm))
        # for p in perm: print(p)
        for i, p in enumerate(perm):
            if i + 1 == k:
                for num in p: res += str(num)
        return res

class Solution_v1_2:
    def getPermutation(self, n: int, k: int) -> str:
        aPerm = next(islice(permutations(range(1, n + 1), n), k-1, k))
        return ''.join(str(x) for x in aPerm)        


class Solution_v2(object):      ### LeetCode ID: ZitaoWang
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1] * n
        digits = [i for i in range(1, 10)]
        for i in range(2, n):
            fact[i] = i * fact[i - 1]
        res = ""
        k -= 1
        for i in range(n - 1, -1, -1):
            q, k = divmod(k, fact[i])
            res += str(digits.pop(q))
        return res    

def main():
    sol = Solution()
    # sol = Solution_v0()
    # sol = Solution_v1()
    # sol = Solution_v1_2()
    # sol = Solution_v2()
    
    print(sol.getPermutation(3, 1))         # Output: "123"    
    # print(sol.getPermutation(3, 3))         # Output: "213"
    print(sol.getPermutation(4, 9))         # Output: "2314"
    # print(sol.getPermutation(9, 273815))    # Output: "783269514"

main()