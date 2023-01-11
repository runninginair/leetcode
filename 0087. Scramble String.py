''' 87. Scramble String

Hard       1.9K       978       Companies

We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:

 * Split the string into two non-empty substrings at a random index,
   i.e., if the string is s, divide it to x and y where s = x + y.
 * Randomly decide to swap the two substrings or to keep them in the same order. 
   i.e., after this step, s may become s = x + y or s = y + x.
 * Apply step 1 recursively on each of the two substrings x and y.

Given two strings s1 and s2 of the same length, return true if s2 is a
scrambled string of s1, otherwise, return false.


Example 1:
Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now, and the result string is "rgeat" which is s2.
As one possible scenario led s1 to be scrambled to s2, we return true.

Example 2:
Input: s1 = "abcde", s2 = "caebd"
Output: false

Example 3:
Input: s1 = "a", s2 = "a"
Output: true
 
Constraints:        s1.length == s2.length
                    1 <= s1.length <= 30
                    s1 and s2 consist of lowercase English letters.
Accepted:           159.1K
Submissions:        440.7K
Acceptance Rate:    36.1%
'''

from collections import Counter
from functools import lru_cache


class Solution:     ### YouTuber: Hua Hua Jiang
    ### Time Limit Exceeded     286 / 288 testcases passed
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2 or s1 == s2[::-1]: return True
        if Counter(s1) != Counter(s2): return False
        L = len(s1)
        for k in range(1, L):
            if self.isScramble(s1[0:k], s2[0:k]) and self.isScramble(s1[k:], s2[k:]):
                return True
            if self.isScramble(s1[0:k], s2[-k:]) and self.isScramble(s1[k:], s2[:L - k]):
                return True
        return False

class Solution_v2:     ### YouTuber: Hua Hua
    @lru_cache(maxsize=None)    # optional
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2 or s1 == s2[::-1]: return True
        if Counter(s1) != Counter(s2): return False
        L = len(s1)
        for k in range(1, L):
            if self.isScramble(s1[0:k], s2[0:k]) and self.isScramble(s1[k:], s2[k:]):
                return True
            if self.isScramble(s1[0:k], s2[-k:]) and self.isScramble(s1[k:], s2[:L - k]):
                return True
        return False

def main():
    # sol = Solution()
    sol = Solution_v2()

    s1, s2 = "great", "rgeat"       # Output: true
    print(sol.isScramble(s1, s2))

    s1, s2 = "abcde", "caebd"       # Output: false
    print(sol.isScramble(s1, s2))

    s1, s2 = "a", "a"               # Output: true
    print(sol.isScramble(s1, s2))

    ### The 287 / 288 testcases
    s1, s2 = "eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd"
    print(sol.isScramble(s1, s2))    # Output: False

main()