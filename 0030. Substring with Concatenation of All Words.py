''' 30. Substring with Concatenation of All Words

Hard    461     25      Companies

You are given a string s and an array of strings words.
All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of
any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef",
"cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not
a concatenated substring because it is not the concatenation of any permutation
of words.
Return the starting indices of all the concatenated substrings in s.
You can return the answer in any order.


Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated
substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"]
which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"]
which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated
substring has to be of length 16.
There is no substring of length 16 is s that is equal to the concatenation of
any permutation of words.
We return an empty array.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3, the concatenated
substring has to be of length 9.
The substring starting at 6 is "foobarthe". It is the concatenation of
["foo","bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo". It is the concatenation of
["bar","the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar". It is the concatenation of
["the","foo","bar"] which is a permutation of words.
 

Constraints:        1 <= s.length <= 10^4
                    1 <= words.length <= 5000
                    1 <= words[i].length <= 30
                    s and words[i] consist of lowercase English letters.
Accepted:           328.4K
Submissions:        1.1M
Acceptance Rate:    31.0%
'''

from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans, map = [], {}
        len_s, len_words, len_word = len(s), len(words), len(words[0])
        if len_s < len_words or len_s < len_word or len_s < len_word * len_words: return ans
        for word in words:
            if word in map: map[word] += 1
            else: map[word] = 1

        def isPermutation(s: str) -> bool:
            mapc = map.copy()
            for i in range(0, len_words * len_word, len_word):
                piece = s[i: i + len_word]
                if piece in mapc:
                    mapc[piece] -= 1
                    if mapc[piece] < 0: return False
                else: return False
            return True

        for i in range(0, len_s - len_word * len_words + 1):
            if s[i: i + len_word] in map:
                if isPermutation(s[i: i + len_word * len_words]): ans.append(i)
        return ans


def main():
    sol = Solution()

    s, words = "barfoothefoobarman", ["foo","bar"]     # Output: [0,9]
    print(sol.findSubstring(s, words))

    s, words = "wordgoodgoodgoodbestword", ["word","good","best","word"]   # Output: []
    print(sol.findSubstring(s, words))

    s, words = "barfoofoobarthefoobarman", ["bar","foo","the"]    # Output: [6,9,12]
    print(sol.findSubstring(s, words))

    s, words = "wordgoodgoodgoodbestword", ["word","good","best","good"]   # Output: [8]
    print(sol.findSubstring(s, words))



if __name__ == "__main__":
    main()

