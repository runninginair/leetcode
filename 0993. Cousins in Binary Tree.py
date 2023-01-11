''' 993. Cousins in Binary Tree
Easy    3198    164     Add to List     Share

Given the root of a binary tree with unique values and the values of two
different nodes of the tree x and y, return true if the nodes corresponding to
the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with
different parents.

Note that in a binary tree, the root node is at the depth 0, and children of
each depth k node are at the depth k + 1.
 

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Constraints:    The number of nodes in the tree is in the range [2, 100].
                1 <= Node.val <= 100
                Each node has a unique value.
                x != y
                x and y are exist in the tree.
Accepted:       227,471
Submissions:    420,135
'''

# Definition for a binary tree node.
from tkinter import N


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
    def isCousins(self, root, x: int, y: int) -> bool:
        if not root: return False
        if root.val == x or root.val == y: return False
        
        index_x = index_y = 0
        arr = []
        level = []
        # Use queue to store root node as tuple (node, node's parent, depth)
        q = [(root, None, 0)]

        while q:
            while q:
                level.append(q.pop(0))
                for node in level:
                    if node:
                        arr.append(node.val)
                    else:
                        arr.append(None)
                    if node and node.left: q.append(node.left)
                    else: q.append(None)
                    if node and node.right: q.append(node.right)

                    else: q.append(None)
            level = []
        print(arr)

        for i in range(len(arr)):
            if arr[i] == x: index_x = i
            elif arr[i] == y: index_y = i
        
        if (index_x - 1) // 2 == (index_y - 1) // 2: return False
        
        l_x = l_y = 0
        while index_x > 2 ** l_x:
            l_x += 1
        while index_y > 2 ** l_y:
            l_y += 1
        return l_x == l_y


def main():
    sol = Solution()
    ### Input: root = [1,2,3,4], x = 4, y = 3
    n1, n2, n3, n4 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4)
    n1.left, n1.right, n2.left = n2, n3, n4 
    x, y = 4, 3     # Output: false
    print(sol.isCousins(n1, x, y))

    n1, n2, n3, n4, n5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
    n1.left, n1.right, n2.left, n2.right, n3.left, n3.right = n2, n3, None, n4, None, n5 
    # Input: root = [1,2,3,null,4,null,5], 
    x, y = 5, 4 # Output: true
    print(sol.isCousins(n1, x, y))

main()

