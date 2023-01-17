''' 1061. Lexicographically Smallest Equivalent String

Medium      691     49      Companies

You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

 * For example, if s1 = "abc" and s2 = "cde",
   then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.

Equivalent characters follow the usual rules of any equivalence relation:

 * Reflexivity: 'a' == 'a'.
 * Symmetry: 'a' == 'b' implies 'b' == 'a'.
 * Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.

For example, given the equivalency information from s1 = "abc" and s2 = "cde",
"acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the
lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the
equivalency information from s1 and s2.


Example 1:
Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in s1 and s2, we can group
their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in lexicographical order.
So the answer is "makkek".

Example 2:
Input: s1 = "hello", s2 = "world", baseStr = "hold"
Output: "hdld"
Explanation: Based on the equivalency information in s1 and s2, we can group
their characters as [h,w], [d,e,o], [l,r].
So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".

Example 3:
Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
Output: "aauaaaaada"
Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c],
[l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are
transformed to 'a', the answer is "aauaaaaada".
 

Constraints:        1 <= s1.length, s2.length, baseStr <= 1000
                    s1.length == s2.length
                    s1, s2, and baseStr consist of lowercase English letters.
Accepted:           22K
Submissions:        29.5K
Acceptance Rate:    74.4%
'''

class Solution:     ### Wrong Answer    108 / 116 testcases passed
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(u: chr) -> chr:
            if u not in map: map[u] = u
            while u != map[u]:
                map[u] = map[map[u]]
                u = map[u]
            return map[u]

        def union(p: chr, q: chr) -> None:
            root_p, root_q = find(p), find(q)
            map[root_p] = map[root_q] = min(root_p, root_q)

        n, map, ans = len(s1), {}, []
        for i in range(n): map[s1[i]] = map[s2[i]] = min(s1[i], s2[i])
        for i in range(n): union(s1[i], s2[i])
        for char in baseStr: ans.append(map[char] if char in map else char)

        return "".join(ans)

class Solution_v2:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        UF = {}     ### UF stands for Union Find
        def find(x: chr) -> chr:
            if x not in UF: UF[x] = x
            if x != UF[x]: UF[x] = find(UF[x])
            return UF[x]

        def union(p: chr, q: chr) -> None:
            root_p, root_q = find(p), find(q)
            if root_p > root_q: UF[root_p] = root_q
            else: UF[root_q] = root_p

        n, ans = len(s1), []
        for i in range(n): union(s1[i], s2[i])
        for cha in baseStr: ans.append(find(cha))

        return "".join(ans)

def main():
    sol = Solution()
    # sol = Solution_v2()

    # s1, s2, baseStr = "parker", "morris", "parser"   # Output: "makkek"
    # print(sol.smallestEquivalentString(s1, s2, baseStr))

    # s1, s2, baseStr = "hello", "world", "hold"      # Output: "hdld"
    # print(sol.smallestEquivalentString(s1, s2, baseStr))

    s1, s2, baseStr = "leetcode", "programs", "sourcecode"    # Output: "aauaaaaada"
    print(sol.smallestEquivalentString(s1, s2, baseStr))

    # s1 =      "opecenadojbodihfgmpijpfocomhcncicefpohkibjckijghii"
    # s2 =      "ndlbhpaeppgekfhnjnmmplmdoifdhbglmedpjgleofgnahglbe"
    # baseStr = "ttusuhhrabgsswpaapxoxdanchyccmpjitwwmfioedtbiggfru"
    # # Expect: "ttusuaaraaasswaaaaxaxaaaaayaaaaaatwwaaaaaataaaaaru"
    # # Output: "ttusuaaraaasswbaabxbxbabbaybbbbaatwwbbababtaaaabru"
    # print(sol.smallestEquivalentString(s1, s2, baseStr))

main()
