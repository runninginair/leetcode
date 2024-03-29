''' 6319. Number of Even and Odd Bits
    2595. Number of Even and Odd Bits

Easy        9       7       Companies

You are given a positive integer n.

Let "even" denote the number of even indices in the binary representation of n
(0-indexed) with value 1.

Let "odd" denote the number of odd indices in the binary representation of n
(0-indexed) with value 1.

Return an integer array answer where answer = [even, odd].


Example 1:
Input: n = 17
Output: [2,0]
Explanation: The binary representation of 17 is 10001. 
             It contains 1 on the 0th and 4th indices. 
             There are 2 even and 0 odd indices.

Example 2:
Input: n = 2
Output: [0,1]
Explanation: The binary representation of 2 is 10.
             It contains 1 on the 1st index. 
             There are 0 even and 1 odd indices.
 

Constraints:        1 <= n <= 1000
Accepted:           12.5K
Submissions:        19K
Acceptance Rate:    65.7%
'''

from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        rev_bin_n = str(bin(n))[::-1]
        even = odd = 0
        print(rev_bin_n)

        for i in range(len(rev_bin_n)-2):
            if i & 1:
                if rev_bin_n[i] == '1': odd += 1
            else:
                if rev_bin_n[i] == '1': even += 1

        return [even, odd]

def main():
    sol = Solution()

    print(sol.evenOddBit(17))
    print(sol.evenOddBit(2))

if __name__ == "__main__":
    main()
