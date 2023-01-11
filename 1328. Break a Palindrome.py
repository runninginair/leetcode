''' 1328. Break a Palindrome
Medium      893     480     Add to List     Share
Given a palindromic string of lowercase English letters palindrome, replace
exactly one character with any lowercase English letter so that the resulting
string is not a palindrome and that it is the lexicographically smallest one
possible.

Return the resulting string. If there is no way to replace a character to make
it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if
in the first position where a and b differ, a has a character strictly smaller
than the corresponding character in b. For example, "abcc" is lexicographically
smaller than "abcd" because the first position they differ is at the fourth
character, and 'c' is smaller than 'd'.


Example 1:
Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

Example 2:
Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
 

Constraints:    1 <= palindrome.length <= 1000
                palindrome consists of only lowercase English letters.
Accepted:       79,964
Submissions:    153,919

'''


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1: return ""
        if n == 2:
            if palindrome[0] == 'a': return "ab"
            else: return 'a'+palindrome[1]
        isOdd = n % 2 == 1
        mid = n // 2 if isOdd else -1
        isChanged = False
        lis = []
        
        for c in palindrome:
            lis.append(c)

        # for i, ele in enumerate(lis):
        # Here we can't use enumerate, case ele is another copy of lis[i], we can't make a change.
        for i in range(n):
            if i == mid: continue
            if lis[i] != 'a':
                lis[i] = 'a'
                isChanged = True
                break

        if not isChanged: lis[-1] = 'b'
        return ''.join(lis)


def main():
    sol = Solution()
    p = "abccba"        # Output: "aaccba"
    print(sol.breakPalindrome(p))

main()