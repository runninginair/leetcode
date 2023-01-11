''' 96. Unique Binary Search Trees
Medium      8178        321     Add to List     Share
Given an integer n, return the number of structurally unique BST's
(binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1
 
Constraints:    1 <= n <= 19

'''

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            temp = 0
            for j in range(1, i + 1):
                temp += dp[j-1]*dp[i-j]
            dp[i] = temp
        return dp[n]


def main():
    sol = Solution()
    for i in range(1, 20):
        print(sol.numTrees(i), end=", ")


main()
