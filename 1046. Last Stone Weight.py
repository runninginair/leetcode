''' 1046. Last Stone Weight
Easy    3980    76      Add to List     Share

You are given an array of integers stones where stones[i] is the weight of the
i-th stone.

We are playing a game with the stones. On each turn, we choose the heaviest two
stones and smash them together. Suppose the heaviest two stones have weights x
and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has
new weight y - x. At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.


Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1
 
Constraints:        1 <= stones.length <= 30
                    1 <= stones[i] <= 1000
Accepted:       363,883
Submissions:    561,979
'''

import heapq
from typing import List


class Solution: # 02:09pm
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -1 * stone for stone in stones]
        while len(stones) > 1:
            heapq.heapify(stones)
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            diff = a - b
            print(a, b, diff, stones)
            if diff != 0: heapq.heappush(stones, diff)
        return 0 if not stones else -1 * stones[0]

def main():
    sol = Solution()
    stones = [2,7,4,1,8,1]  # Output: 1
    print(sol.lastStoneWeight(stones))

main()
