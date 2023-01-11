''' 38. Count and Say
Medium      2047    4567    Add to List     Share
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":


Given a positive integer n, return the nth term of the count-and-say sequence.
 

Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.


Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
 

Constraints:    1 <= n <= 30
Accepted:       677,822
Submissions:    1,364,041

'''

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'
        if n == 2: return '11'
        memo = ['' for _ in range(n + 1)]
        memo[1], memo[2] = '1', '11'
        
        for i in range(3, n+1):
            p1 = 0
            p2 = 1
            count = 1
            word = []
            while p2 <= len(memo[i-1]):
                # print("memo[i-1] -->", memo[i-1])
                while p2 < len(memo[i-1]) and memo[i-1][p2] == memo[i-1][p1]:
                    p2 += 1
                    count +=1
                word.append(str(count) + memo[i-1][p1])
                # print(word)
                p1 = p2
                p2 += 1
                count = 1
            memo[i] = ''.join(word)

        return memo[n]


def main():
    sol = Solution()

    # print(sol.countAndSay(3))
    # print(sol.countAndSay(4))
    # print(sol.countAndSay(5))
    res = []
    for i in range(30, 31):
        res.append(sol.countAndSay(i))

    print(res)

main()
