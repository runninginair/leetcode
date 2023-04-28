''' 2300. Successful Pairs of Spells and Potions

Medium      485     14      Companies

You are given two positive integer arrays spells and potions, of length n and m
respectively, where spells[i] represents the strength of the i-th spell and
potions[j] represents the strength of the j-th potion.

You are also given an integer success. A spell and potion pair is considered
successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of
potions that will form a successful pair with the i-th spell.

 

Example 1:
Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.

Example 2:
Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.
 

Constraints:            n == spells.length
                        m == potions.length
                        1 <= n, m <= 10^5
                        1 <= spells[i], potions[i] <= 10^5
                        1 <= success <= 10^10
Accepted:               22.6K
Submissions:            69.5K
Acceptance Rate:        32.6%

'''

from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        ans = [0 for _ in range(n)]
        potions.sort()
        def binSearch(spell):
            start, end = 0, m - 1
            while start <= end:
                mid = (start + end) >> 1
                if spell * potions[mid] < success: start = mid + 1
                else: end = mid - 1
            return m - start

        for i in range(n):
            ans[i] = binSearch(spells[i])
        return ans

class Solution_v2:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        potions.sort()
        def binSearch(spell):
            l, r = 0, m - 1
            while l <= r:
                mid = l + r >> 1
                if spell * potions[mid] < success: l = mid + 1
                else: r = mid - 1
            return m - l

        for i in range(n):
            spells[i] = binSearch(spells[i])
        return spells

def main():
    sol = Solution()
    sol = Solution_v2()

    spells = [5,1,3]
    potions = [1,2,3,4,5]
    success = 7        ### Output: [4,0,3]
    print(sol.successfulPairs(spells, potions, success))

    spells = [3,1,2]
    potions = [8,5,8]
    success = 16        ### Output: [2,0,2]
    print(sol.successfulPairs(spells, potions, success))


if __name__ == "__main__":
    main()
