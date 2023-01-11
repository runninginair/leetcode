''' 516. Longest Palindromic Subsequence
Medium      6556      266      Add to List      Share

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining elements.


Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 
Constraints:        1 <= s.length <= 1000
                    s consists only of lowercase English letters.
Accepted:       306,751
Submissions:    505,258
'''

class Solution_v1:  ### DP solution
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s: return 0
        N = len(s)
        if N < 2: return N

        dp = [[0 for _ in range(N)] for _ in range(N)]
        # for x in dp: print(x)
        # print("------------")

        for col in range(1, N + 1):
            for row in range(N - col + 1):
                i, j = row, row + col - 1
                # print("Row:=", row, "  Col:", col,"   i =", i, "  j =", j)
                if i == j:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        for x in dp: print(x)
        return dp[0][N - 1]


def main():
    sol = Solution_v1()
    s = "bbbab"     ### Output: 4
    print(sol.longestPalindromeSubseq(s))
    s = "BABCBAB"   ### Output: 7
    print(sol.longestPalindromeSubseq(s))
    s = "cbbd"      ### Output: 2
    print(sol.longestPalindromeSubseq(s))

main()