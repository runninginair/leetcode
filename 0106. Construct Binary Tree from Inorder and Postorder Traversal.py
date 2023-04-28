''' 106. Construct Binary Tree from Inorder and Postorder Traversal

Medium      6.1K      89       Companies

Given two integer arrays inorder and postorder where inorder is the inorder
traversal of a binary tree and postorder is the postorder traversal of the
same tree, construct and return the binary tree.


Example 1:          (3)
                   /   \
                (9)     (20)
                        /   \
                      (15)   (7)

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:          (-1)

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:        1 <= inorder.length <= 3000
                    postorder.length == inorder.length
                    -3000 <= inorder[i], postorder[i] <= 3000
                    inorder and postorder consist of unique values.
                    Each value of postorder also appears in inorder.
                    inorder is guaranteed to be the inorder traversal of the tree.
                    postorder is guaranteed to be the postorder traversal of the tree.
Accepted:           475.6K
Submissions:        812.6K
Acceptance Rate:    58.5%
'''

from typing import List, Optional

class BstNode:      ### A solution for printing the BST. 

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = BstNode(key)
            else:
                self.right.insert(key)
        else: # self.key > key
            if self.left is None:
                self.left = BstNode(key)
            else:
                self.left.insert(key)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if postorder and inorder:
            rootValue, length = postorder[-1], len(postorder)
            root = TreeNode(rootValue)
            key = inorder.index(rootValue)
            root.left = self.buildTree(inorder[:key], postorder[:key])
            root.right = self.buildTree(inorder[key + 1:], postorder[key:length - 1])
            return root
        return None
        
class Solution_v2:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            root = TreeNode(postorder.pop())
            indexInorder = inorder.index(root.val)
            root.right = self.buildTree(inorder[indexInorder+1:], postorder)
            root.left = self.buildTree(inorder[:indexInorder], postorder)
            return root
        return None

class Solution_v3:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i
        def recur(low, high):
            if low > high: return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid+1, high)
            x.left = recur(low, mid-1)
            return x
        return recur(0, len(inorder)-1)

def main():
    sol = Solution()
    sol = Solution_v2()
    sol = Solution_v3()

    inorder, postorder = [9, 3, 15, 20, 7], [9, 15, 7, 20, 3]
    print(sol.buildTree(inorder, postorder))

if __name__ == "__main__":
    main()
