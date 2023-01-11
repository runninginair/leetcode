''' 214. Shortest Palindrome
Hard    2906    206     Add to List     Share

You are given a string s. You can convert s to a palindrome by adding
characters in front of it.

Return the shortest palindrome you can find by performing this transformation.


Example 1:
Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: s = "abcd"
Output: "dcbabcd"
 
Constraints:    0 <= s.length <= 5 * 10^4
                s consists of lowercase English letters only.
Accepted:       148,114
Submissions:    459,725
'''


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        N = len(s)
        if N < 2: return s
        
        key = 0
        for i in range(1, N):
            if self.isPalindrome(s[:i + 1]):
                key = i + 1
        if key == N: return s
        prefix = s[key:][::-1]
        # print(prefix, "--", s)
        return prefix + s

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

def main():
    sol = Solution()
    s = "aacecaaa"
    print(sol.shortestPalindrome(s))

main()
