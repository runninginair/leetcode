''' 2131. Longest Palindrome by Concatenating Two Letter Words
Medium      809     20      Add to List     Share
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
 

Constraints:    1 <= words.length <= 105
                words[i].length == 2
                words[i] consists of lowercase English letters.
Accepted:       36,512
Submissions:    85,784
'''


from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        seen = set()
        seen_XX = set()
        ans = 0
        for word in words:
            if word == word[::-1]:
                if word in seen_XX:
                    ans += 4
                    seen_XX.remove(word)
                else:
                    seen_XX.add(word)
            else:
                if word[::-1] in seen:
                    seen.remove(word[::-1])
                    ans += 4
                    continue
                if word not in seen:
                    seen.add(word)
        if len(seen_XX) > 0: ans += 2
        return ans