''' 93. Restore IP Addresses

Medium      3.4K      671       Companies

A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits, return all possible valid IP addresses
that can be formed by inserting dots into s. You are not allowed to reorder or
remove any digits in s. You may return the valid IP addresses in any order.


Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:        1 <= s.length <= 20
                    s consists of digits only.
Accepted:           338.3K
Submissions:        768.2K
Acceptance Rate:    44.0%
'''

from typing import List


class Solution_v0:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n, res = len(s), []
        if n < 4 or n > 12: return []
        def isValidInt(num: str) -> bool:
            if num == "" or len(num) > 3 or (len(num) > 1 and num[0] == '0'): return False
            return int(num) <= 255
        
        def backTrack(s: str, curr: List[str]) -> None:
            if len(curr) == 3 and isValidInt(s): res.append(".".join(curr + [s]))
            for i in range(1, 4):
                if isValidInt(s[:i]):
                    curr.append(s[:i])
                    backTrack(s[i:], curr)
                    curr.remove(s[:i])      ### Bug is here !!!
        backTrack(s, [])
        return res

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n, res = len(s), []
        if n < 4 or n > 12: return []
        def isValidInt(num: str) -> bool:
            if num == "" or len(num) > 3 or (len(num) > 1 and num[0] == '0'): return False
            return int(num) <= 255
        
        def backTrack(s: str, curr: List[str]) -> None:
            if len(curr) == 3:
                if isValidInt(s): res.append(".".join(curr + [s]))
                else: return
            for i in range(1, 4):
                if isValidInt(s[:i]):
                    curr.append(s[:i])
                    backTrack(s[i:], curr)
                    curr.pop()
        backTrack(s, [])
        return res


class Solution_v2:     ### Iteration Solution
    def restoreIpAddresses(self, s: str) -> List[str]:
        n, res = len(s), []
        if n < 4 or n > 12: return []
        def iSvalidIP(arr: List[str]) -> bool:
            for a in arr:
                if int(a) > 255 or (a[0] == '0' and len(a) > 1): return False
            return True
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    if i + j + k > n - 1 or i + j + k < n - 3: continue
                    arr = [s[:i], s[i:i + j], s[i + j:i + j + k], s[i + j + k:]]
                    if iSvalidIP(arr): res.append('.'.join(arr))
        return res

class Solution_v2_2:     ### Iteration Solution
    def restoreIpAddresses(self, s: str) -> List[str]:
        n, res = len(s), []
        if n < 4 or n > 12: return []
        def isValidInt(a: str) -> bool:
            return False if int(a) > 255 or (a[0] == '0' and len(a) > 1) else True
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    if i + j + k > n - 1 or i + j + k < n - 3: continue
                    if isValidInt(s[:i]) and isValidInt(s[i:i+j]) and isValidInt(s[i+j:i+j+k]) and isValidInt(s[i+j+k:]):
                        res.append('.'.join([s[:i], s[i:i+j], s[i+j:i+j+k], s[i+j+k:]]))
        return res


def main():
    sol = Solution_v0()     ### Has Bug
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v2_2()


    s = "25525511135"       ### Output: ["255.255.11.135", "255.255.111.35"]
    print(sol.restoreIpAddresses(s))

    s = "0000"              ### Output: ["0.0.0.0"]
    print(sol.restoreIpAddresses(s))

    s = "101023"            ### Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    print(sol.restoreIpAddresses(s))

    s = "19216811"          ### Solution_v0 Failed Test Case (# 128)   127 / 145 testcases passed      
    # Expect output: ["1.92.168.11", "19.2.168.11", "19.21.68.11", "19.216.8.11", "19.216.81.1", "192.1.68.11", "192.16.8.11", "192.16.81.1", "192.168.1.1"]
    # Actual output: ['92.1.168.11', '19.2.168.11', '19.21.68.11', '19.216.8.11', '19.216.81.1', '192.1.68.11', '192.16.8.11', '192.16.81.1', '192.168.1.1']
    print(sol.restoreIpAddresses(s))


if __name__ == "__main__":
    main()
