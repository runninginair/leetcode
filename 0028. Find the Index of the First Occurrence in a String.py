''' 28. Find the Index of the First Occurrence in a String

Medium      1.7K      114       Companies

Given two strings needle and haystack, return the index of the first occurrence of
needle in haystack, or -1 if needle is not part of haystack.


Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:        1 <= haystack.length, needle.length <= 10^4
                    haystack and needle consist of only lowercase English characters.
Accepted:           1.6M
Submissions:        4.1M
Acceptance Rate:    38.1%
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def isSame(s1: str, s2: str) -> bool:
            return s1 == s2
        m, n = len(haystack), len(needle)
        if m < n: return -1
        for i in range(m - n + 1):
            if isSame(haystack[i: i + n], needle): return i
        return -1

class Solution_v1:  # T: O(m * n)   M: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if m < n: return -1
        for i in range(m - n + 1):
            if haystack[i: i + n] == needle: return i
        return -1

class Solution_builtin:  # T: O(m * n)   M: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


def main():
    sol = Solution()
    sol = Solution_v1()
    sol = Solution_builtin()

    haystack, needle = "sadbutsad", "sad"  # Output: 0
    print(sol.strStr(haystack, needle))

    haystack, needle = "leetcode", "leeto" # Output: -1
    print(sol.strStr(haystack, needle))

    haystack, needle = "ababababababababababaq", "abababababababaq" # Output: 6
    print(sol.strStr(haystack, needle))


if __name__ == "__main__":
    main()
