''' 0319. Bulb Switcher

Medium      1.2K       1.9K         Companies

There are n bulbs that are initially off. You first turn on all the bulbs, 
then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or
turning off if it's on). For the i-th round, you toggle every i bulb.
For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.


Example 1:

Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.


Example 2:

Input: n = 0
Output: 0


Example 3:
Input: n = 1
Output: 1
 

Constraints:        0 <= n <= 10^9
Accepted:           131.7K
Submissions:        271.7K
Acceptance Rate:    48.5%
'''

class Solution_BF:  # T: O(n^2)     M: O(n)
    def bulbSwitch(self, n: int) -> int:
        bulbs = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i, n, i + 1):
                bulbs[j] = -bulbs[j]
        return bulbs.count(1)

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # return int(math.sqrt(n))
        return int(n ** 0.5)

def main():
    sol = Solution()
    res = [[0, 0]]
    for i in range(1, 101):
        curr = sol.bulbSwitch(i) 
        if sol.bulbSwitch(i) != res[-1][1]:
            res.append([i, curr])
    print(res)


if __name__ == "__main__":
    main()
