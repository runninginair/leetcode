''' 899. Orderly Queue
Hard      622       368     Add to List     Share

You are given a string s and an integer k. You can choose one of the first k
letters of s and append it at the end of the string..

Return the lexicographically smallest string you could have after applying the
mentioned step any number of moves.


Example 1:
Input: s = "cba", k = 1
Output: "acb"
Explanation: 
In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".

Example 2:
Input: s = "baaca", k = 3
Output: "aaabc"
Explanation: 
In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".
 

Constraints:    1 <= k <= s.length <= 1000
                s consist of lowercase English letters.
Accepted:       27,505
Submissions:    46,650

'''

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        return min([s[i:] + s[:i] for i in range(len(s))]) if k == 1 else ''.join(sorted(s)) 

def main():
    sol = Solution()
    s, k = "cba", 1    # Output: "acb"
    print(sol.orderlyQueue(s, k))

    s, k = "baaca", 3  # Output: "aaabc"
    print(sol.orderlyQueue(s, k))


main()
