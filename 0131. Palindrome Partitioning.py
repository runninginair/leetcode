''' 131. Palindrome Partitioning
Medium      8526       264      Add to List     Share
Given a string s, partition s such that every substring of the partition is a
palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
 

Constraints:    1 <= s.length <= 16
                s contains only lowercase English letters.
Accepted:       532,050
Submissions:    853,979
'''

class Solution:
    # def partition(self, s: str) -> List[List[str]]:
    def partition(self, s: str):
        res = []
        # if len(s) == 1:
        #     res.append(s[0])
        #     return res
        n = len(s)
        
        def backTrack(s, cur, totalLength):
            # print(s, cur, totalLength)
            if totalLength >= n:
                if totalLength == n:
                    if self.listAllPalindrome(cur):
                        res.append(cur.copy())
                return
            
            for i in range(1, n+1):
                cur.append(s[:i])
                backTrack(s[i:], cur, totalLength + i)
                cur.pop()
                    
        backTrack(s, [], 0)
        return res

    def listAllPalindrome(self, lis):
        for s in lis:          
            if s != s[::-1]:
                return False
        return True

class Solution_v2:
    def partition(self, s: str):
        if not s: return [[]]
        res = []
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                for sur in self.partition(s[i:]):
                    res.append([s[:i]] + sur)
        return res

def main():
    sol = Solution_v2()
    # t1= ["aa","b","acaca"]
    # print(sol.listAllPalindrome(t1))

    # t2= ["aa","b","accaa"]
    # print(sol.listAllPalindrome(t2))
    s = "aab"
    print(sol.partition(s))

    s = "bb"
    print(sol.partition(s))

    s = "aaabaa"
    print(sol.partition(s))

main()
