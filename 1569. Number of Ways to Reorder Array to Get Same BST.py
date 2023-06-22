''' 1569. Number of Ways to Reorder Array to Get Same BST

Hard    686     79      Companies

Given an array nums that represents a permutation of integers from 1 to n. 
We are going to construct a binary search tree (BST) by inserting the elements 
of nums in order into an initially empty BST. Find the number of different ways 
to reorder nums so that the constructed BST is identical to that formed from 
the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, 
and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] 
yields a different BST.

Return the number of ways to reorder nums such that the BST formed is identical 
to the original BST formed from nums.

Since the answer may be very large, return it modulo 10^9 + 7.


Example 1:          (2)
                   /   \
                (1)     (3)

Input: nums = [2, 1, 3]
Output: 1
Explanation: We can reorder nums to be [2, 3, 1] which will yield the same BST.
There are no other ways to reorder nums which will yield the same BST.


Example 2:          (3)
                   /   \
                (1)     (4)
                  \        \
                  (2)       (5)
                  
Input: nums = [3, 4, 5, 1, 2]
Output: 5
Explanation: The following 5 arrays will yield the same BST: 
[3, 1, 2, 4, 5]
[3, 1, 4, 2, 5]
[3, 1, 4, 5, 2]
[3, 4, 1, 2, 5]
[3, 4, 1, 5, 2]


Example 3:          (1)
                       \
                        (2)
                           \
                            (3)
Input: nums = [1, 2, 3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.
 

Example 4:           (3)
                   /     \
                (1)       (5)
                   \     /   \
                   (2)  (4)   (6)

Input: nums = [3, 1, 2, 5, 4, 6]
Output: 19

Constraints:        1 <= nums.length <= 1000
                    1 <= nums[i] <= nums.length
                    All integers in nums are distinct.
Accepted:           15.2K
Submissions:        29.8K
Acceptance Rate:    51.0%

'''


from typing import List


class Tree:
    def __init__(self, nums: List[int]):
        self.root = Node(nums[0])
        for i in range(1, len(nums)):
            cur, pre = self.root, None
            while cur:
                pre = cur
                if nums[i] < cur.val:
                    cur = cur.left
                else: cur = cur.right
            if nums[i] < pre.val: pre.left = Node(nums[i])
            else: pre.right = Node(nums[i])

class Node:
    def __init__(self, v: int):
        self.val = v
        self.left = None
        self.right = None

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        if not nums: return 0
        t = Tree(nums)
        q = [t.root]
        while q:
            nxt = []
            for node in q:
                print(node.val)
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            q = nxt
        return -1


class Solution_v2:

    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        return (self.countBST(nums) - 1 + MOD) % MOD

    def countBST(self, nums: List[int]) -> int:
        if len(nums) <= 2: return 1

        left = []
        right = []
        root = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < root:
                left.append(nums[i])
            else:
                right.append(nums[i])

        leftCount = self.countBST(left)
        rightCount = self.countBST(right)

        totalCount = self.binomialCoefficient(len(left) + len(right), len(left))
        MOD = 10**9 + 7
        return (leftCount * rightCount * totalCount) % MOD

    def binomialCoefficient(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            dp[i][0] = 1
            for j in range(1, min(i, k) + 1):
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD

        return dp[n][k]


def main():
    sol = Solution()
    sol = Solution_v2()

    nums = [2,1,3]              # Output: 1
    print(sol.numOfWays(nums))

    nums = [3,4,5,1,2]          # Output: 5
    print(sol.numOfWays(nums))

    nums = [1,2,3]              # Output: 0
    print(sol.numOfWays(nums))

    nums = [3, 1, 2, 5, 4, 6]   # Output: 19
    print(sol.numOfWays(nums))


if __name__ == "__main__":
    main()