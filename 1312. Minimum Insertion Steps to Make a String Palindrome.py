''' 1312. Minimum Insertion Steps to Make a String Palindrome

    Hard        3.1K        36          Companies

Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.


Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".


Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

Constraints:        1 <= s.length <= 500
                    s consists of lowercase English letters.
Accepted:           77.9K
Submissions:        117.3K
Acceptance Rate:    66.4%

'''

''' LCS Longest Comman Subsequnce   Top-Down
            l   e   e   t   c   o   d   e
        0   0   0   0   0   0   0   0   0
    e   0   0   1   1   1   1   1   1   1
    d   0   0   1   1   1   1   1   2   2
    o   0   0   1   1   1   1   2   2   2
    c   0   0   1   1   1   2   2   2   2
    t   0   0   1   1   2   2   2   2   2
    e   0   0   1   2   2   2   2   2   3
    e   0   0   1   2   2   2   2   2   3
    l   0   1   1   2   2   2   2   2  [3]
'''

''' LCS Longest Comman Subsequnce   Bottom-Up
        z   j   v   e   i   i   w   v   c
    c                                       0
    v                                       0
    w                                       0
    i                                       0
    i                                       0
    e                                       0
    v                                       0
    j                                       0
    z                                       0
        0   0   0   0   0   0   0   0   0
'''



class Solutiont_NOT_Correct:
    def minInsertions(self, s: str) -> int:
        # if s == s[::-1]: return 0
        n = len(s)
        tail = 0
        p1, p2, offset = 0, n - 1, 0
        while p1 < p2:
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
                offset += 1
            else:
                p1 += 1
                tail += 1
            if p2 - offset == tail: break
        return tail


class Solution_v1_1:
    def minInsertions(self, s: str) -> int:
        ### Step1: Find the length of the LCS of s and reversed s;
        def LCS(s: str, t: str) -> int:   ### Bottom-Up solution
            m, n = len(s), len(t)
            dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if s[i] == t[j]:
                        dp[i][j] = 1 + dp[i + 1][j + 1]
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
            return dp[0][0]
        return len(s) - LCS(s, s[::-1])

class Solution_v1_2:
    def minInsertions(self, s: str) -> int:
        n, t = len(s), s[::-1]
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return n - dp[0][0]

class Solution_v2:    ### DP Top-Down Solution
    def minInsertions(self, s: str) -> int:
        n, t = len(s), s[::-1]
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return n - dp[n][n]

def main():
    sol = Solution_v1_1()
    sol = Solution_v1_2()
    sol = Solution_v2()

    s = "zzazz"     # Output: 0
    print(sol.minInsertions(s))

    s = "mbadm"     # Output: 2
    print(sol.minInsertions(s))

    s = "leetcode"  # Output: 5
    print(sol.minInsertions(s))

    s = "zjveiiwvc" # Output: 5
    print(sol.minInsertions(s))


if __name__ == "__main__":
    main()
