''' 904. Fruit Into Baskets

Medium      2K      144     Companies

You are visiting a farm that has a single row of fruit trees arranged from left to right.
The trees are represented by an integer array fruits where fruits[i] is the type of fruit
the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules
that you must follow:

    * You only have two baskets, and each basket can only hold a single type of fruit.
      There is no limit on the amount of fruit each basket can hold.

    * Starting from any tree of your choice, you must pick exactly one fruit from every
      tree (including the start tree) while moving to the right. The picked fruits must
      fit in one of your baskets.

    * Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.


Example 1:

    Input: fruits = [1,2,1]
    Output: 3
    Explanation: We can pick from all 3 trees.

Example 2:

    Input: fruits = [0,1,2,2]
    Output: 3
    Explanation: We can pick from trees [1,2,2].
    If we had started at the first tree, we would only pick from trees [0,1].

Example 3:

    Input: fruits = [1,2,3,2,2]
    Output: 4
    Explanation: We can pick from trees [2,3,2,2].

If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:        1 <= fruits.length <= 105
                    0 <= fruits[i] < fruits.length
Accepted:           256K
Submissions:        600.6K
Acceptance Rate:    42.6%

'''

from typing import List


class Solution:     ### Time Limit Exceeded  T: O(n^2)  71 / 91 testcases passed
    def totalFruit(self, fruits: List[int]) -> int:
        N, res = len(fruits), 1
        if N == 1: return res
        l = m = r = 0
        while l < N and m < N and r < N:
            while m + 1 < N and fruits[m + 1] == fruits[l]: m += 1
            res = max(res, m - l + 1)
            r = m
            while r + 1 < N and (fruits[r + 1] == fruits[l] or fruits[r + 1] == fruits[m + 1]): r += 1
            res = max(res, r - l + 1)
            l = m + 1
        return res

class Solution_v2:     ### Sliding Window  T: O(n)  M: O(1)
    def totalFruit(self, fruits: List[int]) -> int:
        map, res, left = {}, 0, 0

        for f in fruits:
            if f in map:
                map[f] += 1
                res = max(res, sum(map.values()))
            elif len(map) < 2:
                map[f] = 1
                res = max(res, sum(map.values()))
            else:
                map[f] = 1
                while len(map) > 2:
                    map[fruits[left]] -= 1
                    if map[fruits[left]] == 0: del map[fruits[left]]
                    left += 1
        return res

class Solution_v2_2:     ### Sliding Window  T: O(n)  M: O(1)
    def totalFruit(self, fruits: List[int]) -> int:
        map, cur, res, left = {}, 0, 0, 0
        for f in fruits:
            cur += 1            
            if f in map: map[f] += 1
            else:
                map[f] = 1
                while len(map) > 2:
                    map[fruits[left]] -= 1
                    cur -= 1
                    if map[fruits[left]] == 0: del map[fruits[left]]
                    left += 1
            res = max(cur, res)
        return res

class Solution_official:    ### Sliding Window  T: O(n)  M: O(n)
    def totalFruit(self, fruits: List[int]) -> int:
        # Hash map 'basket' to store the types of fruits.
        basket = {}
        left = 0
        
        # Add fruit from the right index (right) of the window.
        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1
            print("# 0 --", basket, right, left)
            # If the current window has more than 2 types of fruit,
            # we remove one fruit from the left index (left) of the window.
            if len(basket) > 2:
                basket[fruits[left]] -= 1
                print("# 1 --", basket, right, left)

                # If the number of fruits[left] is 0, remove it from the basket.
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                    print("# 2 --", basket, right, left)

                left += 1
            print()
        
        # Once we finish the iteration, the indexes left and right 
        # stands for the longest valid subarray we encountered.
        return right - left + 1


def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_official()
    sol = Solution_v2_2()


    ### idx:  0  1  2  3  4  5  6
    fruits = [0, 1, 6, 6, 4, 4, 6]                  ### Expect output: 5
    print(sol.totalFruit(fruits))

    ### idx:  0  1  2  3  4  5  6
    fruits = [0, 1, 6, 6, 4, 4, 6, 11, 12, 13, 14]  ### Expect output: 5
    print(sol.totalFruit(fruits))

    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]      ### Expect output: 5
    print(sol.totalFruit(fruits))


if __name__ == "__main__":
    main()
