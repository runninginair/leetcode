''' 0605. Can Place Flowers

Easy        3.7K        739         Companies

You have a long flowerbed in which some of the plots are planted, and some are
not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty
and 1 means not empty, and an integer n, return if n new flowers can be planted
in the flowerbed without violating the no-adjacent-flowers rule.


Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 
Constraints:        1 <= flowerbed.length <= 2 * 10^4
                    flowerbed[i] is 0 or 1.
                    There are no two adjacent flowers in flowerbed.
                    0 <= n <= flowerbed.length
Accepted:           355.2K
Submissions:        1.1M
Acceptance Rate:    32.6%
'''

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        length = len(flowerbed)
        if length == 1:
            return True if flowerbed[0] == 0 and n == 1 else False
        if n > (length >> 1) + 1: return False
        most = 0
        for i in range(length):
            if i == 0 and flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                most += 1
            elif i == length - 1 and flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                most += 1
            elif flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                most += 1
            if most == n: return True
        return False

class Solution_v2:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        length = len(flowerbed)
        if length == 1:
            return True if flowerbed[0] == 0 and n == 1 else False
        if n > (flowerbed.count(0) >> 1) + 1: return False
        most = 0
        for i in range(length):
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i + 1] == 0:
                    flowerbed[0] = 1
                    most += 1
                elif i == length - 1 and flowerbed[i - 1] == 0:
                    most += 1
                elif 0 == flowerbed[i - 1] == flowerbed[i + 1]:
                    flowerbed[i] = 1
                    most += 1
        return most >= n



def main():
    sol = Solution()
    sol = Solution_v2()

    flowerbed, n = [1,0,0,0,1], 1               # Output: true
    print(sol.canPlaceFlowers(flowerbed, n))

    flowerbed, n = [1,0,0,0,1], 2               # Output: false
    print(sol.canPlaceFlowers(flowerbed, n))

    flowerbed, n = [1,0,0,0,0,1], 2             # Output: false
    print(sol.canPlaceFlowers(flowerbed, n))

    flowerbed, n = [1], 0                       # Output: true
    print(sol.canPlaceFlowers(flowerbed, n))

if __name__ == "__main__":
    main()
