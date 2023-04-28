''' 459. Repeated Substring Pattern

Easy        4.2K        376         Companies

Given a string s, check if it can be constructed by taking a substring of it
and appending multiple copies of the substring together.


Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:        1 <= s.length <= 104
                    s consists of lowercase English letters.
Accepted:           286K
Submissions:        654.2K
Acceptance Rate:    43.7%
'''


class Solution_Wrong:  # NOT Correct!!!
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)
        if N == 1:
            return False
        cut, map = 1, set()
        for i in range(N):
            if s[i] not in map:
                map.add(s[i])
                cut = i + 1
            else:
                break
        print(cut, map)

        if cut == N or N % cut != 0:
            return False
        for i in range(cut, N, cut):
            if s[i: i + cut] != s[:cut]:
                return False
        return True


#   abc abc abc
#   1
#    2
#     3

class Solution_Correct:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)
        if N == 1:
            return False
        for i in range(1, (N >> 1) + 1):
            if N % i == 0:
                isSame = True
                for j in range(i, N, i):
                    if s[:i] != s[j: j + i]:
                        isSame = False
                        break
                if isSame:
                    return True
        return False


def main():
    sol = Solution_Wrong()
    sol = Solution_Correct()

    s = "abab"              # Output: True
    print(sol.repeatedSubstringPattern(s))

    s = "aba"               # Output: False
    print(sol.repeatedSubstringPattern(s))

    s = "abcabcabcabc"      # Output: True
    print(sol.repeatedSubstringPattern(s))

    s = "bb"                # Output: True
    print(sol.repeatedSubstringPattern(s))

    s = "abaababaab"        # Output: True
    print(sol.repeatedSubstringPattern(s))


if __name__ == "__main__":
    main()
