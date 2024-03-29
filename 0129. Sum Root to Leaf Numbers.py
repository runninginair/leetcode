''' 0129. Sum Root to Leaf Numbers

Medium      4933       92       Add to List     Share
Medium      5.5K       96       Companies

You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.

 * For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers.
Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
 

Example 1:      (1)
               /   \
            (2)     (3)

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:      (4)
               /   \
            (9)     (0)
           /   \
        (5)     (1)

Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 

Constraints:        The number of nodes in the tree is in the range [1, 1000].
                    0 <= Node.val <= 9
                    The depth of the tree will not exceed 10.

Accepted:       505,374
Submissions:    864,266

Accepted:           538.4K
Submissions:        907.1K
Acceptance Rate:    59.4%
'''


from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def sumNumbers(self, root: Optional[TreeNode]) -> int:
    def sumNumbers(self, root) -> int:
        lis = []
        # DFS
        if not root:
            return 0
        preSum = 0
        stack = [[root, preSum]]
        while stack:
            v = stack.pop(-1)
            print("Node.val =", v[0].val, "     preSum = ", v[1])
            if not v[0].left and not v[0].right:
                print("#0  Node.val =", v[0].val, "     preSum = ", v[1])
                lis.append(v[1] + int(v[0].val))

            if v[0].left:
                print("#1  Node.left.val =",
                      v[0].left.val, "     preSum = ", v[1])
                stack.append([v[0].left, v[0].val*10])
            if v[0].right:
                print("#2  Node.right.val =",
                      v[0].right.val, "     preSum = ", v[1])
                stack.append([v[0].right, v[0].val*10])
        print(lis)
        return sum(lis)


class Solution_v2:  # DFS iterative solution    T: O(n), M: O(n)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res, stack = 0, [[root, root.val]]
        while stack:
            v, preSum = stack.pop()
            if not v.left and not v.right:
                res += preSum
            if v.left:
                stack.append([v.left, preSum * 10 + v.left.val])
            if v.right:
                stack.append([v.right, preSum * 10 + v.right.val])
        return res


class Solution_v3:  # DFS recursive solution    T: O(n), M: O(n)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node, preSum) -> None:
            if not node.left and not node.right:
                self.res += node.val + 10 * preSum
            if node.left:
                dfs(node.left, node.val + 10 * preSum)
            if node.right:
                dfs(node.right, node.val + 10 * preSum)
        dfs(root, 0)
        return self.res


def main():
    # sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()

    m1, m2, m3 = TreeNode(1), TreeNode(2), TreeNode(3)
    m1.left, m1.right = m2, m3
    print(sol.sumNumbers(m1))               # Expect Output: 25

    [n1, n2, n3, n4, n5] = [TreeNode(4), TreeNode(9), TreeNode(0), TreeNode(5), TreeNode(1)]
    n1.left, n1.right, n2.left, n2.right = n2, n3, n4, n5
    print(sol.sumNumbers(n1))               # Expect Output: 1026


if __name__ == "__main__":
    main()
