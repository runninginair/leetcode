''' 99. Recover Binary Search Tree
Medium  6235    207 Add to List Share
You are given the root of a binary search tree (BST), where the values of
exactly two nodes of the tree were swapped by mistake.
Recover the tree without changing its structure.

Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

Constraints:
The number of nodes in the tree is in the range [2, 1000].
-2^31 <= Node.val <= 2^31 - 1

Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
Accepted:   364,325
Submissions:726,077

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def recoverTree(self, root: Optional[TreeNode]) -> None:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # inorder traversal the tree. store nodes' value to an array.
        arr = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            arr.append(node)
            dfs(node.right)
        
        lis = sorted(n.val for n in arr)
        
        for i in range(len(arr)):
            arr[i].val = lis[i]


def main():
    sol = Solution()
    n1, n2, n3, n4 = TreeNode(3), TreeNode(1), TreeNode(4), TreeNode(2)
    n1.left, n1.right, n3.left = n2, n3, n4




main()