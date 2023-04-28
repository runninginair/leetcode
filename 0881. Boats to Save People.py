''' 881. Boats to Save People

Medium      4.8K      115       Companies

You are given an array people where people[i] is the weight of the ith person,
and an infinite number of boats where each boat can carry a maximum weight of
limit. Each boat carries at most two people at the same time, provided the sum
of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.


Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
 

Constraints:        1 <= people.length <= 5 * 10^4
                    1 <= people[i] <= limit <= 3 * 10^4
Accepted:           219.2K
Submissions:        398.6K
Acceptance Rate:    55.0%

'''

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        l, r = 0, len(people) - 1
        if people[0] * 2 > limit: return r + 1
        while l <= r:
            if people[l] + people[r] <= limit: l += 1
            r -= 1
            boat += 1
        return boat

class Solution_v2:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat, l, r  = 0, 0, len(people) - 1
        while l <= r:
            if people[l] <= limit - people[r]: l += 1
            r -= 1
            boat += 1
        return boat

class Solution_v3:      ### 2ND WAY WITHOUT SORTING     From Leetcode official Solution
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        B = [0] * (limit+1)
        for p in people:
            B[p] += 1
        bo, s, e = B[limit], 1, limit-1
        while s <= e:
            while s <= e and B[s] <= 0:
                s += 1
            while s <= e and B[e] <= 0:
                e -= 1
            if s > e:
                break
            if s + e <= limit:
                bo += 1
                B[s] -= 1
                B[e] -= 1
            else:
                bo += B[e]
                e -= 1
        return bo

class Solution_v4:      ### 3RD WAY     From Leetcode official Solution
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        min_val = min(people)
        max_val = max(people)
        count = [0] * (max_val - min_val + 1)
        for p in people:
            count[p - min_val] += 1
        l = min_val
        r = max_val
        while l < r:
            if r + l > limit:
                result += count[r - min_val]
                count[r - min_val] = 0
                while l < r and count[r - min_val] == 0:
                    r -= 1
            else:
                min_count = min(count[l - min_val], count[r - min_val])
                count[l - min_val] -= min_count
                count[r - min_val] -= min_count
                result += min_count
                while l < r and count[r - min_val] == 0:
                    r -= 1
                while l < r and count[l - min_val] == 0:
                    l += 1
        if count[l - min_val] > 0:
            d = limit // l
            if d == 1:
                result += count[l - min_val]
            else:
                result += (count[l - min_val] // 2) + (count[l - min_val] % 2)
        return result

def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()
    # sol = Solution_v4()

    people, limit = [1,2], 3
    print(sol.numRescueBoats(people, limit))   # Output: 1

    people, limit = [3,2,2,1], 3
    print(sol.numRescueBoats(people, limit))   # Output: 3

    people, limit = [3,5,3,4], 5
    print(sol.numRescueBoats(people, limit))   # Output: 4


if __name__ == "__main__":
    main()