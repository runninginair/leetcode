''' 926. Flip String to Monotone Increasing

Medium      2.7K      112      Companies

A binary string is monotone increasing if it consists of some number of 0's
(possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or
from 1 to 0.

Return the minimum number of flips to make s monotone increasing.


Example 1:
Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.

Example 2:
Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Example 3:
Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.
 

Constraints:        1 <= s.length <= 10^5
                    s[i] is either '0' or '1'.
Accepted:           120K
Submissions:        199.8K
Acceptance Rate:    60.1%

'''

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        one = 0
        zero = res = s.count('0')
        for d in s:
            if d == '0': zero -= 1
            if d == '1': one += 1
            # print("0:", zero, "  1:", one, "  res:", res)
            res = min(res, zero + one)
        return res

class Solution_v2:
    def minFlipsMonoIncr(self, s: str) -> int:
        one = 0
        zero = res = s.count('0')
        for d in s:
            if d == '0': zero -= 1
            if d == '1': one += 1
            res = min(res, zero + one)
            if one == res: break 
        return res

class Solution_v3:
    def minFlipsMonoIncr(self, s: str) -> int:
        cur = res = s.count('0')
        for d in s:
            if d == '0': cur -= 1
            if d == '1': cur += 1
            res = min(res, cur)
        return res

def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()

    ###  s:    "00110"
    ###  zero-> 21110
    ###   one-> 00122
    s = "00110"     # Output: 1
    print(sol.minFlipsMonoIncr(s))

    s = "010110"    # Output: 2
    print(sol.minFlipsMonoIncr(s))

    s = "00011000"  # Output: 2
    print(sol.minFlipsMonoIncr(s))

    s = "11011"      # Output: 1
    print(sol.minFlipsMonoIncr(s))

    s = "1001110010111111101"      # Output: 5  ---- See Demo below,
    print(sol.minFlipsMonoIncr(s))

    ###     s = " 1 0 0 1 1 1 0 0 1 0 1 1 1 1 1 1 1 0 1"      # Output: 5
    ### Zero:6 -> 6 5 4 4 4 4 3 2 2
    ### One: 0 -> 1 1 1 2 3 4 4 4 5 -> Break!
    ### Res: 6 -> 6 6 5 5 5 5 5 5 

main()