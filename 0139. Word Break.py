''' 139. Word Break
Medium      12678       531      Add to List     Share

Given a string s and a dictionary of strings wordDict, return true if s can be
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.


Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:    1 <= s.length <= 300
                1 <= wordDict.length <= 1000
                1 <= wordDict[i].length <= 20
                s and wordDict[i] consist of only lowercase English letters.
                All the strings of wordDict are unique.
Accepted:       1,233,726
Submissions:    2,716,688
'''

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [1 for _ in range(n)]
        
        for word in wordDict:
            l = len(word)
            for i in range(n):
                if s[i:i+l] == word:
                    for k in range(l):
                        memo[k] = 0
        return sum(memo) == 0


def main():
    sol = Solution()
    s, wordDict = "leetcode", ["leet","code"]   # Output: true
    print(sol.wordBreak(s, wordDict))

main()
