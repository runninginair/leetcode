''' 1547. Minimum Cost to Cut a Stick

Hard        3.2K        65          Companies

Given a wooden stick of length n units. The stick is labelled from 0 to n. 
For example, a stick of length 6 is labelled as follows:

    |----|----|----|----|----|----|
    0    1    2    3    4    5    6

Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of
costs of all cuts. When you cut a stick, it will be split into two smaller sticks
(i.e. the sum of their lengths is the length of the stick before the cut).
Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts.


Example 1:

    cut = [3, 5, 1, 4]  Optimal Ordering

    |---|---|---|---|---|---|---|                cut 3, cost = 7
    0   1   2   3   4   5   6   7

    |---|---|---|   |---|---|---|---|            cut 5, cost += (7-3) => cost = 11
    0   1   2   3   3   4   5   6   7

    |---|---|---|   |---|---|   |---|---|        cut 1, cost += (3-0) => cost = 14
    0   1   2   3   3   4   5   5   6   7
    
    |---|   |---|---|   |---|---|   |---|---|    cut 4, cost += (5-3) => cost = 16
    0   1   1   2   3   3   4   5   5   6   7

    |---|   |---|---|   |---|   |---|   |---|---|       return cost = 16
    0   1   1   2   3   3   4   4   5   5   6   7    
    
    cut = [4, 5, 1, 3] -> 7 + 3 + 4 + 3

Input: n = 7, cuts = [1,3,4,5]
Output: 16
Explanation: Using cuts order = [1, 3, 4, 5] as in the input leads to the following
scenario:

The first cut is done to a rod of length 7 so the cost is 7. 
The second cut is done to a rod of length 6 (i.e. the second part of the first cut), 
the third is done to a rod of length 4 and the last cut is to a rod of length 3. 
The total cost is 7 + 6 + 4 + 3 = 20.

Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with
total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).


Example 2:

Input: n = 9, cuts = [5,6,1,4,2]
Output: 22
Explanation: If you try the given cuts ordering the cost will be 25.
There are much ordering with total cost <= 25, for example,
the order [4, 6, 5, 2, 1] has total cost = 22 which is the minimum possible.
 

Constraints:        2 <= n <= 10^6
                    1 <= cuts.length <= min(n - 1, 100)
                    1 <= cuts[i] <= n - 1
                    All the integers in cuts array are distinct.
Accepted:           68.7K
Submissions:        112.4K
Acceptance Rate:    61.1%

'''

from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

    # def _minCost()

    #     start, end = 0, n
    #     if len(cuts) > 0: cost += end - start
    #     mid = (start + end) / 2

    #     nxtCut = 
        return -1
    

def main():
    sol = Solution()

    n, cuts = 7, [1,3,4,5]     # Output: 16
    print(sol.minCost(n, cuts))

    n, cuts = 9, [5,6,1,4,2]   # Output: 22
    print(sol.minCost(n, cuts))



if __name__ == "__main__":
    main()

