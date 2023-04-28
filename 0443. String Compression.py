''' 443. String Compression

Medium      Liked: 2.9K     Disliked: 4.9K      Companies

Given an array of characters "chars", compress it using the following algorithm:

Begin with an empty string "s". For each group of consecutive repeating characters
in "chars":

 * If the group's length is 1, append the character to "s".
 * Otherwise, append the character followed by the group's length.

The compressed string "s" should not be returned separately, but instead, be stored
in the input character array "chars". Note that group lengths that are 10 or longer
will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.


Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be:
        ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single
character.

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be:
        ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:        1 <= chars.length <= 2000
    chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
    
Accepted:           309.1K
Submissions:        623.8K
Acceptance Rate:    49.6%

'''

from typing import List

class Solution:         # T: O(n)   M: O(n)
    def compress(self, chars: List[str]) -> int:
        N, s, cnt, cur = len(chars), [], 1, chars[0]
        if N == 1: return 1
        for i in range(1, N):
            if chars[i] == chars[i - 1]:
                cnt += 1
            else:
                s.append(cur)
                if cnt > 1:
                    nums = str(cnt)
                    for num in nums: s.append(num)
                cur, cnt = chars[i], 1
        s.append(cur)
        if cnt > 1:
            nums = str(cnt)
            for num in nums: s.append(num)
        for i in range(len(s)): chars[i] = s[i]
        return len(s)

class Solution_v2:      # T: O(n)   M: O(1)
    def compress(self, chars: List[str]) -> int:
        N, cur, cnt, ptr = len(chars), chars[0], 1, 0
        if N == 1: return 1
        for i in range(1, N):
            if chars[i] == chars[i - 1]: cnt += 1
            else:
                chars[ptr] = cur
                ptr += 1
                if cnt > 1:
                    for num in str(cnt):
                        chars[ptr] = num
                        ptr += 1
                cur, cnt = chars[i], 1
        chars[ptr] = cur
        ptr += 1
        if cnt > 1:
            for num in str(cnt):
                chars[ptr] = num
                ptr += 1
        # print(chars[:ptr])
        return ptr

def main():
    sol = Solution()
    sol = Solution_v2()

    chars = ["a","a","b","b","c","c","c"]
    # Output: Return 6,
    # the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
    print(sol.compress(chars))  # Expect output: 6

    chars = ["a"]
    # Output: Return 1
    # the first character of the input array should be: ["a"]
    print(sol.compress(chars))  # Expect output: 1


    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    # Output: Return 4
    # the first 4 characters of the input array should be: ["a","b","1","2"].
    print(sol.compress(chars))  # Expect output: 4


if __name__ == "__main__":
    main()
