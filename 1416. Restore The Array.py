''' 1416. Restore The Array

Hard        505         24          Companies

A program was supposed to print an array of integers. The program forgot to
print whitespaces and the array is printed as a string of digits s and all we
know is that all integers in the array were in the range [1, k] and there are
no leading zeros in the array.

Given the string s and the integer k, return the number of the possible arrays
that can be printed as s using the mentioned program.
Since the answer may be very large, return it modulo 10^9 + 7.


Example 1:
Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]


Example 2:
Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all
integer >= 1 and <= 10.


Example 3:
Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317], [131, 7], [13, 17], [1, 317],
[13, 1, 7], [1, 31, 7], [1, 3, 17], [1, 3, 1, 7]
 

Constraints:    1 <= s.length <= 10^5
                s consists of only digits and does not contain leading zeros.
                1 <= k <= 10^9
Accepted:       16.4K
Submissions:    41K
Acceptance Rate:40.0%   2023-04-22
'''


from typing import List

class Solution: ### Brute Force, Time Limit Exceeded, 28/83 testcases passed
    def numberOfArrays(self, s: str, k: int) -> int:
        res = []
        def dfs(s: str, curr: List[int]) -> None:
            n = len(s)
            for i in range(n):
                num = int(s[0:i+1])
                # print("num =", num)
                if num <= k:                
                    if i == n - 1:
                        res.append(curr + [num])
                        return
                    elif (i + 1 < n and s[i + 1] != '0'):
                        curr.append(num)
                        # print(curr)
                        dfs(s[i + 1:],curr)
                        curr.pop()
        dfs(s, [])
        # print(res)
        return len(res) % 1000000007

class Solution_v1: ### Brute Force, Time Limit Exceeded, 28/83 testcases passed
    def numberOfArrays(self, s: str, k: int) -> int:
        self.res = 0
        def dfs(s: str, curr: List[int]) -> None:
            n = len(s)
            for i in range(n):
                num = int(s[0:i+1])
                if num <= k:                
                    if i == n - 1:
                        self.res += 1
                        return
                    elif (i + 1 < n and s[i + 1] != '0'):
                        curr.append(num)
                        dfs(s[i + 1:],curr)
                        curr.pop()
        dfs(s, [])
        return self.res % 1000000007

class Solution_dp:  ### DP Bottom-Up 
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[-1] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == '0': continue
            num = 0
            j = i
            while j < n and int(s[i:j+1]) <= k:
                num += dp[j+1]
                j += 1
            dp[i] = num % (10 ** 9 + 7)
        return dp[0]


def main():
    sol = Solution()
    sol = Solution_v1()
    sol = Solution_dp()

    s, k = "1000", 10000   # Output: 1
    print(sol.numberOfArrays(s, k))

    s, k = "1000", 10      # Output: 0
    print(sol.numberOfArrays(s, k))

    s, k = "1317", 2000    # Output: 8
    print(sol.numberOfArrays(s, k))

    s, k = "12", 2000    # Output:   2
    print(sol.numberOfArrays(s, k))

    s, k = "1317", 30      # Output: 4
    # 1,3,1,7
    # 1,3,17
    # 1,31,7 X
    # 13,1,7
    # 13,17
    print(sol.numberOfArrays(s, k))

    s, k = "13017", 30      # Output: 2
    # 1,30,1,7
    # 1,30,17
    print(sol.numberOfArrays(s, k))

    s, k = "2553462832281151811513004352253111", 456        # Output: 21752500
    print(sol.numberOfArrays(s, k))


if __name__ == "__main__":
    main()
