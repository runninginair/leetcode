''' 6269. Shortest Distance to Target String in a Circular Array

User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Easy

You are given a 0-indexed circular string array words and a string target.
A circular array means that the array's end connects to the array's beginning.

Formally, the next element of words[i] is words[(i + 1) % n] and the previous
element of words[i] is words[(i - 1 + n) % n], where n is the length of words.
Starting from startIndex, you can move to either the next word or the previous
word with 1 step at a time.

Return the shortest distance needed to reach the string target.
If the string target does not exist in words, return -1.


Example 1:
Input: words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
Output: 1
Explanation: We start from index 1 and can reach "hello" by
- moving 3 units to the right to reach index 4.
- moving 2 units to the left to reach index 4.
- moving 4 units to the right to reach index 0.
- moving 1 unit to the left to reach index 0.
The shortest distance to reach "hello" is 1.

Example 2:
Input: words = ["a","b","leetcode"], target = "leetcode", startIndex = 0
Output: 1
Explanation: We start from index 0 and can reach "leetcode" by
- moving 2 units to the right to reach index 3.
- moving 1 unit to the left to reach index 3.
The shortest distance to reach "leetcode" is 1.

Example 3:
Input: words = ["i","eat","leetcode"], target = "ate", startIndex = 0
Output: -1
Explanation: Since "ate" does not exist in words, we return -1.
 

Constraints:        1 <= words.length <= 100
                    1 <= words[i].length <= 100
                    words[i] and target consist of only lowercase English letters.
                    0 <= startIndex < words.length
'''

from typing import List


class Solution: ### Passed.
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target: return 0
        N, arr, ans = len(words), [], float('inf')
        for i in range(N):
            if words[i] == target: arr.append(i)
        if not arr: return -1
        
        # print(arr)
        for a in arr:
            ans = min(ans, abs(a - startIndex), abs(startIndex + N - a), abs(a + N - startIndex))
        return ans

def main():
    sol = Solution()

    words, target, startIndex = ["hello","i","am","leetcode","hello"], "hello", 1
    print(sol.closetTarget(words, target, startIndex))   # Output: 1

    words, target, startIndex = ["a","b","leetcode"], "leetcode", 0
    print(sol.closetTarget(words, target, startIndex))   # Output: 1

    words, target, startIndex = ["i","eat","leetcode"], "ate", 0
    print(sol.closetTarget(words, target, startIndex))   # Output: -1

    words, target, startIndex = ["hsdqinnoha","mqhskgeqzr","zemkwvqrww","zemkwvqrww","daljcrktje","fghofclnwp","djwdworyka","cxfpybanhd","fghofclnwp","fghofclnwp"], "zemkwvqrww", 8
    print(sol.closetTarget(words, target, startIndex))   # Output: 4

if __name__ == "__main__":
    main()
