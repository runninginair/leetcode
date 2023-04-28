''' 0000_Netflix_OA_Question_4

2023 Summer Netflix Bootcamp OA1 CodeSignal

Give an integer array "numbers", and an integer k, find out the amount of the
sub-array of the "numbers" which contains exactly k pair elements.


Example 1:
Input:
numbers = [1, 2, 1, 2, 1]
k = 2
Output: 3
Explanation:
[1, 2, 1, 2], [1, 2, 1, 2, 1], [2, 1, 2, 1] So, the result is 3.


Example 2:
Input:
numbers = [2, 2, 2, 2, 2, 2]
k = 3
Output: 1
Explanation:
The numbers only contains three pairs of 2, So, the result is 3.


Example 1:
Input:
numbers = [1, 3, 3, 1]
k = 1
Output: 3
Explanation:
[1, 3, 3], [3, 3], [3, 3, 1] So, the result is 3.


numbers.length <= 5,000

'''

from typing import List


class Solution:
    def countSubArr(self, numbers: List[int], k: int) -> int:
        ### Start your code here.
        return -1


def main():
    sol = Solution()

    numbers = [1, 2, 1, 2, 1]
    k = 2       #    Output: 3
    print(sol.countSubArr(numbers, k))


main()