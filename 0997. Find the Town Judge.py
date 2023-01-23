''' 997. Find the Town Judge

Easy        4.5K        345         Companies

In a town, there are n people labeled from 1 to n.
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

 * 1. The town judge trusts nobody.
 * 2. Everybody (except for the town judge) trusts the town judge.
 * 3. There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that
the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be
identified, or return -1 otherwise.


Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:        1 <= n <= 1000
                    0 <= trust.length <= 10^4
                    trust[i].length == 2
                    All the pairs of trust are unique.
                    ai != bi
                    1 <= ai, bi <= n
Accepted:           341.1K
Submissions:        689.7K
Acceptance Rate:    49.5%
'''

from typing import List
import collections

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        G, judge = [set() for _ in range(n)], -1
        for a, b in trust: G[a - 1].add(b)
        for i in range(n):
            if G[i] == set():
                if judge == -1: judge = i + 1
                else: return -1
        for i in range(n):
            if i + 1 == judge: continue
            if judge not in G[i]: return -1
        return judge

class Solution_v1:      ###  Two Counters
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Count the number of people this guy is being trusted by.
        beingTrustedBy = collections.defaultdict(int)
        # Count the number of people this guy trusts
        trusting = collections.defaultdict(int)

        # Going through the trust relations.
        for a,b in trust:
            trusting[a] += 1
            beingTrustedBy[b] += 1
        
        # The judge trusting 0 people, and being trusted by n-1 people
        for i in range(1, n + 1):
            if beingTrustedBy[i] == n - 1 and trusting[i] == 0: return i
        
        # Didn't find a judge
        return -1

class Solution_V2:     ###  One Counter
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Combine the 2 counters from the previous one 
        # Get the difference between the number of people this guy is trusted by and the number of people this guy trusts.
        diff_between_beingTrustedBy_and_trusting = collections.defaultdict(int)

        # Going through the trust relations.
        for a,b in trust:
            diff_between_beingTrustedBy_and_trusting[a] -= 1
            diff_between_beingTrustedBy_and_trusting[b] += 1

        # The judge trusting 0 people, and being trusted by n-1 people.
        # As a result the judge will have the difference as: n-1-0 == n-1
        for i in range(1,n+1):
            if diff_between_beingTrustedBy_and_trusting[i] == n-1: return i

        # Didn't find a judge
        return -1

class Solution_V2_2:     ###  One Counter
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Combine the 2 counters from the previous one 
        # Get the difference between the number of people this guy is trusted by and the number of people this guy trusts.
        diff_between_beingTrustedBy_and_trusting = [0] * (n + 1)

        # Going through the trust relations.
        for a,b in trust:
            diff_between_beingTrustedBy_and_trusting[a] -= 1
            diff_between_beingTrustedBy_and_trusting[b] += 1

        # The judge trusting 0 people, and being trusted by n-1 people.
        # As a result the judge will have the difference as: n-1-0 == n-1
        for i in range(1, n + 1):
            if diff_between_beingTrustedBy_and_trusting[i] == n-1: return i

        # Didn't find a judge
        return -1


def main():
    sol = Solution()
    sol = Solution_v1()
    sol = Solution_V2()
    sol = Solution_V2_2()


    n, trust = 2, [[1,2]]      # Output: 2
    print(sol.findJudge(n, trust))

    n, trust = 3, [[1,3],[2,3]]       # Output: 3
    print(sol.findJudge(n, trust))

    n, trust = 3, [[1,3],[2,3],[3,1]]      # Output: -1
    print(sol.findJudge(n, trust))



if __name__ == "__main__":
    main()



