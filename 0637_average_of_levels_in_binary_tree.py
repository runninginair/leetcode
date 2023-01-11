'''
637. Average of Levels in Binary Tree
'''
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    def averageOfLevels(self, root:TreeNode):
        if not root:
            return None

        answer = []
        level = level_count = level_sum = 0
        que = collections.deque([root, 0])
        while que:
            cur, d = que.popleft()
            if d == level:
                level_count += 1
                level_sum += cur.val
            else:
                answer.append(level_sum/level_count)
                level = d
                level_count = 1
                level_sum = cur.val
            if cur.left: que.append(cur.left, d+1)
            if cur.right: que.append(cur.right, d+1)
        if level_count:
            answer.append(level_sum/level_count)
        return answer

def main():
    n4 = TreeNode(15)
    n5 = TreeNode(7)
    n3 = TreeNode(20, n4, n5)
    n2 = TreeNode(9)
    n1 = TreeNode(3, n2, n3)
    root = n1

    s = Solution()
    print(s.averageOfLevels(root))

main()
