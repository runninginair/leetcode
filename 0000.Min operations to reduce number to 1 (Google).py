''' 0000.Min operations to reduce number to 1(Google)

Sithis      Moderator       22137       Last Edit: May 5, 2020 12:12 PM     12.7K VIEWS

Given a positive integer n and 3 operations on n:

 * n = n - 1
 * n = n / 2 (if and only if n is even)
 * n = n / 3 (if and only if n % 3 == 0)

Find the minimum number of above operations to reduce n to 1.


Example 1:

Input: n = 9
Output: 2
Explanation:
Step 1: 9 / 3 = 3
Step 2: 3 / 3 = 1

Example 2:

Input: n = 8
Output: 3
Explanation:
Step 1: 8 / 2 = 4
Step 2: 4 / 2 = 2
Step 3: 2 - 1 = 1

Example 3:

Input: n = 28
Output: 4
'''

class Solution:
    def minimumStepsToOne(n: int) -> int:
        return 0

def main():
    sol = Solution()

if __name__ == "__main__":
    main()
