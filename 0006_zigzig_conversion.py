'''
6. Zigzag Conversion
Medium      4372       9676     Add to List     Share
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for
better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number
of rows:

    string convert(string s, int numRows);
 

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
 
Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

Accepted:       849,652
Submissions:    1,986,426
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows >= n: return s

        rows, ptr, dir, res = [[] for _ in range(numRows)], 0, -1, ""
        for ch in s:
            rows[ptr].append(ch)
            if ptr == 0 or ptr == numRows - 1:
                dir *= -1
            ptr += dir
        # return ''.join(rows[i]) 
        for i in range(numRows):
            res += "".join(rows[i])
        return res


def main():
    sol = Solution()
    s, k = "PAYPALISHIRING", 3  # PAHNAPLSIIGYIR
    print(sol.convert(s, k))

    s, k = "PAYPALISHIRING", 4  # PINALSIGYAHRPI
    print(sol.convert(s, k))

main()
