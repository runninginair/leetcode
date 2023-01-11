''' 394. Decode String
Medium      9873      433      Add to List      Share

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the
square brackets is being repeated exactly k times.

Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid;
there are no extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k.

For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed
10^5.


Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:    1 <= s.length <= 30
                s consists of lowercase English letters, digits, and square brackets '[]'.
                s is guaranteed to be a valid input.
                All the integers in s are in the range [1, 300].
Accepted:       590,490
Submissions:    1,024,091

'''

class Solution:
    def decodeString(self, s: str) -> str:
        N = len(s)
        stack = []
        res = ""
        counter = 0
        for i in range(N):
            if s[i] == '[':
                stack.append(str(counter))
                counter = 0
                stack.append("")
            elif s[i] == ']':
                temp = stack.pop() * int(stack.pop())
                if not stack:
                    res += temp
                else:
                    stack[-1] += temp
            elif '0' <= s[i] <= '9':
                counter = 10 * counter + int(s[i])
            else:
                if stack: stack[-1] += s[i]
                else: res += s[i]
            # print(stack, counter, res)
        return res

def main():
    sol = Solution()
    # s = "3[a]2[bc]" # Output: "aaabcbc"
    # print(sol.decodeString(s))

    # s = "3[a2[c]]"  # Output: "accaccacc"
    # print(sol.decodeString(s))

    # s = "2[abc]3[cd]ef" # Output: "abcabccdcdcdef"
    # print(sol.decodeString(s))

    s = "100[leetcode]"
    print(sol.decodeString(s))


main()
