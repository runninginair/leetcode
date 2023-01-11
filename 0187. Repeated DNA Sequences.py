''' 187. Repeated DNA Sequences
Medium      2429        444     Add to List     Share
The DNA sequence is composed of a series of nucleotides abbreviated as
'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long 
sequences (substrings) that occur more than once in a DNA molecule.
You may return the answer in any order.

 

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 
Constraints:    1 <= s.length <= 105
                s[i] is either 'A', 'C', 'G', or 'T'.
Accepted:       294,887
Submissions:    640,678

'''

class Solution:
    def findRepeatedDnaSequences(self, s: str):
        n = len(s)
        if n <= 10:
            return []
        res = []
        for i in range(n - 10):
            for j in range(i + 1, n - 9):
                print(s[i: i+10])
                if s[i: i+10] == s[j: j+10] and s[i: i+10] not in res:
                    res.append(s[i: i+10])
        return res


def main():
    sol = Solution()
    # s = "AAAAAAAAAAAAA"     # Output: ["AAAAAAAAAA"]
    # print(sol.findRepeatedDnaSequences(s))

    s = "AAAAAAAAAAA"
    print(sol.findRepeatedDnaSequences(s))


main()
