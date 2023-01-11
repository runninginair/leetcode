''' 572. Subtree of Another Tree
Easy    6428    360     Add to List     Share

Given the roots of two binary trees root and subRoot, return true if there is
a subtree of root with the same structure and node values of subRoot and
false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and
all of this node's descendants. The tree tree could also be considered as a
subtree of itself.
 

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:    The number of nodes in the root tree is in the range [1, 2000].
                The number of nodes in the subRoot tree is in the range [1, 1000].
                -104 <= root.val <= 104
                -104 <= subRoot.val <= 104
Accepted:       579,829
Submissions:    1,261,764
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def isSubtree(self, root, subRoot) -> bool:
        def dfs(root):
            if root.val == subRoot.val:
                if bfs(root, subRoot): return True
            leftSub = dfs(root.left) if root.left else False
            rightSub = dfs(root.right) if root.right else False
            return leftSub or rightSub

        def bfs(root1, root2):
            q = [(root1, root2)]
            while q:
                n1, n2 = q.pop(0)
                if n1.val != n2.val:
                    return False
                if (n1.left and not n2.left) or (not n1.left and n2.left) or (n1.right and not n2.right) or (not n1.right and n2.right):
                    return False
                if n1.left:
                    q.append((n1.left, n2.left))
                if n1.right:
                    q.append((n1.right, n2.right))
            return True
        return dfs(root)


def main():
    sol = Solution()
    # root = [3,4,5,1,2], subRoot = [4,1,2] Output: true
    n1, n2, n3, n4, n5 = TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(1), TreeNode(2), 
    m1, m2, m3 = TreeNode(4), TreeNode(1), TreeNode(2)
    n1.left, n1.right, n2.left, n2.right = n2, n3, n4, n5
    m1.left, m1.right = m2, m3
    print(sol.isSubtree(n1, m1))

    
   # root = [1,1], subRoot = [1] Output: true
    n1, n2 = TreeNode(1), TreeNode(1)
    m1 = TreeNode(1)
    n1.left = n2
    print(sol.isSubtree(n1, m1))   

main()
