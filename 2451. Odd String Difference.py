''' 2451. Odd String Difference

Easy    210     71      Companies

You are given an array of equal-length strings words.
Assume that the length of each string is n.

Each string words[i] can be converted into a difference integer array
difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j]
where 0 <= j <= n - 2.
Note that the difference between two letters is the difference between their
positions in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.

For example, for the string "acb", the difference integer array is
[2 - 0, 1 - 2] = [2, -1].
All the strings in words have the same difference integer array, except one.
You should find that string.

Return the string in words that has different difference integer array.


Example 1:
Input: words = ["adc","wzy","abc"]
Output: "abc"
Explanation: 
- The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
- The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
- The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1]. 
The odd array out is [1, 1], so we return the corresponding string, "abc".

Example 2:
Input: words = ["aaa","bob","ccc","ddd"]
Output: "bob"
Explanation: All the integer arrays are [0, 0] except for "bob",
which corresponds to [13, -13].
 

Constraints:        3 <= words.length <= 100
                    n == words[i].length
                    2 <= n <= 20
                    words[i] consists of lowercase English letters.
Accepted:           17.3K
Submissions:        28.9K
Acceptance Rate:    59.8%
'''

from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        n = len(words[0])
        mark, idxs, cnt = [], [], [0, 0]
        for idx, word in enumerate(words):
            diff = [0] * (n - 1)
            for i in range(1, n):
                diff[i - 1] = ord(word[i]) - ord(word[i - 1])
            if not mark:
                mark.append(diff)
                idxs.append(idx)
                cnt[0] += 1
            elif diff != mark[0]:
                mark.append(diff)
                idxs.append(idx)
                cnt[1] += 1
            elif diff == mark[0]: cnt[0] += 1
            elif diff == mark[1]: cnt[1] += 1
            print (idx, word)
            if cnt[0] and cnt[1] and sum(cnt) > 2:
                return words[idxs[0]] if cnt[0] < cnt[1] else words[idxs[1]]

def main():
    sol = Solution()

    words = ["adc","wzy","abc"]     # Output: "abc"
    print(sol.oddString(words))

    words = ["aaa","bob","ccc","ddd"]   # Output: "bob"
    print(sol.oddString(words))


if __name__ == "__main__":
    main()
