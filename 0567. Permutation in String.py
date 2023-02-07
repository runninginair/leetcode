''' 567. Permutation in String

Medium      8.1K      267       Companies

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.


Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:        1 <= s1.length, s2.length <= 104
                    s1 and s2 consist of lowercase English letters.
Accepted:           546.6K
Submissions:        1.3M
Acceptance Rate:    43.5%

'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n, dic1 = len(s1), len(s2), {}
        if m > n: return False
        for char in s1:
            if char in dic1: dic1[char] += 1
            else: dic1[char] = 1

        def isPermutations(word2: str) -> bool:
            dic2 = dic1.copy()
            for char in word2:
                if char in dic2:
                    dic2[char] -= 1
                    if dic2[char] < 0: return False
                else: return False
            return True
        
        for i in range(n - m + 1):
            # print(s2[i:i + m])
            if isPermutations(s2[i:i + m]): return True
        return False

def main():
    sol = Solution()

    s1, s2 = "ab", "eidbaooo"       # Expect output: True
    print(sol.checkInclusion(s1, s2))

    s1, s2 = "ab", "eidboaoo"       # Expect output: False
    print(sol.checkInclusion(s1, s2))

    s1, s2 = "adc", "dcda"          # Expect output: True
    print(sol.checkInclusion(s1, s2))


if __name__ ==  "__main__":
    main()
