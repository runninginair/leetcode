''' 0655. Print Binary Tree

Medium      351     359     Companies

Given the root of a binary tree, construct a 0-indexed m x n string matrix res
that represents a formatted layout of the tree. The formatted layout matrix
should be constructed using the following rules:

 * The height of the tree is height and the number of rows "m" should be equal
    to height + 1.

 * The number of columns "n" should be equal to 2^(height + 1) - 1.

 * Place the root node in the middle of the top row
    (more formally, at location res[0][(n - 1) / 2]).
 
 * For each node that has been placed in the matrix at position res[r][c],
    place its left child at res[r + 1][c - 2^(height - r - 1)]
    and its right child at res[r + 1][c + 2^(height - r - 1)].
 
 * Continue this process until all the nodes in the tree have been placed.
 
 * Any empty cells should contain the empty string "".

Return the constructed matrix res.


Example 1:      (1)
               /
            (2)

Input: root = [1,2]
Output: [["", "1", ""],
         ["2", "", ""]]

Example 2:      (1)
               /   \
            (2)     (3)
               \
               (4)

Input: root = [1,2,3,null,4]
Output: [["", "", "", "1", "", "", ""],
         ["", "2","", "", "", "3", ""],
         ["", "", "4", "", "", "", ""]]

Constraints:        The number of nodes in the tree is in the range [1, 210].
                    -99 <= Node.val <= 99
                    The depth of the tree will be in the range [1, 10].
Accepted:           58.9K
Submissions:        95.1K
Acceptance Rate:    61.9%
'''

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        if not root:
            return []

        def getTreeDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            return 1 + max(getTreeDepth(root.left), getTreeDepth(root.right))
        m = getTreeDepth(root)   # m = height + 1 ==> height = m - 1
        n = 2 ** m - 1
        res = [["" for _ in range(n)] for _ in range(m)]
        row, root_col = 0, (n - 1) // 2
        que = [(root, root_col)]
        while que:
            level = []
            while que:
                level.append(que.pop(0))
            for node, col in level:
                res[row][col] = str(node.val)
                if node.left:
                    que.append((node.left, col - 2 ** (m - row - 2)))
                if node.right:
                    que.append((node.right, col + 2 ** (m - row - 2)))
            row += 1
        # print("----------")
        # for r in res: print(r)
        return res


def main():
    sol = Solution()

    m1, m2 = TreeNode(1), TreeNode(2)
    m1.left = m2
    print(sol.printTree(m1))

    p1, p2, p3, p4 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4)
    p1.left, p1.right, p2.right = p2, p3, p4
    print(sol.printTree(p1))

    n1, n2, n3, n4, n5, n7 = TreeNode(1), TreeNode(
        2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(7)
    n1.left, n1.right, n2.left, n2.right, n3.right = n2, n3, n4, n5, n7
    print(sol.printTree(n1))


if __name__ == "__main__":
    main()
