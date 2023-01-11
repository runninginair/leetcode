''' 132. Palindrome Partitioning II
Hard    4165    96      Add to List     Share

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1


Constraints:    1 <= s.length <= 2000
                s consists of lowercase English letters only.
Accepted:       225,396
Submissions:    671,018
'''

class Solution:
    def minCut(self, s):
        cut = [x for x in range(-1,len(s))]
        print(cut)
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if s[i:j] == s[j:i:-1]:
                    print(i, j, "\t s[i:j]:", s[i:j], s[j:i:-1])
                    cut[j + 1] = min(cut[j + 1], cut[i] + 1)
                    print(cut)
        return cut[-1]


def main():
    sol = Solution()
    s = 'abccbacc'
    s = 'abcba'
    print(list(s))
    print(sol.minCut(s))

main()
