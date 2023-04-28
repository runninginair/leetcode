''' 427. Construct Quad Tree

Medium      Liked: 788      Disliked: 1.1K      Companies

Given a n * n matrix grid of 0's and 1's only. We want to represent the grid
with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf
is False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly
four children. Besides, each node has two attributes:

 * val: True if the node represents a grid of 1's or False if the node
        represents a grid of 0's.

 * isLeaf: True if the node is leaf node on the tree or False if the node has
           the four children.

class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}

We can construct a Quad-Tree from a two-dimensional area using the following
steps:

    (1) If the current grid has the same value (i.e all 1's or all 0's) set
isLeaf True and set val to the value of the grid and set the four children to
Null and stop.

    (2) If the current grid has different values, set isLeaf to False and set
val to any value and divide the current grid into four sub-grids as shown in
the photo.

    (3) Recurse for each of the children with the proper sub-grid.

        -----------------------------
        |             |             |
        |   topLeft   |  topRight   |
        |             |             |
        -----------------------------
        |             |             |
        | bottomLeft  | bottomRight |
        |             |             |
        -----------------------------

    If you want to know more about the Quad-Tree, you can refer to the wiki.
    https://en.wikipedia.org/wiki/Quadtree

Quad-Tree format:

The output represents the serialized format of a Quad-Tree using level order traversal,
where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that
the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and
if the value of isLeaf or val is False we represent it as 0.


Example 1:
Input: grid = [[0, 1],
               [1, 0]]
Output: [[0, 1],
         [1, 0], [1, 1], [1, 1], [1, 0]]
Explanation: The explanation of this example is shown below: ...
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.


Example 2:
Input: grid = [[1, 1, 1, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 0, 0, 0, 0]]
Output: [[0, 1],
         [1, 1],                [0, 1],                 [1, 1],                 [1, 0],
         null,null,null,null,   [1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below: ...

 
Constraints:        n == grid.length == grid[i].length
                    n == 2^x where 0 <= x <= 6
Accepted:           63.7K
Submissions:        91.4K
Acceptance Rate:    69.7%
'''

from typing import List

"""     ### Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def __str__(self) -> str:
        if self.isLeaf:
            if self.val: return "[1, 1]"
            else: return "[1, 0]"
        else: return ("{[0, 1], [" +
                      self.topLeft.__str__() + ", " +
                      self.topRight.__str__() + ", " +
                      self.bottomLeft.__str__() + ", " +
                      self.bottomRight.__str__()) + "]}"

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        N = len(grid[0])
        if N == 1:
            return Node(grid[0][0] == 1, True, None, None, None, None)
        else:
            half = N >> 1
            tl = self.construct([grid[i][0 : half] for i in range(half)])
            tr = self.construct([grid[i][half : N] for i in range(half)])
            bl = self.construct([grid[i][0 : half] for i in range(half, N)])
            br = self.construct([grid[i][half : N] for i in range(half, N)])
            if (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf
                and tl.val == tr.val == bl.val == br.val):
                return Node(tl.val, True, None, None, None, None)
            else:
                return Node(False, False, tl, tr, bl, br)

def main():
    ### Test Node.__str__(), here we created a Quad-tree as Example 1,
    n1 = Node(False, True, None, None, None, None)
    n2 = Node(True, True, None, None, None, None)
    n3 = Node(True, True, None, None, None, None)
    n4 = Node(False, True, None, None, None, None)
    n0 = Node(False, False, n1, n2, n3, n4)
    # print(n0)    # Expect Output: [[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]

    sol = Solution()

    grid = [[0, 1], [1, 0]]
    # Expect Output: [[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]
    print(sol.construct(grid))

    grid = [[1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0]]
    print(sol.construct(grid))

    grid = [[1, 1, 0, 0],
            [0, 0, 1, 1],
            [1, 1, 0, 0],
            [0, 0, 1, 1]]
    print(sol.construct(grid))


if __name__ == "__main__":
    main()
