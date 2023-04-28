''' 6362. Find the Longest Balanced Substring of a Binary String
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Easy
You are given a binary string s consisting only of zeroes and ones.

A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

Return the length of the longest balanced substring of s.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "01000111"
Output: 6
Explanation: The longest balanced substring is "000111", which has length 6.
Example 2:

Input: s = "00111"
Output: 4
Explanation: The longest balanced substring is "0011", which has length 4. 
Example 3:

Input: s = "111"
Output: 0
Explanation: There is no balanced substring except the empty substring, so the answer is 0.
 

Constraints:

1 <= s.length <= 50
'0' <= s[i] <= '1'

'''
# class Solution:
#     def fuc(self):
#         return -1

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = cnt0 = cnt1 = 0
        for c in s:
            if c == '0':
                if cnt1 == 0:
                    cnt0 += 1
                else:
                    res = max(res, 2 * min(cnt0, cnt1))
                    cnt0, cnt1 = 1, 0

            else:
                cnt1 += 1
                res = max(res, 2 * min(cnt0, cnt1))
        return res



def main():
    sol = Solution()

    # print(sol.fuc())
    s = "01000111"  # Output: 6
    print(sol.findTheLongestBalancedSubstring(s))

    s = "00111" # Output: 4
    print(sol.findTheLongestBalancedSubstring(s))

    s = "111"   # Output: 0
    print(sol.findTheLongestBalancedSubstring(s))

    s = "101"   # Output: 0
    print(sol.findTheLongestBalancedSubstring(s))

main()