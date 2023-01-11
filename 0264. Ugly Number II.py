''' 264. Ugly Number II
Medium     4829    242    Add to List   Share

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

Constraints:    1 <= n <= 1690
Accepted:       287,938
Submissions:    623,339

'''


class Solution: ### Brute Force    O(n^2)
    def nthUglyNumber(self, n: int) -> int:
        if n < 7: return n
        i, num = 7, 7
        while True:
            num += 1
            if self.isUglyNumber(num):
                if i == n: return num
                i += 1

    def isUglyNumber(self, num: int) -> bool:
        if num < 1: return False
        elif num < 7: return True
        while num % 5 == 0: num //= 5
        while num % 3 == 0: num //= 3
        while num % 2 == 0: num //= 2
        return num == 1

class Solution_v2: ### Sliding Window  O(n)
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        two = three = five = 0
        while len(ugly) < n:
            while ugly[two] * 2 <= ugly[-1]: two += 1
            while ugly[three] * 3 <= ugly[-1]: three += 1
            while ugly[five] * 5 <= ugly[-1]: five += 1
            ugly.append(min(ugly[two] * 2, ugly[three] * 3, ugly[five] * 5))
        return ugly[-1]


def main():
    # sol = Solution()
    sol = Solution_v2()
    for n in range(1, 21):
        print("n:", n, " - ",sol.nthUglyNumber(n))

main()
