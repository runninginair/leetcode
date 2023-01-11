''' 6284. Make Number of Distinct Characters Equal

User Accepted:6
User Tried:10
Total Accepted:6
Total Submissions:13
Difficulty:Medium

You are given two 0-indexed strings word1 and word2.

A move consists of choosing two indices i and j such that
0 <= i < word1.length and 0 <= j < word2.length
and swapping word1[i] with word2[j].

Return true if it is possible to get the number of distinct characters in word1
and word2 to be equal with exactly one move. Return false otherwise.


Example 1:
Input: word1 = "ac", word2 = "b"
Output: false
Explanation: Any pair of swaps would yield two distinct characters in the first
string, and one in the second string.

Example 2:
Input: word1 = "abcc", word2 = "aab"
Output: true
Explanation: We swap index 2 of the first string with index 0 of the second string.
The resulting strings are word1 = "abac" and word2 = "cab", which both have 3 distinct characters.

Example 3:
Input: word1 = "abcde", word2 = "fghij"
Output: true
Explanation: Both resulting strings will have 5 distinct characters, regardless of which indices we swap.
 

Constraints:    1 <= word1.length, word2.length <= 10^5
                word1 and word2 consist of only lowercase English letters.
'''
import collections
from typing import List


class Solution:     ### LeetCode ID: shubham5545 -- Java2Py
    def isItPossible(self, word1: str, word2: str) -> bool:
        arr1, arr2 = [0 for _ in range(26)], [0 for _ in range(26)]
        def checkForSame(a: List[int], b: List[int]) -> bool:
            cnt1 = cnt2 = 0
            for c in a:
                if c != 0: cnt1 += 1
            for c in b:
                if c != 0: cnt2 += 1
            return cnt1 == cnt2

        for w1 in word1:
            i = ord(w1) - ord('a')
            if arr1[i] < 2: arr1[i] += 1
        for w2 in word2:
            i = ord(w2) - ord('a')
            if arr2[i] < 2: arr2[i] += 1
        
        for i in range(26):
            if arr1[i] == 0: continue
            arr1[i] -= 1

            for j in range(26):
                if arr2[j] == 0: continue
                arr2[j] -= 1
                arr1[j] += 1
                arr2[i] += 1
                if checkForSame(arr1, arr2): return True
                arr1[j] -= 1
                arr2[i] -= 1
                arr2[j] += 1

            arr1[i] += 1
        return False

class Solution_v2:     ### LeetCode ID: akaghosting    brute force
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1 = collections.Counter(word1)
        cnt2 = collections.Counter(word2)
        print(" cnt1:",cnt1, "\n cnt2:", cnt2)

        if len(word1) == len(word2) and len(cnt1) == len(cnt2):
            print("# 0 ---- True")
            return True

        for k1 in cnt1:
            for k2 in cnt2:
                n1, n2 = len(cnt1), len(cnt2)
                print("# 1: ---- k1 =", k1, "  k2 =", k2, "  n1 =", n1, "  n2 =", n2, "  cnt1[k1]:", cnt1[k1], "  cnt2[k2]:", cnt2[k2])
                if cnt1[k1] == 1: n1 -= 1
                if cnt2[k2] == 1: n2 -= 1
                print("# 2: ---- k1 =", k1, "  k2 =", k2, "  n1 =", n1, "  n2 =", n2)
                if k1 != k2:
                    if k2 not in cnt1: n1 += 1
                    if k1 not in cnt2: n2 += 1
                    print("# 3: ---- k1 =", k1, "  k2 =", k2, "  n1 =", n1, "  n2 =", n2, "\n")
                    if n1 == n2: return True
        print("# 4: ---- k1 =", k1, "  k2 =", k2, "  n1 =", n1, "  n2 =", n2, "\n")
        return False

class Solution_v2_2:     ### LeetCode ID: akaghosting    brute force
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1 = collections.Counter(word1)
        cnt2 = collections.Counter(word2)
        len1, len2 = len(cnt1), len(cnt2)
        if len1 == len2 and len(word1) == len(word2): return True
        elif abs(len1 - len2) > 2: return False
        for k1 in cnt1:
            for k2 in cnt2:
                n1, n2 = len1, len2
                if cnt1[k1] == 1: n1 -= 1
                if cnt2[k2] == 1: n2 -= 1
                if k1 != k2:
                    if k2 not in cnt1: n1 += 1
                    if k1 not in cnt2: n2 += 1
                    if n1 == n2: return True
        return False

class Solution_v3:     ### LeetCode ID: prudentprogrammer 
    def isItPossible(self, word1: str, word2: str) -> bool:
        cache1 = collections.Counter(word1)
        cache2 = collections.Counter(word2)
        
        for l1, c1 in cache1.items():
            for l2, c2 in cache2.items():
                temp1 = cache1.copy()
                temp2 = cache2.copy()

                temp1[l1] -= 1
                if temp1[l1] == 0:
                    del temp1[l1]

                temp2[l2] -= 1
                if temp2[l2] == 0:
                    del temp2[l2]

                temp1[l2] += 1
                temp2[l1] += 1
                if len(temp1.keys()) == len(temp2.keys()):
                    return True
        return False

class Solution_v4(object):
    def isItPossible(self, word1, word2):
        # O(len(word1) + len(word2))
        count1, count2 = {}, {}
        for char in word1:
            if char not in count1:
                count1[char] = 1
            else:
                count1[char] += 1
        for char in word2:
            if char not in count2:
                count2[char] = 1
            else:
                count2[char] += 1

        # scan the keys, and do swap(O(26 * 26))
        res = False
        for key1 in count1.keys():
            for key2 in count2.keys():
                count1_new = count1.copy()
                count2_new = count2.copy()

                # we should always check the redundant key
                count1_new[key1] -= 1
                if count1_new[key1] == 0:
                    count1_new.pop(key1)

                count2_new[key2] -= 1
                if count2_new[key2] == 0:
                    count2_new.pop(key2)

                # swap the element
                if key2 not in count1_new:
                    count1_new[key2] = 1
                else:
                    count1_new[key2] += 1

                if key1 not in count2_new:
                    count2_new[key1] = 1
                else:
                    count2_new[key1] += 1

                res = res or (len(count1_new) == len(count2_new))
                # early stopping
                if res:
                    break

            # early stopping
            if res:
                break

        return res


def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v2_2()
    # sol = Solution_v3()
    # sol = Solution_v4()

    word1, word2 = "ac", "b"                   ## Output: false
    print(sol.isItPossible(word1, word2))

    word1, word2 = "abcc", "aab"               ## Output: true
    print(sol.isItPossible(word1, word2))

    word1, word2 = "abcde",  "fghij"           ## Output: true
    print(sol.isItPossible(word1, word2))

    # "ac" & "c" -> True   "aac" & "c" -> False "aacc" & "cc" -> True   "acc" & "cc" -> False  "ac" & "b" -> False   "aaccc" -> "b" -> False
    # "abc" & "cc" -> True   "aabbcc" & "cc" -> False  "ac" & "b" -> False   "aaccc" -> "b" -> False

    word1, word2 = "abcdexxxyy",  "fghijz"     ## Output: False
    print(sol.isItPossible(word1, word2))

    word1, word2 = "a", "bb"                   ## Output: Flase
    print(sol.isItPossible(word1, word2))    


if __name__ == "__main__":
    main()
