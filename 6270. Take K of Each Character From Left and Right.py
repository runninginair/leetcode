''' 6270. Take K of Each Character From Left and Right

User Accepted:260       User Tried:434      Total Accepted:261
Total Submissions:694      Difficulty:Medium

You are given a string s consisting of the characters 'a', 'b', and 'c' and
a non-negative integer k. Each minute, you may take either the leftmost
character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each
character, or return -1 if it is not possible to take k of each character.


Example 1:
Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.

Example 2:
Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.
 

Constraints:    1 <= s.length <= 10^5
                s consists of only the letters 'a', 'b', and 'c'.
                0 <= k <= s.length
'''

import collections

class Solution:     ### Time Limit Exceeded  T: O(n^2)
    '''
###     index = 0   1   2   3   4   5   6   7   8   9   10  11
###     s, k = "a   a   b   a   a   a   a   c   a   a   b   c", 2

###         a:  0   1       3   4   5   6       8   9
###         b:          2                               10
###         c:                              7               11       
###              0       1       2       3       4       5      6       7       8       9       10      11      12
###      left [0,0,0],[1,0,0],[2,0,0],[2,1,0],[3,1,0],[4,1,1],[5,1,0][6,1,0],[6,1,1],[7,1,1],[8,1,1],[8,2,1],[8,2,2]
###     right [0,0,0],[0,0,1],[0,1,1],[1,1,1],[2,1,1],[2,1,2]

###     index = 0   1   2   3   4   5   6   7   8   9   10  11
###     s, k = "a   a   a   b   a   a   a   c   a   a   a   a", 1
    '''
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0
        ans = N = len(s)
        left, right = [[0,0,0] for _ in range(N + 1)], [[0,0,0] for _ in range(N + 1)]
        la = lb = lc = ra = rb = rc = 0
        for i in range(N):
            if s[i] == 'a': la += 1
            elif s[i] == 'b': lb += 1
            else: lc += 1
            if s[-i - 1] == 'a': ra += 1
            elif s[-i - 1] == 'b': rb += 1
            else: rc += 1
            right[i + 1], left[i + 1] = [ra, rb, rc].copy(), [la, lb, lc].copy()
        
        for count in left[-1]:
            if count < k: return -1
        
        # print(left, "\n", right, "\n")

        for i in range(N + 1):
            if i > ans: break
            for j in range(N + 1):
                if i + j > ans: break
                if (left[i][0] + right[j][0] >= k and 
                    left[i][1] + right[j][1] >= k and 
                    left[i][2] + right[j][2] >= k):
                    ans = min(ans, i + j)
                    break
        return ans

class Solution_v2:      ### LeetCode ID: 2020B0101056   Sliding Window O(n)
    def takeCharacters(self, s: str, k: int) -> int:
        ra, rb, rc = s.count('a') - k,  s.count('b') - k, s.count('c') - k
		# if any of them is less than 0, it means there are less than k occurences of a character.
        print("# 0: ", ra, rb, rc)
        if any(i < 0 for i in [ra, rb, rc]): return -1

        hm = collections.defaultdict(int)
        left = j = res = 0

        for char in s:
            hm[char] += 1
            left += 1
            print("# 1: ", " char =", char, " hm[char] =", hm[char], " left =", left)
            while hm['a'] > ra or hm['b'] > rb or hm['c'] > rc:
                print("## 2.1: ", hm[s[j]], left, j)
                hm[s[j]] -= 1
                left -= 1
                j += 1
                print("## 2.2: ", s[j - 1], hm[s[j - 1]], left, j)
            print("### 3:  res =", res, "  left =", left, end="\n\n")
            res = max(res, left)
        return len(s) - res

class Solution_v3:
    def takeCharacters(self, s: str, k: int) -> int:
        map = {'a': 0, 'b': 0, 'c': 0}
        for char in s: map[char] += 1
        if map['a'] < k or map['b'] < k or map['c'] < k: return -1
        ra, rb, rc = map['a'] - k, map['b'] - k, map['c'] - k
        
        map['a'] = map['b'] = map['c'] = ans = curr = ptr = 0
        for char in s:
            curr += 1
            map[char] += 1
            while map['a'] > ra or map['b'] > rb or map['c'] > rc:
                map[s[ptr]] -= 1
                ptr += 1
                curr -= 1
            ans = max(ans, curr)

        return len(s)  - ans

def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()


    s, k = "aabaaaacaabc", 2   # Output: 8
    print(sol.takeCharacters(s, k))

    s, k = "a", 1  # Output: -1
    print(sol.takeCharacters(s, k))

    s, k = "a", 0  # Output: 0
    print(sol.takeCharacters(s, k))

    s, k = "acba", 1    # Output: 3
    print(sol.takeCharacters(s, k))

    s, k = "caccbbba", 1    # Output: 3     127 / 138 testcases passed
    print(sol.takeCharacters(s, k))

main()            
